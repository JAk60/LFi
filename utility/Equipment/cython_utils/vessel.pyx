# vessel_utils.pyx
import math
cimport cython


@cython.cdivision(True)  # Disable division by zero checking for performance
@cython.boundscheck(False)  # Disable bounds checking for performance
@cython.wraparound(False)  # Disable negative indexing for performance
cpdef double capacity(double K, double L, double O):
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
        return 0.0  # Changed from "" to 0.0 as Cython needs consistent return types


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double capability_minimum_radius_of_turn(double K, double L, double O):
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
        # Calculate denominator outside conditional
        return 0.9 - (O - L) ** 2 / ((O - L) ** 2 + (L - K) ** 2) * 0.9  # Quadratic decay
    return 0.0  # Default case


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double capability_time_for_refuel(double K, double L, double O):
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


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double capability_range_without_refueling(double K, double L, double O):
    if O >= K:
        return 1.0

    elif O >= L and O < K:
        if K != L:
            return 0.9 + 0.1 * (O - L) / (K - L)
        else:
            return 0.9

    else:
        return 0.9 * math.exp(-0.5 * (L - O))


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double capability_stealth(double K, double L, double O):
    if O >= K:
        return 1.0

    elif O >= L and O < K:
        if K != L:
            return 0.9 + 0.1 * (O - L) / (K - L)
        else:
            return 0.9

    else:
        return 0.9 * math.exp(-0.5 * (L - O))


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double reliability(double K, double L, double O):
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
        return 0.0  # Changed from "" to 0.0


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double operational_availability_util(double CM138, double CN138, double CQ138):
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


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double operational_maintainability_util(double K, double L, double O):
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


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double mission_completion_safety_util(double K, double L, double O):
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


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double human_safety_util(double K, double L, double O):
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


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double operational_environment_util(double K, double L, double O):
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


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double Pending_major_defects_util(double K, double L, double O):
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
        return 0.0  # Changed from None to 0.0


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double Pending_preventive_maintenance_util(double K, double L, double O):
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
        return 0.0  # Changed from None to 0.0


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double allowable_utilisation_factor_util(double K, double L, double O):
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
        return 0.0  # Changed from None to 0.0


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double stealth_radar(double K, double L, double O):
    cdef double denominator
    
    if O <= K:
        return 1.0
    elif K < O < L:
        if L != K:
            return 1.0 - (O - K) / (L - K) * (1.0 - 0.9)
        else:
            return 0.9
    elif O == L:
        return 0.9
    elif O > L:
        denominator = (O - L) ** 2 + (L - K) ** 2
        if denominator != 0:
            return 0.9 - (O - L) ** 2 / denominator * 0.9
        else:
            return 0.9
    else:
        return 0.0  # Changed from "" to 0.0


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double stealth_signature(double K, double L, double O):
    cdef double denominator
    
    if O <= K:
        return 1.0
    elif K < O < L:
        if L != K:
            return 1.0 - (O - K) / (L - K) * (1.0 - 0.9)
        else:
            return 0.9
    elif O == L:
        return 0.9
    elif O > L:
        denominator = (O - L) ** 2 + (L - K) ** 2
        if denominator != 0:
            return 0.9 - (O - L) ** 2 / denominator * 0.9
        else:
            return 0.9
    else:
        return 0.0  # Changed from "" to 0.0


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double stealth_jammaer_util(double K, double L, double O):
    """
    K = K column reference
    L = L column reference
    O = O column reference
    """
    if O >= K:
        return 1.0
    elif K > O > L:
        return 0.9 + 0.1 * ((O - L) / (K - L)) ** 2  # Quadratic interpolation
    elif O == L:
        return 0.9
    elif O < L:
        if L != 0:
            return 0.9 * (O / L)
        else:
            return 0.0
    return 0.0  # Default case


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double non_vulnerablity_util(double K, double L, double O):
    """
    K = K column reference
    L = L column reference
    O = O column reference
    """
    if O >= K:
        return 1.0
    elif K > O > L:
        return 0.9 + 0.1 * ((O - L) / (K - L)) ** 2  # Quadratic interpolation
    elif O == L:
        return 0.9
    elif O < L:
        if L != 0:
            return 0.9 * (O / L)
        else:
            return 0.0
    return 0.0  # Default case


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double recoverability(double K, double L, double O):
    if O >= K:
        return 1.0
    elif O == L:
        return 0.9
    elif O > K:
        if (L - K) != 0:
            return 1.0 - ((O - K) / (L - K) * 0.1)
        else:
            return 0.9
    elif O > 0:
        return 0.9 * (O / L)
    else:
        return 0.0


# For the DataFrame processing function, we need to use Python objects
def vessel_super_function(df, i):
    # Check if required columns exist in the DataFrame
    required_cols = ["C1", "C2", "C5"]
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"DataFrame must contain these columns: {required_cols}")

    # Initialize results list
    results = []

    # Attribute mappings for calculation functions
    attribute_mapping = {
        "Capacity (Maximum Speed)(knots)": capacity,
        "Capacity (Endurance) (Ration+Fuel) (Days)": capacity,
        "Capability (Minimum radius of turn)(metre)": capability_minimum_radius_of_turn,
        "Capability (Range without refuelling)(Nm)": capability_range_without_refueling,
        "Capability (Time for refuelling)(Hours)": capability_time_for_refuel,
        "Capability (Stealth)(scale 1-10)": capability_stealth,
        "Reliability (%)": reliability,
        "Operational Availability (Total time available/ Total time available + Downtime OR simply availability) (%)": operational_availability_util,
        "Operational Maintainability (Hours)( In how many hours the system is brought to ideal state)": operational_maintainability_util,
        "Safety (Mission completion safety)": mission_completion_safety_util,
        "Safety (Human safety) (Hazard related)": human_safety_util,
        "Safety (Operational Environment)": operational_environment_util,
        "Maintenance (Pending MAJOR defects)": Pending_major_defects_util,
        "Maintenance (Pending preventive maintenance)": Pending_preventive_maintenance_util,
        "Allowable Utilisation Factor (For equal utilisation of equipment)": allowable_utilisation_factor_util,
    }

    # Special attributes (only calculated when i[7] is 2 or 3)
    special_attributes = {
        "Stealth (Radar c/s)( sq. metre)": stealth_radar,
        "Stealth (Signature)(Noise in DB)": stealth_signature,
        "Stealth - Jammers (Scale 1-10)": stealth_jammaer_util,
        "Non vulnerability (Scale 1-10)": non_vulnerablity_util,
        "Recoverability (Scale 1-10)": recoverability,
    }

    # Determine the function to use
    if i[1] in special_attributes:
        if i[7] in [2, 3]:
            print("Entered special attribute calculation:", i[7])
            func = special_attributes[i[1]]
        else:
            return [0]  # Special attributes return 0 when i[7] is not 2 or 3
    elif i[1] in attribute_mapping:
        func = attribute_mapping[i[1]]
    else:
        raise ValueError(f"Invalid attribute: {i[1]}")

    # Process each row using the selected function
    for index, row in df.iterrows():
        result = func(row["C1"], row["C2"], row["C5"])  # Apply function
        results.append(result)

    print(df)
    print(results)
    return results