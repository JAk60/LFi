# from setuptools import setup, find_packages

# setup(
#     name="spear",
#     version="0.1",
#     packages=find_packages(),
# )
from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules=cythonize('ac.pyx'),
    include_dirs=[np.get_include()],
)
