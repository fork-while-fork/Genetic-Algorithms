from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("GAeval", ["GAeval.pyx"])]

setup(
  name = 'Genetic Algorithm Evaluation app',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
