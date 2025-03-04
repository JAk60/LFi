# Save as utils.pyx
import math
from cpython cimport bool

# Define C types for better performance
ctypedef double dtype_t

cpdef dtype_t capacity_power(dtype_t K, dtype_t L, dtype_t O):
    if O >= K:
        return 1.0
    elif K > O >= L:
        return 0.9 + 0.1 * (O - L) / (K - L)  # Linear interpolation
    else:  # O < L
        return 0.9 * math.exp(-0.5 * (L - O))  # Exponential decay

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
        return -1.0  # Return a numeric value instead of empty string for consistency

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
        return 0.9 - (O - L) ** 2 / ((O - L) ** 2 + (L - K) ** 2) * 0.9  # Quadratic decay
    return -1.0  # Default case

cpdef dtype_t capability_multiple_fuel_acceptance(dtype_t O):
    return 1.0 - O

cpdef dtype_t capability_vibration_suppression_util(dtype_t K, dtype_t L, dtype_t O):
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
            result = 0.9 * (O / L) ** 2
        else:
            result = 0.0
        return result
    elif O == 0:
        return 0.0
    else:
        return -1.0  # Default case as numeric value

cpdef dtype_t operational_availability_util(dtype_t CM138, dtype_t CN138, dtype_t CQ138):
    cdef dtype_t result

    if CQ138 >= CM138:
        return 1.0
    elif CM138 > CQ138 > CN138:
        if CM138 != CN138:
            result = 0.9 + 0.1 * ((CQ138 - CN138) / (CM138 - CN138)) ** 2
        else:
            result = 0.9
        return result
    elif CQ138 == CN138:
        return 0.9
    elif CQ138 < CN138:
        if CN138 != 0:
            result = 0.9 * (CQ138 / CN138)
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
    if O <= K:
        return 1.0
    elif O == L:
        return 0.9
    elif K < O < L:
        return 0.9 + 0.1 * (1.0 - (O - K) / (L - K)) ** 2
    elif O <= 2.0 * K:
        return 0.9 * (1.0 - (O - L) / (2.0 * K - L)) ** 2
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
    elif L < O < K:
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
    elif L < O < K:
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
    elif L < O < K:
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
        return 0.9 - (O - L) ** 2 / ((O - L) ** 2 + (L - K) ** 2) * 0.9
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
        return 0.9 - (O - L) ** 2 / ((O - L) ** 2 + (L - K) ** 2) * 0.9
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
        return 0.9 - (O - L) ** 2 / ((O - L) ** 2 + (L - K) ** 2) * 0.9
    else:
        return -1.0

# Cythonized pandas dataframe processing function
def gt_super_function(df, i):
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

    # Process each metric type
    if metric_type == "Capacity (Efficiency) (%)":
        for idx in range(n_rows):
            result = capacity(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)
        results.append("Capacity (Efficiency) (%)")

    elif metric_type == "Capacity (Power) (MW)":
        for idx in range(n_rows):
            result = capacity_power(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)
        results.append("Capacity (Power) (MW)")

    elif metric_type == "Capacity (Shaft Rotation) (RPM)":
        for idx in range(n_rows):
            result = capacity(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)
        results.append("Capacity (Shaft Rotation) (RPM)")

    elif metric_type == "Capability (Response time) (SEC)":
        for idx in range(n_rows):
            result = capability_response_time(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)
        results.append("Capability (Response time) (SEC)")

    elif metric_type == "Capability (Multiple fuel acceptance) (%)":
        for idx in range(n_rows):
            result = capability_multiple_fuel_acceptance(O_vals[idx])
            results.append(result)
        results.append("Capability (Multiple fuel acceptance) (%)")

    elif metric_type == "Capability (Vibration suppression)":
        for idx in range(n_rows):
            result = capability_vibration_suppression_util(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)
        results.append("Capability (Vibration suppression)")

    elif metric_type == "Reliability (%)":
        for idx in range(n_rows):
            result = reliability(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)
        results.append("Reliability (%)")

    elif metric_type == "Operational Availability (Total time available/ Total time available + Downtime OR simply availability) (%)":
        for idx in range(n_rows):
            result = operational_availability_util(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)
        results.append("Operational Availability (Total time available/ Total time available + Downtime OR simply availability) (%)")

    elif metric_type == "Operational Maintainability (In how many hours the system is brought to ideal state) (Hours)":
        for idx in range(n_rows):
            result = operational_maintainability_util(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)
        results.append("Operational Maintainability (In how many hours the system is brought to ideal state) (Hours)")

    elif metric_type == "Safety (Mission completion safety)":
        for idx in range(n_rows):
            result = mission_completion_safety_util(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)
        results.append("Safety (Mission completion safety)")

    elif metric_type == "Safety (Human safety) (Hazard related)":
        for idx in range(n_rows):
            result = human_safety_util(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)
        results.append("Safety (Human safety) (Hazard related)")

    elif metric_type == "Safety (Operational Environment)":
        for idx in range(n_rows):
            result = operational_environment_util(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)
        results.append("Safety (Operational Environment)")

    elif metric_type == "Maintenance (Pending MAJOR defects)":
        for idx in range(n_rows):
            result = pending_major_defects_util(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)
        results.append("Maintenance (Pending MAJOR defects)")

    elif metric_type == "Maintenance (Pending preventive maintenance)":
        for idx in range(n_rows):
            result = pending_preventive_maintenance_util(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)
        results.append("Maintenance (Pending preventive maintenance)")

    elif metric_type == "Allowable Utilisation Factor (For equal utilisation of equipment)":
        for idx in range(n_rows):
            result = allowable_utilisation_factor_util(K_vals[idx], L_vals[idx], O_vals[idx])
            results.append(result)
        results.append("Allowable Utilisation Factor (For equal utilisation of equipment)")

    print(df)
    print(results)
    return results
