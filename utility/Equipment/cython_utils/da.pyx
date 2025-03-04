# Save as utility_functions.pyx
cimport cython
from libc.math cimport pow

# Define a C type for better performance
ctypedef double dtype_t


cpdef dtype_t capacity(dtype_t K, dtype_t L, dtype_t O):
    if O >= K:
        return 1.0
    elif K > O > L:
        return 1.0 - ((K - O) / (K - L) * 0.1)
    elif O == L:
        return 0.9
    elif O < L:
        return 0.9 - ((L - O) / L * 0.9)
    elif O == 0:
        return 0.0
    else:
        return -1.0  # Return a numeric value instead of empty string


cpdef dtype_t capability_response_time(dtype_t K, dtype_t L, dtype_t O):
    """
    K = K column reference
    L = L column reference
    O = O column reference
    """
    if O <= K:
        return 1.0
    elif K < O < L:
        return 1.0 - (O - K) / (L - K) * (1.0 - 0.9)  # Linear interpolation
    elif O == L:
        return 0.9
    elif O > L:
        return 0.9 - (O - L)**2 / ((O - L)**2 + (L - K)**2) * 0.9  # Quadratic decay
    return -1.0  # Default case


cpdef dtype_t reliability(dtype_t K, dtype_t L, dtype_t O):
    cdef dtype_t result
    
    if O >= K:
        return 1.0

    elif O < K and O > L:
        if K != L:
            result = 1.0 - (K - O) / (K - L) * 0.1
        else:
            result = 1.0
        return result

    elif O == L:
        return 0.9

    elif O < L:
        if L != 0:
            result = 0.9 * pow(O / L, 2)
        else:
            result = 0.0
        return result

    elif O == 0:
        return 0.0

    else:
        return -1.0  # Default case as numeric value


cpdef dtype_t operational_availability_util(dtype_t K, dtype_t L, dtype_t O):
    cdef dtype_t result
    
    if O >= K:
        return 1.0

    elif K > O > L:
        if K != L:
            result = 0.9 + 0.1 * pow((O - L) / (K - L), 2)
        else:
            result = 0.9
        return result

    elif O == L:
        return 0.9

    elif O < L:
        if L != 0:
            result = 0.9 * (O / L)
        else:
            result = 0.0
        return result

    else:
        return 0.0


cpdef dtype_t operational_maintainability_util(dtype_t K, dtype_t L, dtype_t O):
    """
    K = DK (reference)
    L = DL (reference)
    O = DO (reference)
    """
    cdef dtype_t result
    
    if O <= K:
        return 1.0
    elif O == L:
        return 0.9
    elif O < L:
        result = 0.9 + 0.1 * pow(1.0 - (O - K) / (L - K), 2)
        return result
    elif O <= 2.0 * K:
        result = 0.9 * pow(1.0 - (O - L) / (2.0 * K - L), 2)
        return result
    else:
        return 0.0


cpdef dtype_t mission_completion_safety_util(dtype_t K, dtype_t L, dtype_t O):
    """
    K = EI (reference)
    L = EJ (reference)
    O = EM (reference)
    """
    if O >= K:
        return 1.0
    elif O == L:
        return 0.9
    elif O > K:
        return 1.0 - ((O - K) / (L - K) * 0.1)
    elif O > 0:
        return 0.9 * (O / L)
    else:
        return 0.0


cpdef dtype_t human_safety_util(dtype_t K, dtype_t L, dtype_t O):
    """
    K = EI (reference)
    L = EJ (reference)
    O = EM (reference)
    """
    if O >= K:
        return 1.0
    elif O == L:
        return 0.9
    elif O > K:
        return 1.0 - ((O - K) / (L - K) * 0.1)
    elif O > 0:
        return 0.9 * (O / L)
    else:
        return 0.0


cpdef dtype_t operational_environment_util(dtype_t K, dtype_t L, dtype_t O):
    """
    K = EI (reference)
    L = EJ (reference)
    O = EM (reference)
    """
    if O >= K:
        return 1.0
    elif O == L:
        return 0.9
    elif O > K:
        return 1.0 - ((O - K) / (L - K) * 0.1)
    elif O > 0:
        return 0.9 * (O / L)
    else:
        return 0.0


cpdef dtype_t pending_major_defects_util(dtype_t K, dtype_t L, dtype_t O):
    """
    K = FG (reference)
    L = FH (reference)
    O = FK (reference)
    """
    if O <= K:
        return 1.0
    elif K < O < L:
        return 1.0 - (O - K) / (L - K) * (1.0 - 0.9)
    elif O == L:
        return 0.9
    elif O > L:
        return 0.9 - pow(O - L, 2) / (pow(O - L, 2) + pow(L - K, 2)) * 0.9
    else:
        return -1.0  # Default case as numeric value


cpdef dtype_t pending_preventive_maintenance_util(dtype_t K, dtype_t L, dtype_t O):
    """
    K = FG (reference)
    L = FH (reference)
    O = FK (reference)
    """
    if O <= K:
        return 1.0
    elif K < O < L:
        return 1.0 - (O - K) / (L - K) * (1.0 - 0.9)
    elif O == L:
        return 0.9
    elif O > L:
        return 0.9 - pow(O - L, 2) / (pow(O - L, 2) + pow(L - K, 2)) * 0.9
    else:
        return -1.0  # Default case as numeric value


cpdef dtype_t allowable_utilisation_factor_util(dtype_t K, dtype_t L, dtype_t O):
    """
    K = FG (reference)
    L = FH (reference)
    O = FK (reference)
    """
    if O <= K:
        return 1.0
    elif K < O < L:
        return 1.0 - (O - K) / (L - K) * (1.0 - 0.9)
    elif O == L:
        return 0.9
    elif O > L:
        return 0.9 - pow(O - L, 2) / (pow(O - L, 2) + pow(L - K, 2)) * 0.9
    else:
        return -1.0


@cython.boundscheck(False)
@cython.wraparound(False)
def da_super_function(df, i):
    import numpy as np
    
    # Check if required columns exist
    required_cols = ["C1", "C2", "C5"]
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"DataFrame must contain these columns: {required_cols}")

    # Initialize results list and get values as numpy arrays for performance
    cdef:
        list results = []
        str metric_type = i[1]
        double[:] K_vals = df["C1"].to_numpy()
        double[:] L_vals = df["C2"].to_numpy()
        double[:] O_vals = df["C5"].to_numpy()
        int n_rows = len(df)
        int idx
        double result
    
    # Process based on metric type using optimized loop
    if metric_type == "Capacity (Efficiency) (%)":
        for idx in range(n_rows):
            result = capacity(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)

    elif metric_type == "Capacity (kW)":
        for idx in range(n_rows):
            result = capacity(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)

    elif metric_type == "Capacity (Voltage output)":
        for idx in range(n_rows):
            result = capacity(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)

    elif metric_type == "Capability (Response time) (SEC)":
        for idx in range(n_rows):
            result = capability_response_time(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)

    elif metric_type == "Reliability (%)":
        for idx in range(n_rows):
            result = reliability(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)

    elif metric_type == "Operational Availability (Total time available/ Total time available + Downtime OR simply availability) (%)":
        for idx in range(n_rows):
            result = operational_availability_util(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)

    elif metric_type == "Operational Maintainability (In how many hours the system is brought to ideal state) (Hours)":
        for idx in range(n_rows):
            result = operational_maintainability_util(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)

    elif metric_type == "Safety (Mission completion safety)":
        for idx in range(n_rows):
            result = mission_completion_safety_util(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)

    elif metric_type == "Safety (Human safety) (Hazard related)":
        for idx in range(n_rows):
            result = human_safety_util(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)

    elif metric_type == "Safety (Operational Environment)":
        for idx in range(n_rows):
            result = operational_environment_util(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)

    elif metric_type == "Maintenance (Pending MAJOR defects)":
        for idx in range(n_rows):
            result = pending_major_defects_util(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)

    elif metric_type == "Maintenance (Pending preventive maintenance)":
        for idx in range(n_rows):
            result = pending_preventive_maintenance_util(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)

    elif metric_type == "Allowable Utilisation Factor (For equal utilisation of equipment)":
        for idx in range(n_rows):
            result = allowable_utilisation_factor_util(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)

    print(df)
    print("probabs", results)
    return results