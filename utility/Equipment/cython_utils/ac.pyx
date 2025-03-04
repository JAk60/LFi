import pandas as pd
import numpy as np
cimport numpy as np
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
def capacity(double K, double L, double O):
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
        return -1.0  # Return -1 for error, easier to handle in Cython


@cython.boundscheck(False)
@cython.wraparound(False)
def capability_response_time(double K, double L, double O):
    if O <= K:
        return 1.0
    elif K < O < L:
        return 1.0 - (O - K) / (L - K) * (1.0 - 0.9)
    elif O == L:
        return 0.9
    elif O > L:
        return 0.9 - (O - L)**2 / ((O - L)**2 + (L - K)**2) * 0.9
    return -1.0 # Error


@cython.boundscheck(False)
@cython.wraparound(False)
def reliability(double K, double L, double O):
    if O >= K:
        return 1.0
    elif O < K and O > L:
        return 1 - (K - O) / (K - L) * 0.1 if K != L else 1.0
    elif O == L:
        return 0.9
    elif O < L:
        return 0.9 * (O / L)**2 if L != 0 else 0.0
    elif O == 0:
        return 0.0
    else:
        return -1.0 # Error


@cython.boundscheck(False)
@cython.wraparound(False)
def operational_availability_util(double CM138, double CN138, double CQ138):
    if CQ138 >= CM138:
        return 1.0
    elif CM138 > CQ138 > CN138:
        return 0.9 + 0.1 * ((CQ138 - CN138) / (CM138 - CN138))**2 if CM138 != CN138 else 0.9
    elif CQ138 == CN138:
        return 0.9
    elif CQ138 < CN138:
        return 0.9 * (CQ138 / CN138) if CN138 != 0 else 0.0
    else:
        return 0.0 # No Error, as per your original code


@cython.boundscheck(False)
@cython.wraparound(False)
def operational_maintainability_util(double K, double L, double O):
    if O <= K:
        return 1.0
    elif O == L:
        return 0.9
    elif O < L:
        return 0.9 + 0.1 * (1 - (O - K) / (L - K))**2
    elif O <= 2 * K:
        return 0.9 * (1 - (O - L) / (2 * K - L))**2
    else:
        return 0.0


@cython.boundscheck(False)
@cython.wraparound(False)
def mission_completion_safety_util(double K, double L, double O):
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


@cython.boundscheck(False)
@cython.wraparound(False)
def human_safety_util(double K, double L, double O):
    return mission_completion_safety_util(K, L, O)  # Same logic


@cython.boundscheck(False)
@cython.wraparound(False)
def operational_environment_util(double K, double L, double O):
    return mission_completion_safety_util(K, L, O)  # Same logic


@cython.boundscheck(False)
@cython.wraparound(False)
def Pending_major_defects_util(double K, double L, double O):
    if O <= K:
        return 1.0
    elif K < O < L:
        return 1.0 - (O - K) / (L - K) * (1.0 - 0.9)
    elif O == L:
        return 0.9
    elif O > L:
        return 0.9 - (O - L)**2 / ((O - L)**2 + (L - K)**2) * 0.9
    return -1.0 # Error


@cython.boundscheck(False)
@cython.wraparound(False)
def Pending_preventive_maintenance_util(double K, double L, double O):
     return Pending_major_defects_util(K, L, O) # Same logic


@cython.boundscheck(False)
@cython.wraparound(False)
def allowable_utilisation_factor_util(double K, double L, double O):
    return Pending_major_defects_util(K, L, O) # Same logic



import numpy as np
cimport numpy as np
cimport cython
import pandas as pd



@cython.boundscheck(False)
@cython.wraparound(False)
def ac_super_function(df, tuple i):
    cdef int j
    cdef int n

    required_cols = ["C1", "C2", "C5"]
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"DataFrame must contain these columns: {required_cols}")

    # Optimized DataFrame access: Use memoryviews!
    cdef double[::1] C1 = np.asarray(df["C1"].astype(np.float64)).view(np.float64)  # Memoryview
    cdef double[::1] C2 = np.asarray(df["C2"].astype(np.float64)).view(np.float64)  # Memoryview
    cdef double[::1] C5 = np.asarray(df["C5"].astype(np.float64)).view(np.float64)  # Memoryview

    n = len(df)
    cdef np.ndarray[double, ndim=1] results = np.empty(n, dtype=np.float64)

    if i[1] == "Capacity (TR)":
        for j in range(n):
            results[j] = capacity(C1[j], C2[j], C5[j])

    elif i[1] == "Capability (Response time) (SEC)":
        for j in range(n):
            results[j] = capability_response_time(C1[j], C2[j], C5[j])

    elif i[1] == "Reliability (%)":
        for j in range(n):
            results[j] = reliability(C1[j], C2[j], C5[j])

    elif i[1] == "Operational Availability (Total time available/ Total time available + Downtime OR simply availability) (%)":
        for j in range(n):
            results[j] = operational_availability_util(C1[j], C2[j], C5[j])

    elif i[1] == "Operational Maintainability (In how many hours the system is brought to ideal state) (Hours)":
        for j in range(n):
            results[j] = operational_maintainability_util(C1[j], C2[j], C5[j])

    elif i[1] == "Safety (Mission completion safety)":
        for j in range(n):
            results[j] = mission_completion_safety_util(C1[j], C2[j], C5[j])

    elif i[1] == "Safety (Human safety) (Hazard related)":
        for j in range(n):
            results[j] = human_safety_util(C1[j], C2[j], C5[j])

    elif i[1] == "Safety (Operational Environment)":
        for j in range(n):
            results[j] = operational_environment_util(C1[j], C2[j], C5[j])

    elif i[1] == "Maintenance (Pending MAJOR defects)":
        for j in range(n):
            results[j] = Pending_major_defects_util(C1[j], C2[j], C5[j])

    elif i[1] == "Maintenance (Pending preventive maintenance)":
        for j in range(n):
            results[j] = Pending_preventive_maintenance_util(C1[j], C2[j], C5[j])

    elif i[1] == "Allowable Utilisation Factor (For equal utilisation of equipment)":
        for j in range(n):
            results[j] = allowable_utilisation_factor_util(C1[j], C2[j], C5[j])

    return results