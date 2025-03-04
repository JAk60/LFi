import math


def capacity(K, L, O):
    if O >= K:
        return 1
    elif K > O > L:
        return 1 - ((K - O) / (K - L) * 0.1)
    elif O == L:
        return 0.9
    elif O < L:
        return 0.9 - ((L - O) / L * 0.9)
    elif O == 0:
        return 0
    else:
        return ""


def capability_minimum_radius_of_turn(K, L, O):
    """
    K = K column reference
    L = L column reference
    O = O column reference
    """
    if O <= K:
        return 1
    elif K < O < L:
        return 1 - (O - K) / (L - K) * (1 - 0.9)  # Linear interpolation
    elif O == L:
        return 0.9
    elif O > L:
        return (
            0.9 - (O - L) ** 2 / ((O - L) ** 2 + (L - K) ** 2) * 0.9
        )  # Quadratic decay
    return None  # Default case


def capability_time_for_refuel(K, L, O):
    """
    K = K column reference
    L = L column reference
    O = O column reference
    """
    if O <= K:
        return 1
    elif K < O < L:
        return 1 - (O - K) / (L - K) * (1 - 0.9)  # Linear interpolation
    elif O == L:
        return 0.9
    elif O > L:
        return (
            0.9 - (O - L) ** 2 / ((O - L) ** 2 + (L - K) ** 2) * 0.9
        )  # Quadratic decay
    return None  # Default case


def capability_range_without_refueling(K, L, O):
    if O >= K:
        return 1.0  # Equivalent to IF(O >= K, 1, ...)

    elif O >= L and O < K:
        return 0.9 + 0.1 * (O - L) / (K - L) if K != L else 0.9
        # Equivalent to IF(AND(O >= L, O < K), 0.9 + 0.1 * (O - L) / (K - L), ...)

    else:
        return 0.9 * math.exp(-0.5 * (L - O))
        # Equivalent to IF(..., 0.9 * EXP(-0.5 * (L - O)))


def capability_stealth(K, L, O):
    if O >= K:
        return 1.0  # Equivalent to IF(O >= K, 1, ...)

    elif O >= L and O < K:
        return 0.9 + 0.1 * (O - L) / (K - L) if K != L else 0.9
        # Equivalent to IF(AND(O >= L, O < K), 0.9 + 0.1 * (O - L) / (K - L), ...)

    else:
        return 0.9 * math.exp(-0.5 * (L - O))
        # Equivalent to IF(..., 0.9 * EXP(-0.5 * (L - O)))


def reliability(K, L, O):
    if O >= K:
        return 1.0  # Equivalent to IF(O >= K, 1, ...)

    elif O < K and O > L:
        return 1 - (K - O) / (K - L) * 0.1 if K != L else 1
        # Equivalent to IF(AND(O < K, O > L), 1 - (K - O) / (K - L) * 0.1, ...)

    elif O == L:
        return 0.9  # Equivalent to IF(O = L, 0.9, ...)

    elif O < L:
        return (
            0.9 * (O / L) ** 2 if L != 0 else 0
        )  # Equivalent to IF(O < L, 0.9 * (O / L)^2, ...)

    elif O == 0:
        return 0  # Equivalent to IF(O = 0, 0, ...)

    else:
        return ""  # Default case as in Excel


def operational_availability_util(CM138, CN138, CQ138):
    if CQ138 >= CM138:
        return 1.0  # Equivalent to IF(CQ138 >= CM138, 1, ...)

    elif CM138 > CQ138 > CN138:
        return (
            0.9 + 0.1 * ((CQ138 - CN138) / (CM138 - CN138)) ** 2
            if CM138 != CN138
            else 0.9
        )
        # Equivalent to IF(AND(CQ138 < CM138, CQ138 > CN138), 0.9 + 0.1 * ((CQ138 - CN138) / (CM138 - CN138))^2, ...)

    elif CQ138 == CN138:
        return 0.9  # Equivalent to IF(CQ138 = CN138, 0.9, ...)

    elif CQ138 < CN138:
        return (
            0.9 * (CQ138 / CN138) if CN138 != 0 else 0
        )  # Equivalent to IF(CQ138 < CN138, 0.9 * (CQ138 / CN138), ...)

    else:
        return 0  # Default case as in Excel


def operational_maintainability_util(K, L, O):
    """
    K = DK (reference)
    L = DL (reference)
    O = DO (reference)
    """
    if O <= K:
        return 1
    elif O == L:
        return 0.9
    elif O < L:
        return 0.9 + 0.1 * (1 - (O - K) / (L - K)) ** 2
    elif O <= 2 * K:
        return 0.9 * (1 - (O - L) / (2 * K - L)) ** 2
    else:
        return 0


def mission_completion_safety_util(K, L, O):
    """
    K = EI (reference)
    L = EJ (reference)
    O = EM (reference)
    """
    if O >= K:
        return 1
    elif O == L:
        return 0.9
    elif O > K:
        return 1 - ((O - K) / (L - K) * 0.1)
    elif O > 0:
        return 0.9 * (O / L)
    else:
        return 0


def human_safety_util(K, L, O):
    """
    K = EI (reference)
    L = EJ (reference)
    O = EM (reference)
    """
    if O >= K:
        return 1
    elif O == L:
        return 0.9
    elif O > K:
        return 1 - ((O - K) / (L - K) * 0.1)
    elif O > 0:
        return 0.9 * (O / L)
    else:
        return 0


def operational_environment_util(K, L, O):
    """
    K = EI (reference)
    L = EJ (reference)
    O = EM (reference)
    """
    if O >= K:
        return 1
    elif O == L:
        return 0.9
    elif O > K:
        return 1 - ((O - K) / (L - K) * 0.1)
    elif O > 0:
        return 0.9 * (O / L)
    else:
        return 0


def Pending_major_defects_util(K, L, O):
    """
    K = FG (reference)
    L = FH (reference)
    O = FK (reference)
    """
    if O <= K:
        return 1
    elif K < O < L:
        return 1 - (O - K) / (L - K) * (1 - 0.9)
    elif O == L:
        return 0.9
    elif O > L:
        return 0.9 - (O - L) ** 2 / ((O - L) ** 2 + (L - K) ** 2) * 0.9
    else:
        return None  # If no condition is met (shouldn't be needed)


def Pending_preventive_maintenance_util(K, L, O):
    """
    K = FG (reference)
    L = FH (reference)
    O = FK (reference)
    """
    if O <= K:
        return 1
    elif K < O < L:
        return 1 - (O - K) / (L - K) * (1 - 0.9)
    elif O == L:
        return 0.9
    elif O > L:
        return 0.9 - (O - L) ** 2 / ((O - L) ** 2 + (L - K) ** 2) * 0.9
    else:
        return None  # If no condition is met (shouldn't be needed)


def allowable_utilisation_factor_util(K, L, O):
    """
    K = FG (reference)
    L = FH (reference)
    O = FK (reference)
    """
    if O <= K:
        return 1
    elif K < O < L:
        return 1 - (O - K) / (L - K) * (1 - 0.9)
    elif O == L:
        return 0.9
    elif O > L:
        return 0.9 - (O - L) ** 2 / ((O - L) ** 2 + (L - K) ** 2) * 0.9
    else:
        return None


def stealth_radar(K, L, O):
    if O <= K:
        return 1.0  # Equivalent to IF(O <= K, 1, ...)

    elif K < O < L:
        return 1 - (O - K) / (L - K) * (1 - 0.9) if L != K else 0.9
        # Equivalent to IF(AND(O > K, O < L), 1 - (O - K) / (L - K) * (1 - 0.9), ...)

    elif O == L:
        return 0.9  # Equivalent to IF(O = L, 0.9, ...)

    elif O > L:
        return (
            0.9 - (O - L) ** 2 / ((O - L) ** 2 + (L - K) ** 2) * 0.9
            if (O - L) ** 2 + (L - K) ** 2 != 0
            else 0.9
        )
        # Equivalent to IF(O > L, 0.9 - (O - L)^2 / ((O - L)^2 + (L - K)^2) * 0.9, ...)

    else:
        return ""  # Default case as in Excel


def stealth_signature(K, L, O):
    if O <= K:
        return 1.0  # Equivalent to IF(O <= K, 1, ...)

    elif K < O < L:
        return 1 - (O - K) / (L - K) * (1 - 0.9) if L != K else 0.9
        # Equivalent to IF(AND(O > K, O < L), 1 - (O - K) / (L - K) * (1 - 0.9), ...)

    elif O == L:
        return 0.9  # Equivalent to IF(O = L, 0.9, ...)

    elif O > L:
        return (
            0.9 - (O - L) ** 2 / ((O - L) ** 2 + (L - K) ** 2) * 0.9
            if (O - L) ** 2 + (L - K) ** 2 != 0
            else 0.9
        )
        # Equivalent to IF(O > L, 0.9 - (O - L)^2 / ((O - L)^2 + (L - K)^2) * 0.9, ...)

    else:
        return ""  # Default case as in Excel


def stealth_jammaer_util(K, L, O):
    """
    K = K column reference
    L = L column reference
    O = O column reference
    """
    if O >= K:
        return 1
    elif K > O > L:
        return 0.9 + 0.1 * ((O - L) / (K - L)) ** 2  # Quadratic interpolation
    elif O == L:
        return 0.9
    elif O < L:
        return 0.9 * (O / L) if L != 0 else 0  # Avoid division by zero
    return 0  # Default case


def non_vulnerablity_util(K, L, O):
    """
    K = K column reference
    L = L column reference
    O = O column reference
    """
    if O >= K:
        return 1
    elif K > O > L:
        return 0.9 + 0.1 * ((O - L) / (K - L)) ** 2  # Quadratic interpolation
    elif O == L:
        return 0.9
    elif O < L:
        return 0.9 * (O / L) if L != 0 else 0  # Avoid division by zero
    return 0  # Default case


def recoverability(K, L, O):
    if O >= K:
        return 1  # Equivalent to IF(O >= K, 1, ...)

    elif O == L:
        return 0.9  # Equivalent to IF(O = L, 0.9, ...)

    elif O > K:
        return (
            1 - ((O - K) / (L - K) * 0.1) if (L - K) != 0 else 0.9
        )  # Equivalent to IF(O > K, 1 - ((O - K) / (L - K) * 0.1), ...)

    elif O > 0:
        return 0.9 * (O / L)  # Equivalent to IF(O > 0, 0.9 * (O / L), ...)

    else:
        return 0  # Default case for when none of the conditions are met


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
