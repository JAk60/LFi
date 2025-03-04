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


def capability_response_time(K, L, O):
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


def capability_barllel_temperature_allowed(K, L, O):
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


def capability_rounds_per_min(K, L, O):  # Changed parameter order to match Excel
    if O >= K:
        print("1")
        return 1
    elif L <= O < K:
        return 0.9 + 0.1 * (O - L) / (K - L)
    else:
        return 0.9 * math.exp(-0.5 * (L - O))


def capability_ammunition_types(AY121, AZ121, BC121):
    """
    Converts Excel formula:
    =IF(BC121>=AY121,1,IF(AND(BC121>=AZ121,BC121<AY121),0.9+0.1*(BC121-AZ121)/(AY121-AZ121),0.9*EXP(-0.5*(AZ121-BC121))))

    Parameters:
    AY121: First parameter
    AZ121: Second parameter
    BC121: Third parameter
    """
    if BC121 >= AY121:
        return 1
    elif BC121 >= AZ121 and BC121 < AY121:
        return 0.9 + 0.1 * (BC121 - AZ121) / (AY121 - AZ121)
    else:
        return 0.9 * math.exp(-0.5 * (AZ121 - BC121))


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


def srgm_super_function(df, i):
    # Check if required columns exist
    required_cols = ["C1", "C2", "C5"]
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"DataFrame must contain these columns: {required_cols}")

    # Initialize results list
    results = []

    if i[1] == "Capacity (Range of fire)(Km)":
        # Process each row
        for index, row in df.iterrows():
            if i[7] in [1, 2]:  # Assuming i[7] is a valid index and should be checked
                results.append(0)
            else:
                result = capacity(row["C1"], row["C2"], row["C5"])
                results.append(result)

    elif i[1] == "Capacity (Elevation range)":
        # Process each row
        for index, row in df.iterrows():
            if i[7] in [1, 2]:  # Assuming i[7] is a valid index and should be checked
                results.append(0)
            else:
                result = capacity(row["C1"], row["C2"], row["C5"])
                results.append(result)

    elif i[1] == "Capacity (Magazine capacity)":
        # Process each row
        for index, row in df.iterrows():
            if i[7] in [1, 2]:  # Assuming i[7] is a valid index and should be checked
                results.append(0)
            else:
                result = capacity(row["C1"], row["C2"], row["C5"])
                results.append(result)

    elif i[1] == "Capability (Response time)(sec)":
        # Process each row
        for index, row in df.iterrows():
            if i[7] in [1, 2]:  # Assuming i[7] is a valid index and should be checked
                results.append(0)
            else:
                result = capability_response_time(row["C1"], row["C2"], row["C5"])
                results.append(result)

    elif i[1] == "Capability (Ronds per minute)":
        # Process each row
        for index, row in df.iterrows():
            if i[7] in [1, 2]:  # Assuming i[7] is a valid index and should be checked
                results.append(0)
            else:
                result = capability_rounds_per_min(row["C1"], row["C2"], row["C5"])
                results.append(result)

    elif i[1] == "Capability (Ammunition types)":
        # Process each row
        for index, row in df.iterrows():
            if i[7] in [1, 2]:  # Assuming i[7] is a valid index and should be checked
                results.append(0)
            else:
                result = capability_ammunition_types(row["C1"], row["C2"], row["C5"])
                results.append(result)

    elif i[1] == "Capability (Barrel temperature allowed)(Deg. C)":
        # Process each row
        for index, row in df.iterrows():
            if i[7] in [1, 2]:  # Assuming i[7] is a valid index and should be checked
                results.append(0)
            else:
                result = capability_barllel_temperature_allowed(
                    row["C1"], row["C2"], row["C5"]
                )
                results.append(result)

    elif i[1] == "Reliability (%)":
        # Process each row
        for index, row in df.iterrows():
            if i[7] in [1, 2]:  # Assuming i[7] is a valid index and should be checked
                results.append(0)
            else:
                result = reliability(row["C1"], row["C2"], row["C5"])
                results.append(result)

    elif (
        i[1]
        == "Operational Availability (Total time available/ Total time available + Downtime OR simply availability) (%)"
    ):
        # Process each row
        for index, row in df.iterrows():
            if i[7] in [1, 2]:  # Assuming i[7] is a valid index and should be checked
                results.append(0)
            else:
                result = operational_availability_util(row["C1"], row["C2"], row["C5"])
                results.append(result)

    elif (
        i[1]
        == "Operational Maintainability (In how many hours the system is brought to ideal state) (Hours)"
    ):
        # Process each row
        for index, row in df.iterrows():
            if i[7] in [1, 2]:  # Assuming i[7] is a valid index and should be checked
                results.append(0)
            else:
                result = operational_maintainability_util(
                    row["C1"], row["C2"], row["C5"]
                )
                results.append(result)

    elif i[1] == "Safety (Mission completion safety)":
        # Process each row
        for index, row in df.iterrows():
            if i[7] in [1, 2]:  # Assuming i[7] is a valid index and should be checked
                results.append(0)
            else:
                result = mission_completion_safety_util(row["C1"], row["C2"], row["C5"])
                results.append(result)

    elif i[1] == "Safety (Human safety) (Hazard related)":
        # Process each row
        for index, row in df.iterrows():
            if i[7] in [1, 2]:  # Assuming i[7] is a valid index and should be checked
                results.append(0)
            else:
                result = human_safety_util(row["C1"], row["C2"], row["C5"])
                results.append(result)

    elif i[1] == "Safety (Operational Environment)":
        # Process each row
        for index, row in df.iterrows():
            if i[7] in [1, 2]:  # Assuming i[7] is a valid index and should be checked
                results.append(0)
            else:
                result = operational_environment_util(row["C1"], row["C2"], row["C5"])
                results.append(result)

    elif i[1] == "Maintenance (Pending MAJOR defects)":
        # Process each row
        for index, row in df.iterrows():
            if i[7] in [1, 2]:  # Assuming i[7] is a valid index and should be checked
                results.append(0)
            else:
                result = Pending_major_defects_util(row["C1"], row["C2"], row["C5"])
                results.append(result)

    elif i[1] == "Maintenance (Pending preventive maintenance)":
        # Process each row
        for index, row in df.iterrows():
            if i[7] in [1, 2]:  # Assuming i[7] is a valid index and should be checked
                results.append(0)
            else:
                result = Pending_preventive_maintenance_util(
                    row["C1"], row["C2"], row["C5"]
                )
                results.append(result)

    elif i[1] == "Allowable Utilisation Factor (For equal utilisation of equipment)":
        # Process each row
        for index, row in df.iterrows():
            if i[7] in [1, 2]:  # Assuming i[7] is a valid index and should be checked
                results.append(0)
            else:
                result = allowable_utilisation_factor_util(
                    row["C1"], row["C2"], row["C5"]
                )
                results.append(result)

    print(df)
    print(results)
    return results
