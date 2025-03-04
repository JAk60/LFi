from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension(
        "utils",  # The name of the extension module
        ["utils.pyx"],  # The Cython source file
        include_dirs=[np.get_include()],  # Include directories for NumPy
    )
]

setup(
    ext_modules=cythonize(extensions),
)
