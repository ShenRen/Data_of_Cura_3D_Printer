'''OpenGL extension EXT.stencil_clear_tag

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_stencil_clear_tag'
_DEPRECATED = False
GL_STENCIL_TAG_BITS_EXT = constant.Constant( 'GL_STENCIL_TAG_BITS_EXT', 0x88F2 )
GL_STENCIL_CLEAR_TAG_VALUE_EXT = constant.Constant( 'GL_STENCIL_CLEAR_TAG_VALUE_EXT', 0x88F3 )
glStencilClearTagEXT = platform.createExtensionFunction( 
'glStencilClearTagEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLsizei,constants.GLuint,),
doc='glStencilClearTagEXT(GLsizei(stencilTagBits), GLuint(stencilClearTag)) -> None',
argNames=('stencilTagBits','stencilClearTag',),
deprecated=_DEPRECATED,
)


def glInitStencilClearTagEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )