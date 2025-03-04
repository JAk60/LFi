# File: lf_applier.pyx

# cython: language_level=3
# cython: boundscheck=False
# cython: wraparound=False
# cython: cdivision=True

import enum
import numpy as np
cimport numpy as np
from tqdm import tqdm
from itertools import chain
from typing import DefaultDict, Dict, List, Set, NamedTuple, Tuple, Union

from ..lf_set import LFSet
from ..utils import check_unique_names
from ..lf import ABSTAIN, LabelingFunction
from ..data_types import DataPoint, DataPoints

# Define C types for Cython
ctypedef object DataPoint_t

class ApplierMetadata(NamedTuple):
    """Metadata about Applier call."""
    # Map from LF name to number of faults in apply call
    faults: Dict[str, int]

cdef class _FunctionCaller:
    cdef public bint fault_tolerant
    cdef public dict fault_counts
    
    def __init__(self, bint fault_tolerant):
        self.fault_tolerant = fault_tolerant
        self.fault_counts = {}
    
    def __call__(self, f, x):
        if not self.fault_tolerant:
            return f(x)
        try:
            return f(x)
        except Exception:
            if f.name not in self.fault_counts:
                self.fault_counts[f.name] = 1
            else:
                self.fault_counts[f.name] += 1
            return -1

cdef class BaseLFApplier:
    """Base class for LF applier objects."""
    cdef list _lfs
    cdef list _lf_names
    cdef bint _use_recarray
    
    def __init__(self, lf_set):  # Use a generic Python object instead of LFSet type
        self._lfs = lf_set.get_lfs()
        self._lf_names = [lf.name for lf in lf_set.get_lfs()]
        self._use_recarray = False
        check_unique_names(self._lf_names)
    
    cpdef _numpy_from_row_data(self, list labels):
        cdef int len_labels = len(labels)
        cdef int len_lfs = len(self._lfs)
        cdef int i, n
        
        # Create numpy arrays
        L = np.empty((len_labels, len_lfs), dtype=object)
        L.fill(ABSTAIN)
        S = np.full((len_labels, len_lfs), None)
        
        cdef list row_list = []
        cdef list col_list = []
        cdef list enm_list = []
        cdef list conf_list = []
        
        # Fast collection of data from labels
        if any(map(len, labels)):
            for label_list in labels:
                for tup in label_list:
                    row_list.append(tup[0])
                    col_list.append(tup[1])
                    enm_list.append(tup[2])
                    conf_list.append(tup[3])
            
            # Optimize bulk assignment
            n = len(row_list)
            for i in range(n):
                L[row_list[i], col_list[i]] = enm_list[i]
                S[row_list[i], col_list[i]] = conf_list[i]
        
        if self._use_recarray:
            # This branch is not used in the original code
            shape = L.shape
            n_rows = shape[0]  # Extract scalar value
            dtype = [(name, np.int64) for name in self._lf_names]
            recarray = np.recarray(n_rows, dtype=dtype)
            for idx, name in enumerate(self._lf_names):
                recarray[name] = L[:, idx]
            return recarray
        else:
            return L, S
    
    def __repr__(self):
        return f"{type(self).__name__}, LFs: {self._lf_names}"

cpdef list apply_lfs_to_data_point(
    x, int index, list lfs, _FunctionCaller f_caller
):
    """Apply labeling functions to a single data point."""
    cdef list labels = []
    cdef int j
    cdef object lf, y, z
    
    for j in range(len(lfs)):
        lf = lfs[j]
        y, z = f_caller(lf, x)
        
        if y == ABSTAIN and z is None:
            continue
        
        if y == ABSTAIN and z is not None:
            labels.append((index, j, y, z))
            continue
        
        # Check if y has .value attribute (like an enum)
        if hasattr(y, 'value'):
            labels.append((index, j, y.value, z))
        else:
            labels.append((index, j, y, z))
    
    return labels

cdef class LFApplier(BaseLFApplier):
    """LF applier for a list of data points or a NumPy array."""
    
    def apply(
        self,
        data_points,
        bint progress_bar=True,
        bint fault_tolerant=False,
        bint return_meta=False,
    ):
        cdef list labels = []
        cdef _FunctionCaller f_caller = _FunctionCaller(fault_tolerant)
        cdef int i
        cdef int data_len = len(data_points)
        cdef object x
        
        if progress_bar:
            with tqdm(total=data_len) as pbar:
                for i in range(data_len):
                    x = data_points[i]
                    labels.append(apply_lfs_to_data_point(x, i, self._lfs, f_caller))
                    pbar.update()
        else:
            for i in range(data_len):
                x = data_points[i]
                labels.append(apply_lfs_to_data_point(x, i, self._lfs, f_caller))
        
        L, S = self._numpy_from_row_data(labels)
        
        if return_meta:
            return L, ApplierMetadata(dict(f_caller.fault_counts))
        return L, S