import numpy as np
cimport numpy as np
from itertools import permutations
import sys
from libc.stdio cimport printf

# Function to compute the matrix permanent (optimized)
cdef double permanent(double[:, :] matrix):  # Type hint for Cython
    cdef int n = matrix.shape[0]
    cdef double result = 0.0
    cdef int i, j
    cdef double prod

    cdef int[:] p_arr = np.zeros(n, dtype=np.intc) # preallocate for permutation
    cdef int[:] indices = np.arange(n, dtype=np.intc) # indices to permute

    for p in permutations(indices):
        for i in range(n):
            p_arr[i] = p[i]
        prod = 1.0
        for i in range(n):
            prod *= matrix[i, p_arr[i]]
        result += prod

    return result


cpdef list process_matrices(double[:, :] importance_matrix,
                           double[:, :] normalized_matrix,
                           int num_matrices=5):
    cdef list permanents = []
    cdef double[:, :] new_matrix
    cdef int i, j
    cdef double perm_result
    cdef double sum_permanents  # For normalization

    for i in range(num_matrices):
        new_matrix = importance_matrix.copy()
        for j in range(10):
            new_matrix[j, j] = normalized_matrix[i, j]

        perm_result = permanent(new_matrix)
        permanents.append(perm_result)

        print(f"Matrix {i} Permanent: {perm_result}")
        sys.stdout.flush()
        printf(b"Processed Matrix %d, Permanent: %f\n", i, perm_result)

    # Normalization: Divide by the sum of permanents
    if permanents:  # Check if the list is not empty
        sum_permanents = sum(permanents)

        if sum_permanents != 0:  # Avoid division by zero
            # Normalize the permanents (in-place modification is more efficient)
            for i in range(len(permanents)):
                permanents[i] /= sum_permanents
        else:
            print("Warning: Sum of permanents is 0. Cannot normalize.")

    return permanents  # Return the normalized list