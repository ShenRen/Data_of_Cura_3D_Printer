'''OpenGL extension ARB.texture_compression_rgtc

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_texture_compression_rgtc'
_DEPRECATED = False
GL_COMPRESSED_RED_RGTC1 = constant.Constant( 'GL_COMPRESSED_RED_RGTC1', 0x8DBB )
GL_COMPRESSED_SIGNED_RED_RGTC1 = constant.Constant( 'GL_COMPRESSED_SIGNED_RED_RGTC1', 0x8DBC )
GL_COMPRESSED_RG_RGTC2 = constant.Constant( 'GL_COMPRESSED_RG_RGTC2', 0x8DBD )
GL_COMPRESSED_SIGNED_RG_RGTC2 = constant.Constant( 'GL_COMPRESSED_SIGNED_RG_RGTC2', 0x8DBE )


def glInitTextureCompressionRgtcARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
