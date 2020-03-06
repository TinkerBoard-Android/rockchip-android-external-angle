// GENERATED FILE - DO NOT EDIT.
// Generated by generate_entry_points.py using data from gl.xml and wgl.xml.
//
// Copyright 2020 The ANGLE Project Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.
//
// validationGL41_autogen.h:
//   Validation functions for the OpenGL 4.1 entry points.

#ifndef LIBANGLE_VALIDATION_GL41_AUTOGEN_H_
#define LIBANGLE_VALIDATION_GL41_AUTOGEN_H_

#include "common/PackedEnums.h"

namespace gl
{
class Context;

bool ValidateDepthRangeArrayv(const Context *context,
                              GLuint first,
                              GLsizei count,
                              const GLdouble *v);
bool ValidateDepthRangeIndexed(const Context *context, GLuint index, GLdouble n, GLdouble f);
bool ValidateGetDoublei_v(const Context *context,
                          GLenum target,
                          GLuint index,
                          const GLdouble *data);
bool ValidateGetFloati_v(const Context *context, GLenum target, GLuint index, const GLfloat *data);
bool ValidateGetVertexAttribLdv(const Context *context,
                                GLuint index,
                                GLenum pname,
                                const GLdouble *params);
bool ValidateProgramUniform1d(const Context *context,
                              ShaderProgramID programPacked,
                              UniformLocation locationPacked,
                              GLdouble v0);
bool ValidateProgramUniform1dv(const Context *context,
                               ShaderProgramID programPacked,
                               UniformLocation locationPacked,
                               GLsizei count,
                               const GLdouble *value);
bool ValidateProgramUniform2d(const Context *context,
                              ShaderProgramID programPacked,
                              UniformLocation locationPacked,
                              GLdouble v0,
                              GLdouble v1);
bool ValidateProgramUniform2dv(const Context *context,
                               ShaderProgramID programPacked,
                               UniformLocation locationPacked,
                               GLsizei count,
                               const GLdouble *value);
bool ValidateProgramUniform3d(const Context *context,
                              ShaderProgramID programPacked,
                              UniformLocation locationPacked,
                              GLdouble v0,
                              GLdouble v1,
                              GLdouble v2);
bool ValidateProgramUniform3dv(const Context *context,
                               ShaderProgramID programPacked,
                               UniformLocation locationPacked,
                               GLsizei count,
                               const GLdouble *value);
bool ValidateProgramUniform4d(const Context *context,
                              ShaderProgramID programPacked,
                              UniformLocation locationPacked,
                              GLdouble v0,
                              GLdouble v1,
                              GLdouble v2,
                              GLdouble v3);
bool ValidateProgramUniform4dv(const Context *context,
                               ShaderProgramID programPacked,
                               UniformLocation locationPacked,
                               GLsizei count,
                               const GLdouble *value);
bool ValidateProgramUniformMatrix2dv(const Context *context,
                                     ShaderProgramID programPacked,
                                     UniformLocation locationPacked,
                                     GLsizei count,
                                     GLboolean transpose,
                                     const GLdouble *value);
bool ValidateProgramUniformMatrix2x3dv(const Context *context,
                                       ShaderProgramID programPacked,
                                       UniformLocation locationPacked,
                                       GLsizei count,
                                       GLboolean transpose,
                                       const GLdouble *value);
bool ValidateProgramUniformMatrix2x4dv(const Context *context,
                                       ShaderProgramID programPacked,
                                       UniformLocation locationPacked,
                                       GLsizei count,
                                       GLboolean transpose,
                                       const GLdouble *value);
bool ValidateProgramUniformMatrix3dv(const Context *context,
                                     ShaderProgramID programPacked,
                                     UniformLocation locationPacked,
                                     GLsizei count,
                                     GLboolean transpose,
                                     const GLdouble *value);
bool ValidateProgramUniformMatrix3x2dv(const Context *context,
                                       ShaderProgramID programPacked,
                                       UniformLocation locationPacked,
                                       GLsizei count,
                                       GLboolean transpose,
                                       const GLdouble *value);
bool ValidateProgramUniformMatrix3x4dv(const Context *context,
                                       ShaderProgramID programPacked,
                                       UniformLocation locationPacked,
                                       GLsizei count,
                                       GLboolean transpose,
                                       const GLdouble *value);
bool ValidateProgramUniformMatrix4dv(const Context *context,
                                     ShaderProgramID programPacked,
                                     UniformLocation locationPacked,
                                     GLsizei count,
                                     GLboolean transpose,
                                     const GLdouble *value);
bool ValidateProgramUniformMatrix4x2dv(const Context *context,
                                       ShaderProgramID programPacked,
                                       UniformLocation locationPacked,
                                       GLsizei count,
                                       GLboolean transpose,
                                       const GLdouble *value);
bool ValidateProgramUniformMatrix4x3dv(const Context *context,
                                       ShaderProgramID programPacked,
                                       UniformLocation locationPacked,
                                       GLsizei count,
                                       GLboolean transpose,
                                       const GLdouble *value);
bool ValidateScissorArrayv(const Context *context, GLuint first, GLsizei count, const GLint *v);
bool ValidateScissorIndexed(const Context *context,
                            GLuint index,
                            GLint left,
                            GLint bottom,
                            GLsizei width,
                            GLsizei height);
bool ValidateScissorIndexedv(const Context *context, GLuint index, const GLint *v);
bool ValidateVertexAttribL1d(const Context *context, GLuint index, GLdouble x);
bool ValidateVertexAttribL1dv(const Context *context, GLuint index, const GLdouble *v);
bool ValidateVertexAttribL2d(const Context *context, GLuint index, GLdouble x, GLdouble y);
bool ValidateVertexAttribL2dv(const Context *context, GLuint index, const GLdouble *v);
bool ValidateVertexAttribL3d(const Context *context,
                             GLuint index,
                             GLdouble x,
                             GLdouble y,
                             GLdouble z);
bool ValidateVertexAttribL3dv(const Context *context, GLuint index, const GLdouble *v);
bool ValidateVertexAttribL4d(const Context *context,
                             GLuint index,
                             GLdouble x,
                             GLdouble y,
                             GLdouble z,
                             GLdouble w);
bool ValidateVertexAttribL4dv(const Context *context, GLuint index, const GLdouble *v);
bool ValidateVertexAttribLPointer(const Context *context,
                                  GLuint index,
                                  GLint size,
                                  GLenum type,
                                  GLsizei stride,
                                  const void *pointer);
bool ValidateViewportArrayv(const Context *context, GLuint first, GLsizei count, const GLfloat *v);
bool ValidateViewportIndexedf(const Context *context,
                              GLuint index,
                              GLfloat x,
                              GLfloat y,
                              GLfloat w,
                              GLfloat h);
bool ValidateViewportIndexedfv(const Context *context, GLuint index, const GLfloat *v);
}  // namespace gl

#endif  // LIBANGLE_VALIDATION_GL41_AUTOGEN_H_
