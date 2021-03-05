//
// Copyright 2020 The ANGLE Project Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.
//
// DriverUniform.cpp: Add code to support driver uniforms
//

#include "compiler/translator/tree_util/DriverUniform.h"

#include "compiler/translator/Compiler.h"
#include "compiler/translator/IntermNode.h"
#include "compiler/translator/StaticType.h"
#include "compiler/translator/SymbolTable.h"
#include "compiler/translator/tree_util/FindMain.h"
#include "compiler/translator/tree_util/IntermNode_util.h"
#include "compiler/translator/tree_util/IntermTraverse.h"
#include "compiler/translator/util.h"

namespace sh
{

namespace
{
constexpr ImmutableString kEmulatedDepthRangeParams = ImmutableString("ANGLEDepthRangeParams");

constexpr const char kViewport[]               = "viewport";
constexpr const char kClipDistancesEnabled[]   = "clipDistancesEnabled";
constexpr const char kXfbActiveUnpaused[]      = "xfbActiveUnpaused";
constexpr const char kXfbVerticesPerInstance[] = "xfbVerticesPerInstance";
constexpr const char kXfbBufferOffsets[]       = "xfbBufferOffsets";
constexpr const char kAcbBufferOffsets[]       = "acbBufferOffsets";
constexpr const char kDepthRange[]             = "depthRange";
constexpr const char kNumSamples[]             = "numSamples";

constexpr const char kHalfRenderArea[] = "halfRenderArea";
constexpr const char kFlipXY[]         = "flipXY";
constexpr const char kNegFlipXY[]      = "negFlipXY";
constexpr const char kFragRotation[]   = "fragRotation";
}  // anonymous namespace

// Class DriverUniform
bool DriverUniform::addComputeDriverUniformsToShader(TIntermBlock *root, TSymbolTable *symbolTable)
{
    constexpr size_t kNumComputeDriverUniforms                                               = 1;
    constexpr std::array<const char *, kNumComputeDriverUniforms> kComputeDriverUniformNames = {
        {kAcbBufferOffsets}};

    ASSERT(!mDriverUniforms);
    // This field list mirrors the structure of ComputeDriverUniforms in ContextVk.cpp.
    TFieldList *driverFieldList = new TFieldList;

    const std::array<TType *, kNumComputeDriverUniforms> kDriverUniformTypes = {{
        new TType(EbtUInt, 4),
    }};

    for (size_t uniformIndex = 0; uniformIndex < kNumComputeDriverUniforms; ++uniformIndex)
    {
        TField *driverUniformField =
            new TField(kDriverUniformTypes[uniformIndex],
                       ImmutableString(kComputeDriverUniformNames[uniformIndex]), TSourceLoc(),
                       SymbolType::AngleInternal);
        driverFieldList->push_back(driverUniformField);
    }

    // Define a driver uniform block "ANGLEUniformBlock" with instance name "ANGLEUniforms".
    mDriverUniforms = DeclareInterfaceBlock(
        root, symbolTable, driverFieldList, EvqUniform, TMemoryQualifier::Create(), 0,
        ImmutableString(vk::kDriverUniformsBlockName), ImmutableString(vk::kDriverUniformsVarName));
    return mDriverUniforms != nullptr;
}

TFieldList *DriverUniform::createUniformFields(TSymbolTable *symbolTable) const
{
    constexpr size_t kNumGraphicsDriverUniforms                                                = 8;
    constexpr std::array<const char *, kNumGraphicsDriverUniforms> kGraphicsDriverUniformNames = {
        {kViewport, kClipDistancesEnabled, kXfbActiveUnpaused, kXfbVerticesPerInstance, kNumSamples,
         kXfbBufferOffsets, kAcbBufferOffsets, kDepthRange}};

    // This field list mirrors the structure of GraphicsDriverUniforms in ContextVk.cpp.
    TFieldList *driverFieldList = new TFieldList;

    const std::array<TType *, kNumGraphicsDriverUniforms> kDriverUniformTypes = {{
        new TType(EbtFloat, 4),
        new TType(EbtUInt),  // uint clipDistancesEnabled;  // 32 bits for 32 clip distances max
        new TType(EbtUInt),
        new TType(EbtInt),
        new TType(EbtInt),
        new TType(EbtInt, 4),
        new TType(EbtUInt, 4),
        createEmulatedDepthRangeType(symbolTable),
    }};

    for (size_t uniformIndex = 0; uniformIndex < kNumGraphicsDriverUniforms; ++uniformIndex)
    {
        TField *driverUniformField =
            new TField(kDriverUniformTypes[uniformIndex],
                       ImmutableString(kGraphicsDriverUniformNames[uniformIndex]), TSourceLoc(),
                       SymbolType::AngleInternal);
        driverFieldList->push_back(driverUniformField);
    }

    return driverFieldList;
}

TType *DriverUniform::createEmulatedDepthRangeType(TSymbolTable *symbolTable) const
{
    // Init the depth range type.
    TFieldList *depthRangeParamsFields = new TFieldList();
    depthRangeParamsFields->push_back(new TField(new TType(EbtFloat, EbpHigh, EvqGlobal, 1, 1),
                                                 ImmutableString("near"), TSourceLoc(),
                                                 SymbolType::AngleInternal));
    depthRangeParamsFields->push_back(new TField(new TType(EbtFloat, EbpHigh, EvqGlobal, 1, 1),
                                                 ImmutableString("far"), TSourceLoc(),
                                                 SymbolType::AngleInternal));
    depthRangeParamsFields->push_back(new TField(new TType(EbtFloat, EbpHigh, EvqGlobal, 1, 1),
                                                 ImmutableString("diff"), TSourceLoc(),
                                                 SymbolType::AngleInternal));
    // This additional field might be used by subclass such as TranslatorMetal.
    depthRangeParamsFields->push_back(new TField(new TType(EbtFloat, EbpHigh, EvqGlobal, 1, 1),
                                                 ImmutableString("reserved"), TSourceLoc(),
                                                 SymbolType::AngleInternal));

    TStructure *emulatedDepthRangeParams = new TStructure(
        symbolTable, kEmulatedDepthRangeParams, depthRangeParamsFields, SymbolType::AngleInternal);

    TType *emulatedDepthRangeType = new TType(emulatedDepthRangeParams, false);

    return emulatedDepthRangeType;
}

// The Add*DriverUniformsToShader operation adds an internal uniform block to a shader. The driver
// block is used to implement Vulkan-specific features and workarounds. Returns the driver uniforms
// variable.
//
// There are Graphics and Compute variations as they require different uniforms.
bool DriverUniform::addGraphicsDriverUniformsToShader(TIntermBlock *root, TSymbolTable *symbolTable)
{
    ASSERT(!mDriverUniforms);

    TType *emulatedDepthRangeType = createEmulatedDepthRangeType(symbolTable);
    // Declare a global depth range variable.
    TVariable *depthRangeVar =
        new TVariable(symbolTable->nextUniqueId(), kEmptyImmutableString, SymbolType::Empty,
                      TExtension::UNDEFINED, emulatedDepthRangeType);

    DeclareGlobalVariable(root, depthRangeVar);

    TFieldList *driverFieldList = createUniformFields(symbolTable);
    // Define a driver uniform block "ANGLEUniformBlock" with instance name "ANGLEUniforms".
    mDriverUniforms = DeclareInterfaceBlock(
        root, symbolTable, driverFieldList, EvqUniform, TMemoryQualifier::Create(), 0,
        ImmutableString(vk::kDriverUniformsBlockName), ImmutableString(vk::kDriverUniformsVarName));

    return mDriverUniforms != nullptr;
}

TIntermBinary *DriverUniform::createDriverUniformRef(const char *fieldName) const
{
    size_t fieldIndex =
        FindFieldIndex(mDriverUniforms->getType().getInterfaceBlock()->fields(), fieldName);

    TIntermSymbol *angleUniformsRef = new TIntermSymbol(mDriverUniforms);
    TConstantUnion *uniformIndex    = new TConstantUnion;
    uniformIndex->setIConst(static_cast<int>(fieldIndex));
    TIntermConstantUnion *indexRef =
        new TIntermConstantUnion(uniformIndex, *StaticType::GetBasic<EbtInt>());
    return new TIntermBinary(EOpIndexDirectInterfaceBlock, angleUniformsRef, indexRef);
}

TIntermBinary *DriverUniform::getViewportRef() const
{
    return createDriverUniformRef(kViewport);
}

TIntermBinary *DriverUniform::getAbcBufferOffsets() const
{
    return createDriverUniformRef(kAcbBufferOffsets);
}

TIntermBinary *DriverUniform::getXfbActiveUnpaused() const
{
    return createDriverUniformRef(kXfbActiveUnpaused);
}

TIntermBinary *DriverUniform::getXfbVerticesPerInstance() const
{
    return createDriverUniformRef(kXfbVerticesPerInstance);
}

TIntermBinary *DriverUniform::getXfbBufferOffsets() const
{
    return createDriverUniformRef(kXfbBufferOffsets);
}

TIntermBinary *DriverUniform::getClipDistancesEnabled() const
{
    return createDriverUniformRef(kClipDistancesEnabled);
}

TIntermBinary *DriverUniform::getDepthRangeRef() const
{
    return createDriverUniformRef(kDepthRange);
}

TIntermBinary *DriverUniform::getDepthRangeReservedFieldRef() const
{
    TIntermBinary *depthRange = createDriverUniformRef(kDepthRange);

    return new TIntermBinary(EOpIndexDirectStruct, depthRange, CreateIndexNode(3));
}

TIntermBinary *DriverUniform::getNumSamplesRef() const
{
    return createDriverUniformRef(kNumSamples);
}

//
// Class DriverUniformExtended
//
TFieldList *DriverUniformExtended::createUniformFields(TSymbolTable *symbolTable) const
{
    TFieldList *driverFieldList = DriverUniform::createUniformFields(symbolTable);

    constexpr size_t kNumGraphicsDriverUniformsExt = 4;
    constexpr std::array<const char *, kNumGraphicsDriverUniformsExt>
        kGraphicsDriverUniformNamesExt = {{kHalfRenderArea, kFlipXY, kNegFlipXY, kFragRotation}};

    const std::array<TType *, kNumGraphicsDriverUniformsExt> kDriverUniformTypesExt = {{
        new TType(EbtFloat, 2),
        new TType(EbtFloat, 2),
        new TType(EbtFloat, 2),
        // NOTE: There's a vec2 gap here that can be used in the future
        new TType(EbtFloat, 2, 2),
    }};

    for (size_t uniformIndex = 0; uniformIndex < kNumGraphicsDriverUniformsExt; ++uniformIndex)
    {
        TField *driverUniformField =
            new TField(kDriverUniformTypesExt[uniformIndex],
                       ImmutableString(kGraphicsDriverUniformNamesExt[uniformIndex]), TSourceLoc(),
                       SymbolType::AngleInternal);
        driverFieldList->push_back(driverUniformField);
    }

    return driverFieldList;
}

TIntermBinary *DriverUniformExtended::getFlipXYRef() const
{
    return createDriverUniformRef(kFlipXY);
}

TIntermBinary *DriverUniformExtended::getNegFlipXYRef() const
{
    return createDriverUniformRef(kNegFlipXY);
}

TIntermSwizzle *DriverUniformExtended::getNegFlipYRef() const
{
    // Create a swizzle to "negFlipXY.y"
    TIntermBinary *negFlipXY    = createDriverUniformRef(kNegFlipXY);
    TVector<int> swizzleOffsetY = {1};
    TIntermSwizzle *negFlipY    = new TIntermSwizzle(negFlipXY, swizzleOffsetY);
    return negFlipY;
}

TIntermBinary *DriverUniformExtended::getFragRotationMatrixRef() const
{
    return createDriverUniformRef(kFragRotation);
}

TIntermBinary *DriverUniformExtended::getHalfRenderAreaRef() const
{
    return createDriverUniformRef(kHalfRenderArea);
}

}  // namespace sh
