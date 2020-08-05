// Copyright (c) 2020 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "source/fuzz/transformation_replace_copy_object_with_store_load.h"
#include "test/fuzz/fuzz_test_util.h"

namespace spvtools {
namespace fuzz {
namespace {

TEST(TransformationReplaceCopyObjectWithStoreLoad, BasicScenarios) {
  std::string reference_shader = R"(
               OpCapability Shader
          %1 = OpExtInstImport "GLSL.std.450"
               OpMemoryModel Logical GLSL450
               OpEntryPoint Fragment %4 "main" %23
               OpExecutionMode %4 OriginUpperLeft
               OpSource ESSL 310
               OpName %4 "main"
               OpName %8 "a"
               OpName %10 "b"
               OpName %14 "c"
               OpName %16 "d"
               OpName %18 "e"
               OpName %23 "f"
          %2 = OpTypeVoid
          %3 = OpTypeFunction %2
          %6 = OpTypeInt 32 1
          %7 = OpTypePointer Function %6
          %9 = OpConstant %6 2
         %11 = OpConstant %6 3
         %12 = OpTypeFloat 32
         %13 = OpTypePointer Function %12
         %15 = OpConstant %12 2
         %17 = OpConstant %12 3
         %22 = OpTypePointer Private %12
         %23 = OpVariable %22 Private
          %4 = OpFunction %2 None %3
          %5 = OpLabel
          %8 = OpVariable %7 Function
         %10 = OpVariable %7 Function
         %14 = OpVariable %13 Function
         %16 = OpVariable %13 Function
         %18 = OpVariable %7 Function
               OpStore %8 %9
               OpStore %10 %11
               OpStore %14 %15
               OpStore %16 %17
         %19 = OpLoad %6 %8
         %20 = OpLoad %6 %10
         %21 = OpIAdd %6 %19 %20
               OpStore %18 %21
         %24 = OpLoad %12 %14
         %25 = OpLoad %12 %16
         %26 = OpFMul %12 %24 %25
               OpStore %23 %26
         %27 = OpCopyObject %6 %21
         %28 = OpCopyObject %12 %26
         %40 = OpCopyObject %13 %14
               OpReturn
               OpFunctionEnd
  )";

  const auto env = SPV_ENV_UNIVERSAL_1_4;
  const auto consumer = nullptr;
  const auto context =
      BuildModule(env, consumer, reference_shader, kFuzzAssembleOption);

  FactManager fact_manager;
  spvtools::ValidatorOptions validator_options;
  TransformationContext transformation_context(&fact_manager,
                                               validator_options);
  ASSERT_TRUE(IsValid(env, context.get()));

  // Invalid: fresh_variable_id=10 is not fresh.
  auto transformation_invalid_1 = TransformationReplaceCopyObjectWithStoreLoad(
      27, 10, SpvStorageClassFunction, 9);
  ASSERT_FALSE(transformation_invalid_1.IsApplicable(context.get(),
                                                     transformation_context));

  // Invalid: copy_object_result_id=26 is not a CopyObject instruction.
  auto transformation_invalid_2 = TransformationReplaceCopyObjectWithStoreLoad(
      26, 30, SpvStorageClassFunction, 9);
  ASSERT_FALSE(transformation_invalid_2.IsApplicable(context.get(),
                                                     transformation_context));

  // Invalid: copy_object_result_id=40 is of type pointer.
  auto transformation_invalid_3 = TransformationReplaceCopyObjectWithStoreLoad(
      40, 30, SpvStorageClassFunction, 9);
  ASSERT_FALSE(transformation_invalid_3.IsApplicable(context.get(),
                                                     transformation_context));

  // Invalid: Pointer type instruction in this storage class pointing to the
  // value type is not defined.
  auto transformation_invalid_4 = TransformationReplaceCopyObjectWithStoreLoad(
      40, 30, SpvStorageClassPrivate, 9);
  ASSERT_FALSE(transformation_invalid_4.IsApplicable(context.get(),
                                                     transformation_context));

  // Invalid: initializer_id=15 is invalid.
  auto transformation_invalid_5 = TransformationReplaceCopyObjectWithStoreLoad(
      27, 30, SpvStorageClassPrivate, 15);
  ASSERT_FALSE(transformation_invalid_5.IsApplicable(context.get(),
                                                     transformation_context));

  // Invalid: SpvStorageClassUniform is not applicable to the transformation.
  auto transformation_invalid_6 = TransformationReplaceCopyObjectWithStoreLoad(
      27, 30, SpvStorageClassUniform, 9);
  ASSERT_FALSE(transformation_invalid_6.IsApplicable(context.get(),
                                                     transformation_context));

  auto transformation_valid_1 = TransformationReplaceCopyObjectWithStoreLoad(
      27, 30, SpvStorageClassFunction, 9);
  ASSERT_TRUE(transformation_valid_1.IsApplicable(context.get(),
                                                  transformation_context));
  transformation_valid_1.Apply(context.get(), &transformation_context);
  ASSERT_TRUE(IsValid(env, context.get()));

  auto transformation_valid_2 = TransformationReplaceCopyObjectWithStoreLoad(
      28, 32, SpvStorageClassPrivate, 15);
  ASSERT_TRUE(transformation_valid_2.IsApplicable(context.get(),
                                                  transformation_context));
  transformation_valid_2.Apply(context.get(), &transformation_context);
  ASSERT_TRUE(IsValid(env, context.get()));

  std::string after_transformation = R"(
               OpCapability Shader
          %1 = OpExtInstImport "GLSL.std.450"
               OpMemoryModel Logical GLSL450
               OpEntryPoint Fragment %4 "main" %23 %32
               OpExecutionMode %4 OriginUpperLeft
               OpSource ESSL 310
               OpName %4 "main"
               OpName %8 "a"
               OpName %10 "b"
               OpName %14 "c"
               OpName %16 "d"
               OpName %18 "e"
               OpName %23 "f"
          %2 = OpTypeVoid
          %3 = OpTypeFunction %2
          %6 = OpTypeInt 32 1
          %7 = OpTypePointer Function %6
          %9 = OpConstant %6 2
         %11 = OpConstant %6 3
         %12 = OpTypeFloat 32
         %13 = OpTypePointer Function %12
         %15 = OpConstant %12 2
         %17 = OpConstant %12 3
         %22 = OpTypePointer Private %12
         %23 = OpVariable %22 Private
         %32 = OpVariable %22 Private %15
          %4 = OpFunction %2 None %3
          %5 = OpLabel
         %30 = OpVariable %7 Function %9
          %8 = OpVariable %7 Function
         %10 = OpVariable %7 Function
         %14 = OpVariable %13 Function
         %16 = OpVariable %13 Function
         %18 = OpVariable %7 Function
               OpStore %8 %9
               OpStore %10 %11
               OpStore %14 %15
               OpStore %16 %17
         %19 = OpLoad %6 %8
         %20 = OpLoad %6 %10
         %21 = OpIAdd %6 %19 %20
               OpStore %18 %21
         %24 = OpLoad %12 %14
         %25 = OpLoad %12 %16
         %26 = OpFMul %12 %24 %25
               OpStore %23 %26
               OpStore %30 %21
         %27 = OpLoad %6 %30
               OpStore %32 %26
         %28 = OpLoad %12 %32
         %40 = OpCopyObject %13 %14
               OpReturn
               OpFunctionEnd
  )";
  ASSERT_TRUE(IsEqual(env, after_transformation, context.get()));
}

}  // namespace
}  // namespace fuzz
}  // namespace spvtools
