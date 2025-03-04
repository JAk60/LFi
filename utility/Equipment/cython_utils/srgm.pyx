# distutils: language=c++
# cython: boundscheck=False, wraparound=False, nonecheck=False, cdivision=True
import cython
from libc.math cimport exp

cdef double capacity(double K, double L, double O):
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
        return 0.0  # Replace empty string with numeric default

cdef double capability_response_time(double K, double L, double O):
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
    return 0.0  # Default case

cdef double capability_barllel_temperature_allowed(double K, double L, double O):
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
    return 0.0  # Default case

cdef double capability_rounds_per_min(double K, double L, double O):
    if O >= K:
        return 1.0
    elif L <= O < K:
        return 0.9 + 0.1 * (O - L) / (K - L)
    else:
        return 0.9 * exp(-0.5 * (L - O))

cdef double capability_ammunition_types(double AY121, double AZ121, double BC121):
    """
    Converts Excel formula:
    =IF(BC121>=AY121,1,IF(AND(BC121>=AZ121,BC121<AY121),0.9+0.1*(BC121-AZ121)/(AY121-AZ121),0.9*EXP(-0.5*(AZ121-BC121))))
    """
    if BC121 >= AY121:
        return 1.0
    elif BC121 >= AZ121 and BC121 < AY121:
        return 0.9 + 0.1 * (BC121 - AZ121) / (AY121 - AZ121)
    else:
        return 0.9 * exp(-0.5 * (AZ121 - BC121))

cdef double capability_stealth(double K, double L, double O):
    if O >= K:
        return 1.0
    elif O >= L and O < K:
        if K != L:
            return 0.9 + 0.1 * (O - L) / (K - L)
        else:
            return 0.9
    else:
        return 0.9 * exp(-0.5 * (L - O))

cdef double reliability(double K, double L, double O):
    if O >= K:
        return 1.0
    elif O < K and O > L:
        if K != L:
            return 1.0 - (K - O) / (K - L) * 0.1
        else:
            return 1.0
    elif O == L:
        return 0.9
    elif O < L:
        if L != 0:
            return 0.9 * (O / L) ** 2
        else:
            return 0.0
    elif O == 0:
        return 0.0
    else:
        return 0.0  # Default case

cdef double operational_availability_util(double CM138, double CN138, double CQ138):
    if CQ138 >= CM138:
        return 1.0
    elif CM138 > CQ138 > CN138:
        if CM138 != CN138:
            return 0.9 + 0.1 * ((CQ138 - CN138) / (CM138 - CN138)) ** 2
        else:
            return 0.9
    elif CQ138 == CN138:
        return 0.9
    elif CQ138 < CN138:
        if CN138 != 0:
            return 0.9 * (CQ138 / CN138)
        else:
            return 0.0
    else:
        return 0.0

cdef double operational_maintainability_util(double K, double L, double O):
    """
    K = DK (reference)
    L = DL (reference)
    O = DO (reference)
    """
    if O <= K:
        return 1.0
    elif O == L:
        return 0.9
    elif O < L:
        return 0.9 + 0.1 * (1.0 - (O - K) / (L - K)) ** 2
    elif O <= 2.0 * K:
        return 0.9 * (1.0 - (O - L) / (2.0 * K - L)) ** 2
    else:
        return 0.0

cdef double mission_completion_safety_util(double K, double L, double O):
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

cdef double human_safety_util(double K, double L, double O):
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

cdef double operational_environment_util(double K, double L, double O):
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

cdef double Pending_major_defects_util(double K, double L, double O):
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
        return 0.0

cdef double Pending_preventive_maintenance_util(double K, double L, double O):
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
        return 0.0

cdef double allowable_utilisation_factor_util(double K, double L, double O):
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
        return 0.0

def srgm_super_function(df, i):
    # We'll use typed memoryviews for optimized results list
    cdef list results = []
    cdef int row_count = len(df)
    cdef double c1, c2, c5
    cdef int idx
    cdef int i7 = i[7]

    # Check if required columns exist
    required_cols = ["C1", "C2", "C5"]
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"DataFrame must contain these columns: {required_cols}")

    function_name = i[1]

    # Process each row based on function name
    for idx in range(row_count):
        if i7 in [1, 2]:
            results.append(0.0)
            continue

        # Extract values
        c1 = df.iloc[idx]["C1"]
        c2 = df.iloc[idx]["C2"]
        c5 = df.iloc[idx]["C5"]

        # Dispatch to the correct function
        if function_name == "Capacity (Range of fire)(Km)" or \
           function_name == "Capacity (Elevation range)" or \
           function_name == "Capacity (Magazine capacity)":
            results.append(capacity(c1, c2, c5))

        elif function_name == "Capability (Response time)(sec)":
            results.append(capability_response_time(c1, c2, c5))

        elif function_name == "Capability (Ronds per minute)":
            results.append(capability_rounds_per_min(c1, c2, c5))

        elif function_name == "Capability (Ammunition types)":
            results.append(capability_ammunition_types(c1, c2, c5))

        elif function_name == "Capability (Barrel temperature allowed)(Deg. C)":
            results.append(capability_barllel_temperature_allowed(c1, c2, c5))

        elif function_name == "Reliability (%)":
            results.append(reliability(c1, c2, c5))

        elif function_name == "Operational Availability (Total time available/ Total time available + Downtime OR simply availability) (%)":
            results.append(operational_availability_util(c1, c2, c5))

        elif function_name == "Operational Maintainability (In how many hours the system is brought to ideal state) (Hours)":
            results.append(operational_maintainability_util(c1, c2, c5))

        elif function_name == "Safety (Mission completion safety)":
            results.append(mission_completion_safety_util(c1, c2, c5))

        elif function_name == "Safety (Human safety) (Hazard related)":
            results.append(human_safety_util(c1, c2, c5))

        elif function_name == "Safety (Operational Environment)":
            results.append(operational_environment_util(c1, c2, c5))

        elif function_name == "Maintenance (Pending MAJOR defects)":
            results.append(Pending_major_defects_util(c1, c2, c5))

        elif function_name == "Maintenance (Pending preventive maintenance)":
            results.append(Pending_preventive_maintenance_util(c1, c2, c5))

        elif function_name == "Allowable Utilisation Factor (For equal utilisation of equipment)":
            results.append(allowable_utilisation_factor_util(c1, c2, c5))

    return results
