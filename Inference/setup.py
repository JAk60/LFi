from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension(
        "LFapplier",  # The name of the extension module
        ["LFapplier.pyx"],  # The Cython source file
        include_dirs=[np.get_include()],  # Include directories for NumPy
    )
]

setup(
    ext_modules=cythonize(extensions),
)
