# Copyright (c) 2013 The ANGLE Project Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
    'variables':
    {
        # These file lists are shared with the GN build.
        'libangle_common_sources':
        [
            'common/angleutils.cpp',
            'common/angleutils.h',
            'common/blocklayout.cpp',
            'common/blocklayout.h',
            'common/debug.cpp',
            'common/debug.h',
            'common/event_tracer.cpp',
            'common/event_tracer.h',
            'common/mathutil.cpp',
            'common/mathutil.h',
            'common/platform.h',
            'common/tls.cpp',
            'common/tls.h',
            'common/utilities.cpp',
            'common/utilities.h',
            'common/version.h',
        ],
        'libangle_includes':
        [
            '../include/EGL/egl.h',
            '../include/EGL/eglext.h',
            '../include/EGL/eglplatform.h',
            '../include/GLES2/gl2.h',
            '../include/GLES2/gl2ext.h',
            '../include/GLES2/gl2platform.h',
            '../include/GLES3/gl3.h',
            '../include/GLES3/gl3ext.h',
            '../include/GLES3/gl3platform.h',
            '../include/GLSLANG/ShaderLang.h',
            '../include/GLSLANG/ShaderVars.h',
            '../include/KHR/khrplatform.h',
            '../include/angle_gl.h',
        ],
        'libangle_sources':
        [
            'libANGLE/AttributeMap.cpp',
            'libANGLE/AttributeMap.h',
            'libANGLE/BinaryStream.h',
            'libANGLE/Buffer.cpp',
            'libANGLE/Buffer.h',
            'libANGLE/Caps.cpp',
            'libANGLE/Caps.h',
            'libANGLE/Config.cpp',
            'libANGLE/Config.h',
            'libANGLE/Constants.h',
            'libANGLE/Context.cpp',
            'libANGLE/Context.h',
            'libANGLE/Data.cpp',
            'libANGLE/Data.h',
            'libANGLE/Display.cpp',
            'libANGLE/Display.h',
            'libANGLE/Error.cpp',
            'libANGLE/Error.h',
            'libANGLE/Fence.cpp',
            'libANGLE/Fence.h',
            'libANGLE/Float16ToFloat32.cpp',
            'libANGLE/Framebuffer.cpp',
            'libANGLE/Framebuffer.h',
            'libANGLE/FramebufferAttachment.cpp',
            'libANGLE/FramebufferAttachment.h',
            'libANGLE/HandleAllocator.cpp',
            'libANGLE/HandleAllocator.h',
            'libANGLE/ImageIndex.h',
            'libANGLE/ImageIndex.cpp',
            'libANGLE/Program.cpp',
            'libANGLE/Program.h',
            'libANGLE/ProgramBinary.cpp',
            'libANGLE/ProgramBinary.h',
            'libANGLE/Query.cpp',
            'libANGLE/Query.h',
            'libANGLE/RefCountObject.cpp',
            'libANGLE/RefCountObject.h',
            'libANGLE/Renderbuffer.cpp',
            'libANGLE/Renderbuffer.h',
            'libANGLE/ResourceManager.cpp',
            'libANGLE/ResourceManager.h',
            'libANGLE/Sampler.cpp',
            'libANGLE/Sampler.h',
            'libANGLE/Shader.cpp',
            'libANGLE/Shader.h',
            'libANGLE/State.cpp',
            'libANGLE/State.h',
            'libANGLE/Surface.cpp',
            'libANGLE/Surface.h',
            'libANGLE/Texture.cpp',
            'libANGLE/Texture.h',
            'libANGLE/TransformFeedback.cpp',
            'libANGLE/TransformFeedback.h',
            'libANGLE/Uniform.cpp',
            'libANGLE/Uniform.h',
            'libANGLE/VertexArray.cpp',
            'libANGLE/VertexArray.h',
            'libANGLE/VertexAttribute.cpp',
            'libANGLE/VertexAttribute.h',
            'libANGLE/angletypes.cpp',
            'libANGLE/angletypes.h',
            'libANGLE/export.h',
            'libANGLE/features.h',
            'libANGLE/formatutils.cpp',
            'libANGLE/formatutils.h',
            'libANGLE/queryconversions.cpp',
            'libANGLE/queryconversions.h',
            'libANGLE/renderer/BufferImpl.h',
            'libANGLE/renderer/FenceImpl.h',
            'libANGLE/renderer/FramebufferImpl.h',
            'libANGLE/renderer/Image.cpp',
            'libANGLE/renderer/Image.h',
            'libANGLE/renderer/IndexRangeCache.cpp',
            'libANGLE/renderer/IndexRangeCache.h',
            'libANGLE/renderer/ProgramImpl.cpp',
            'libANGLE/renderer/ProgramImpl.h',
            'libANGLE/renderer/QueryImpl.h',
            'libANGLE/renderer/RenderbufferImpl.h',
            'libANGLE/renderer/RenderbufferImpl.cpp',
            'libANGLE/renderer/Renderer.cpp',
            'libANGLE/renderer/Renderer.h',
            'libANGLE/renderer/RenderTarget.h',
            'libANGLE/renderer/RenderTarget.cpp',
            'libANGLE/renderer/ShaderExecutable.h',
            'libANGLE/renderer/ShaderImpl.h',
            'libANGLE/renderer/SurfaceImpl.cpp',
            'libANGLE/renderer/SurfaceImpl.h',
            'libANGLE/renderer/SwapChain.h',
            'libANGLE/renderer/TextureImpl.h',
            'libANGLE/renderer/TransformFeedbackImpl.h',
            'libANGLE/renderer/VertexArrayImpl.h',
            'libANGLE/renderer/Workarounds.h',
            'libANGLE/renderer/copyimage.cpp',
            'libANGLE/renderer/copyimage.h',
            'libANGLE/renderer/copyimage.inl',
            'libANGLE/renderer/copyvertex.h',
            'libANGLE/renderer/copyvertex.inl',
            'libANGLE/renderer/generatemip.h',
            'libANGLE/renderer/generatemip.inl',
            'libANGLE/renderer/imageformats.h',
            'libANGLE/renderer/loadimage.cpp',
            'libANGLE/renderer/loadimage.h',
            'libANGLE/renderer/loadimage.inl',
            'libANGLE/renderer/loadimageSSE2.cpp',
            'libANGLE/renderer/vertexconversion.h',
            'libANGLE/validationES.cpp',
            'libANGLE/validationES.h',
            'libANGLE/validationES2.cpp',
            'libANGLE/validationES2.h',
            'libANGLE/validationES3.cpp',
            'libANGLE/validationES3.h',
            'third_party/murmurhash/MurmurHash3.cpp',
            'third_party/murmurhash/MurmurHash3.h',
            'third_party/systeminfo/SystemInfo.cpp',
            'third_party/systeminfo/SystemInfo.h',
        ],
        'libangle_d3d_shared_sources':
        [
            'libANGLE/renderer/d3d/BufferD3D.cpp',
            'libANGLE/renderer/d3d/BufferD3D.h',
            'libANGLE/renderer/d3d/DynamicHLSL.cpp',
            'libANGLE/renderer/d3d/DynamicHLSL.h',
            'libANGLE/renderer/d3d/FramebufferD3D.cpp',
            'libANGLE/renderer/d3d/FramebufferD3D.h',
            'libANGLE/renderer/d3d/HLSLCompiler.cpp',
            'libANGLE/renderer/d3d/HLSLCompiler.h',
            'libANGLE/renderer/d3d/ImageD3D.cpp',
            'libANGLE/renderer/d3d/ImageD3D.h',
            'libANGLE/renderer/d3d/IndexBuffer.cpp',
            'libANGLE/renderer/d3d/IndexBuffer.h',
            'libANGLE/renderer/d3d/IndexDataManager.cpp',
            'libANGLE/renderer/d3d/IndexDataManager.h',
            'libANGLE/renderer/d3d/MemoryBuffer.cpp',
            'libANGLE/renderer/d3d/MemoryBuffer.h',
            'libANGLE/renderer/d3d/ProgramD3D.cpp',
            'libANGLE/renderer/d3d/ProgramD3D.h',
            'libANGLE/renderer/d3d/RenderbufferD3D.cpp',
            'libANGLE/renderer/d3d/RenderbufferD3D.h',
            'libANGLE/renderer/d3d/RendererD3D.cpp',
            'libANGLE/renderer/d3d/RendererD3D.h',
            'libANGLE/renderer/d3d/ShaderD3D.cpp',
            'libANGLE/renderer/d3d/ShaderD3D.h',
            'libANGLE/renderer/d3d/SurfaceD3D.cpp',
            'libANGLE/renderer/d3d/SurfaceD3D.h',
            'libANGLE/renderer/d3d/TextureD3D.cpp',
            'libANGLE/renderer/d3d/TextureD3D.h',
            'libANGLE/renderer/d3d/TextureStorage.cpp',
            'libANGLE/renderer/d3d/TextureStorage.h',
            'libANGLE/renderer/d3d/TransformFeedbackD3D.cpp',
            'libANGLE/renderer/d3d/TransformFeedbackD3D.h',
            'libANGLE/renderer/d3d/VertexBuffer.cpp',
            'libANGLE/renderer/d3d/VertexBuffer.h',
            'libANGLE/renderer/d3d/VertexDataManager.cpp',
            'libANGLE/renderer/d3d/VertexDataManager.h',
        ],
        'libangle_d3d9_sources':
        [
            'libANGLE/renderer/d3d/d3d9/Blit9.cpp',
            'libANGLE/renderer/d3d/d3d9/Blit9.h',
            'libANGLE/renderer/d3d/d3d9/Buffer9.cpp',
            'libANGLE/renderer/d3d/d3d9/Buffer9.h',
            'libANGLE/renderer/d3d/d3d9/Fence9.cpp',
            'libANGLE/renderer/d3d/d3d9/Fence9.h',
            'libANGLE/renderer/d3d/d3d9/formatutils9.cpp',
            'libANGLE/renderer/d3d/d3d9/formatutils9.h',
            'libANGLE/renderer/d3d/d3d9/Framebuffer9.cpp',
            'libANGLE/renderer/d3d/d3d9/Framebuffer9.h',
            'libANGLE/renderer/d3d/d3d9/Image9.cpp',
            'libANGLE/renderer/d3d/d3d9/Image9.h',
            'libANGLE/renderer/d3d/d3d9/IndexBuffer9.cpp',
            'libANGLE/renderer/d3d/d3d9/IndexBuffer9.h',
            'libANGLE/renderer/d3d/d3d9/Query9.cpp',
            'libANGLE/renderer/d3d/d3d9/Query9.h',
            'libANGLE/renderer/d3d/d3d9/Renderer9.cpp',
            'libANGLE/renderer/d3d/d3d9/Renderer9.h',
            'libANGLE/renderer/d3d/d3d9/renderer9_utils.cpp',
            'libANGLE/renderer/d3d/d3d9/renderer9_utils.h',
            'libANGLE/renderer/d3d/d3d9/RenderTarget9.cpp',
            'libANGLE/renderer/d3d/d3d9/RenderTarget9.h',
            'libANGLE/renderer/d3d/d3d9/ShaderCache.h',
            'libANGLE/renderer/d3d/d3d9/ShaderExecutable9.cpp',
            'libANGLE/renderer/d3d/d3d9/ShaderExecutable9.h',
            'libANGLE/renderer/d3d/d3d9/shaders/compiled/componentmaskps.h',
            'libANGLE/renderer/d3d/d3d9/shaders/compiled/flipyvs.h',
            'libANGLE/renderer/d3d/d3d9/shaders/compiled/luminanceps.h',
            'libANGLE/renderer/d3d/d3d9/shaders/compiled/passthroughps.h',
            'libANGLE/renderer/d3d/d3d9/shaders/compiled/standardvs.h',
            'libANGLE/renderer/d3d/d3d9/SwapChain9.cpp',
            'libANGLE/renderer/d3d/d3d9/SwapChain9.h',
            'libANGLE/renderer/d3d/d3d9/TextureStorage9.cpp',
            'libANGLE/renderer/d3d/d3d9/TextureStorage9.h',
            'libANGLE/renderer/d3d/d3d9/VertexArray9.h',
            'libANGLE/renderer/d3d/d3d9/VertexBuffer9.cpp',
            'libANGLE/renderer/d3d/d3d9/VertexBuffer9.h',
            'libANGLE/renderer/d3d/d3d9/VertexDeclarationCache.cpp',
            'libANGLE/renderer/d3d/d3d9/VertexDeclarationCache.h',
        ],
        'libangle_d3d11_sources':
        [
            'libANGLE/renderer/d3d/d3d11/Blit11.cpp',
            'libANGLE/renderer/d3d/d3d11/Blit11.h',
            'libANGLE/renderer/d3d/d3d11/Buffer11.cpp',
            'libANGLE/renderer/d3d/d3d11/Buffer11.h',
            'libANGLE/renderer/d3d/d3d11/Clear11.cpp',
            'libANGLE/renderer/d3d/d3d11/Clear11.h',
            'libANGLE/renderer/d3d/d3d11/Fence11.cpp',
            'libANGLE/renderer/d3d/d3d11/Fence11.h',
            'libANGLE/renderer/d3d/d3d11/formatutils11.cpp',
            'libANGLE/renderer/d3d/d3d11/formatutils11.h',
            'libANGLE/renderer/d3d/d3d11/Framebuffer11.cpp',
            'libANGLE/renderer/d3d/d3d11/Framebuffer11.h',
            'libANGLE/renderer/d3d/d3d11/Image11.cpp',
            'libANGLE/renderer/d3d/d3d11/Image11.h',
            'libANGLE/renderer/d3d/d3d11/IndexBuffer11.cpp',
            'libANGLE/renderer/d3d/d3d11/IndexBuffer11.h',
            'libANGLE/renderer/d3d/d3d11/InputLayoutCache.cpp',
            'libANGLE/renderer/d3d/d3d11/InputLayoutCache.h',
            'libANGLE/renderer/d3d/d3d11/NativeWindow.h',
            'libANGLE/renderer/d3d/d3d11/PixelTransfer11.cpp',
            'libANGLE/renderer/d3d/d3d11/PixelTransfer11.h',
            'libANGLE/renderer/d3d/d3d11/Query11.cpp',
            'libANGLE/renderer/d3d/d3d11/Query11.h',
            'libANGLE/renderer/d3d/d3d11/Renderer11.cpp',
            'libANGLE/renderer/d3d/d3d11/Renderer11.h',
            'libANGLE/renderer/d3d/d3d11/renderer11_utils.cpp',
            'libANGLE/renderer/d3d/d3d11/renderer11_utils.h',
            'libANGLE/renderer/d3d/d3d11/RenderStateCache.cpp',
            'libANGLE/renderer/d3d/d3d11/RenderStateCache.h',
            'libANGLE/renderer/d3d/d3d11/RenderTarget11.cpp',
            'libANGLE/renderer/d3d/d3d11/RenderTarget11.h',
            'libANGLE/renderer/d3d/d3d11/ShaderExecutable11.cpp',
            'libANGLE/renderer/d3d/d3d11/ShaderExecutable11.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/buffertotexture11_gs.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/buffertotexture11_ps_4f.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/buffertotexture11_ps_4i.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/buffertotexture11_ps_4ui.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/buffertotexture11_vs.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/clearfloat11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/clearfloat11vs.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/clearsint11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/clearsint11vs.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/clearuint11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/clearuint11vs.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthrough2d11vs.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthrough3d11gs.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthrough3d11vs.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughdepth2d11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughlum2d11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughlum3d11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughlumalpha2d11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughlumalpha3d11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughr2d11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughr2di11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughr2dui11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughr3d11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughr3di11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughr3dui11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughrg2d11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughrg2di11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughrg2dui11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughrg3d11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughrg3di11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughrg3dui11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughrgb2d11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughrgb2di11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughrgb2dui11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughrgb3d11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughrgb3di11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughrgb3dui11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughrgba2d11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughrgba2di11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughrgba2dui11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughrgba3d11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughrgba3di11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/passthroughrgba3dui11ps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/swizzlef2darrayps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/swizzlef2dps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/swizzlef3dps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/swizzlei2darrayps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/swizzlei2dps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/swizzlei3dps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/swizzleui2darrayps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/swizzleui2dps.h',
            'libANGLE/renderer/d3d/d3d11/shaders/compiled/swizzleui3dps.h',
            'libANGLE/renderer/d3d/d3d11/SwapChain11.cpp',
            'libANGLE/renderer/d3d/d3d11/SwapChain11.h',
            'libANGLE/renderer/d3d/d3d11/TextureStorage11.cpp',
            'libANGLE/renderer/d3d/d3d11/TextureStorage11.h',
            'libANGLE/renderer/d3d/d3d11/Trim11.cpp',
            'libANGLE/renderer/d3d/d3d11/Trim11.h',
            'libANGLE/renderer/d3d/d3d11/VertexArray11.h',
            'libANGLE/renderer/d3d/d3d11/VertexBuffer11.cpp',
            'libANGLE/renderer/d3d/d3d11/VertexBuffer11.h',
        ],
        'libangle_d3d11_win32_sources':
        [
            'libANGLE/renderer/d3d/d3d11/win32/NativeWindow.cpp',
        ],
        'libangle_d3d11_winrt_sources':
        [
            'libANGLE/renderer/d3d/d3d11/winrt/SwapChainPanelNativeWindow.cpp',
            'libANGLE/renderer/d3d/d3d11/winrt/SwapChainPanelNativeWindow.h',
            'libANGLE/renderer/d3d/d3d11/winrt/CoreWindowNativeWindow.cpp',
            'libANGLE/renderer/d3d/d3d11/winrt/CoreWindowNativeWindow.h',
            'libANGLE/renderer/d3d/d3d11/winrt/InspectableNativeWindow.cpp',
            'libANGLE/renderer/d3d/d3d11/winrt/InspectableNativeWindow.h',
        ],
        'libangle_static%': 1,
    },
    # Everything below this is duplicated in the GN build. If you change
    # anything also change angle/BUILD.gn
    'targets':
    [
        {
            'target_name': 'libANGLE',
            'dependencies': [ 'translator', 'commit_id', ],
            'includes': [ '../build/common_defines.gypi', ],
            'include_dirs':
            [
                '.',
                '../include',
                'libANGLE',
            ],
            'sources':
            [
                '<@(libangle_sources)',
                '<@(libangle_common_sources)',
                '<@(libangle_includes)',
            ],
            'defines':
            [
                'GL_APICALL=',
                'GL_GLEXT_PROTOTYPES=',
                'EGLAPI=',
                'ANGLE_PRELOADED_D3DCOMPILER_MODULE_NAMES={ "d3dcompiler_47.dll", "d3dcompiler_46.dll", "d3dcompiler_43.dll" }',
                'LIBANGLE_IMPLEMENTATION',
            ],
            'direct_dependent_settings':
            {
                'include_dirs':
                [
                    '.',
                    '../include',
                ],
                'defines':
                [
                    'GL_APICALL=',
                    'GL_GLEXT_PROTOTYPES=',
                    'EGLAPI=',
                    'ANGLE_PRELOADED_D3DCOMPILER_MODULE_NAMES={ "d3dcompiler_47.dll", "d3dcompiler_46.dll", "d3dcompiler_43.dll" }',
                ],
                'conditions':
                [
                    ['angle_enable_d3d9==1',
                    {
                        'defines':
                        [
                            'ANGLE_ENABLE_D3D9',
                        ],
                    }],
                    ['angle_enable_d3d11==1',
                    {
                        'defines':
                        [
                            'ANGLE_ENABLE_D3D11',
                        ],
                    }],
                ],
            },
            'conditions':
            [
                ['libangle_static==1',
                {
                    'defines':
                    [
                        'LIBANGLE_STATIC',
                    ],
                    'direct_dependent_settings':
                    {
                        'defines':
                        [
                            'LIBANGLE_STATIC',
                        ],
                    },
                    'type': 'static_library',
                },
                { # 'libangle_static==0'
                    'type': 'shared_library',
                }],
                ['angle_enable_d3d9==1 or angle_enable_d3d11==1',
                {
                    'sources':
                    [
                        '<@(libangle_d3d_shared_sources)',
                    ],
                }],
                ['angle_enable_d3d9==1',
                {
                    'sources':
                    [
                        '<@(libangle_d3d9_sources)',
                    ],
                    'defines':
                    [
                        'ANGLE_ENABLE_D3D9',
                    ],
                    'link_settings':
                    {
                        'msvs_settings':
                        {
                            'VCLinkerTool':
                            {
                                'AdditionalDependencies':
                                [
                                    'd3d9.lib',
                                ]
                            }
                        },
                    },
                }],
                ['angle_enable_d3d11==1',
                {
                    'sources':
                    [
                        '<@(libangle_d3d11_sources)',
                    ],
                    'defines':
                    [
                        'ANGLE_ENABLE_D3D11',
                    ],
                    'link_settings':
                    {
                        'msvs_settings':
                        {
                            'VCLinkerTool':
                            {
                                'conditions':
                                [
                                    ['angle_build_winrt==0',
                                    {
                                        'AdditionalDependencies':
                                        [
                                            'dxguid.lib',
                                        ],
                                    }],
                                    ['angle_build_winrt==1',
                                    {
                                        'AdditionalDependencies':
                                        [
                                            'dxguid.lib',
                                            'd3d11.lib',
                                            'd3dcompiler.lib',
                                        ],
                                    }],
                                ],
                            }
                        },
                    },
                    'conditions':
                    [
                        ['angle_build_winrt==1',
                        {
                            'sources':
                            [
                                '<@(libangle_d3d11_winrt_sources)',
                            ],
                        },
                        { # win32
                            'sources':
                            [
                                '<@(libangle_d3d11_win32_sources)',
                            ],
                        }],
                    ],
                }],
                ['angle_build_winrt==0 and OS=="win"',
                {
                    'dependencies':
                    [
                        'copy_compiler_dll'
                    ],
                }],
                ['angle_build_winrt==1',
                {
                    'defines':
                    [
                        'NTDDI_VERSION=NTDDI_WINBLUE',
                    ],
                    'msvs_enable_winrt' : '1',
                    'msvs_requires_importlibrary' : 'true',
                    'msvs_settings':
                    {
                        'VCLinkerTool':
                        {
                            'EnableCOMDATFolding': '1',
                            'OptimizeReferences': '1',
                        }
                    },
                }],
                ['angle_build_winphone==1',
                {
                    'msvs_enable_winphone' : '1',
                }],
            ],
            'configurations':
            {
                'Debug_Base':
                {
                    'defines':
                    [
                        'ANGLE_ENABLE_DEBUG_ANNOTATIONS',
                        'ANGLE_GENERATE_SHADER_DEBUG_INFO'
                    ],
                    'msvs_settings':
                    {
                        'VCLinkerTool':
                        {
                            'AdditionalDependencies':
                            [
                                'd3d9.lib',
                            ]
                        }
                    },
                },
            },
        },
        {
            'target_name': 'libGLESv2',
            'type': 'shared_library',
            'dependencies': [ 'libANGLE' ],
            'includes': [ '../build/common_defines.gypi', ],
            'sources':
            [
                'common/angleutils.cpp',
                'common/angleutils.h',
                'common/debug.cpp',
                'common/debug.h',
                'common/event_tracer.cpp',
                'common/event_tracer.h',
                'common/tls.cpp',
                'common/tls.h',
                'libGLESv2/libGLESv2.cpp',
                'libGLESv2/libGLESv2.def',
                'libGLESv2/libGLESv2.rc',
                'libGLESv2/main.cpp',
                'libGLESv2/main.h',
                'libGLESv2/resource.h',
            ],
            'defines':
            [
                'LIBGLESV2_IMPLEMENTATION',
            ],
            'conditions':
            [
                ['angle_build_winrt==1',
                {
                    'msvs_enable_winrt' : '1',
                    'msvs_requires_importlibrary' : 'true',
                    'msvs_settings':
                    {
                        'VCLinkerTool':
                        {
                            'EnableCOMDATFolding': '1',
                            'OptimizeReferences': '1',
                        }
                    },
                }],
                ['angle_build_winphone==1',
                {
                    'msvs_enable_winphone' : '1',
                }],
            ],
        },
    ],
}
