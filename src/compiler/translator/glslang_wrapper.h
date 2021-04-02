//
// Copyright 2021 The ANGLE Project Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.
//
// glslang_wrapper:
//   A wrapper to compile GLSL strings to SPIR-V blobs.  glslang here refers to the Khronos
//   compiler.
//

#ifndef COMPILER_TRANSLATOR_GLSLANG_WRAPPER_H_
#define COMPILER_TRANSLATOR_GLSLANG_WRAPPER_H_

#include "GLSLANG/ShaderLang.h"
#include "common/PackedEnums.h"

#include <string>
#include <vector>

namespace sh
{
#if defined(ANGLE_ENABLE_VULKAN) || defined(ANGLE_ENABLE_METAL)
void GlslangInitialize();
void GlslangFinalize();

// Generate SPIR-V out of intermediate GLSL through glslang.
ANGLE_NO_DISCARD bool GlslangCompileToSpirv(const ShBuiltInResources &resources,
                                            sh::GLenum shaderType,
                                            const std::string &shaderSource,
                                            std::vector<uint32_t> *spirvBlobOut);
#else
ANGLE_INLINE void GlslangInitialize()
{
    UNREACHABLE();
}
ANGLE_INLINE void GlslangFinalize()
{
    UNREACHABLE();
}
#endif  // defined(ANGLE_ENABLE_VULKAN) || defined(ANGLE_ENABLE_METAL)
}  // namespace sh

#endif  // COMPILER_TRANSLATOR_GLSLANG_WRAPPER_H_
