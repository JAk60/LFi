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


def operational_availability_util(K, L, O):
    if O >= K:
        return 1.0  # Equivalent to IF(O >= K, 1, ...)

    elif K > O > L:
        return 0.9 + 0.1 * ((O - L) / (K - L)) ** 2 if K != L else 0.9
        # Equivalent to IF(AND(O < K, O > L), 0.9 + 0.1 * ((O - L) / (K - L))^2, ...)

    elif O == L:
        return 0.9  # Equivalent to IF(O = L, 0.9, ...)

    elif O < L:
        return (
            0.9 * (O / L) if L != 0 else 0
        )  # Equivalent to IF(O < L, 0.9 * (O / L), ...)

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


def da_super_function(df, i):
    # Check if required columns exist
    required_cols = ["C1", "C2", "C5"]
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"DataFrame must contain these columns: {required_cols}")

    # Initialize results list
    results = []

    if i[1] == "Capacity (Efficiency) (%)":
        # Process each row
        for index, row in df.iterrows():
            # Assuming C1 is K, C2 is L, and C5 is O in your original function
            result = capacity(row["C1"], row["C2"], row["C5"])
            results.append(result)
        # results.append("Capacity (Efficiency) (%)")

    elif i[1] == "Capacity (kW)":
        # Process each row
        for index, row in df.iterrows():
            # Assuming C1 is K, C2 is L, and C5 is O in your original function
            result = capacity(row["C1"], row["C2"], row["C5"])
            results.append(result)
        # results.append("Capacity (kW)")

    elif i[1] == "Capacity (Voltage output)":
        # Process each row
        for index, row in df.iterrows():
            # Assuming C1 is K, C2 is L, and C5 is O in your original function
            result = capacity(row["C1"], row["C2"], row["C5"])
            results.append(result)
        # results.append("Capacity (Voltage output)")

    elif i[1] == "Capability (Response time) (SEC)":
        # Process each row
        for index, row in df.iterrows():
            # Assuming C1 is K, C2 is L, and C5 is O in your original function
            result = capability_response_time(row["C1"], row["C2"], row["C5"])
            results.append(result)
        # results.append("Capability (Response time) (SEC)")

    elif i[1] == "Reliability (%)":
        # Process each row
        for index, row in df.iterrows():
            # Assuming C1 is K, C2 is L, and C5 is O in your original function
            result = reliability(row["C1"], row["C2"], row["C5"])
            results.append(result)
        # results.append("Reliability (%)")

    elif (
        i[1]
        == "Operational Availability (Total time available/ Total time available + Downtime OR simply availability) (%)"
    ):
        # Process each row
        for index, row in df.iterrows():
            # Assuming C1 is K, C2 is L, and C5 is O in your original function
            result = operational_availability_util(row["C1"], row["C2"], row["C5"])
            results.append(result)
        # results.append("Operational Availability (Total time available/ Total time available + Downtime OR simply availability) (%)")

    elif (
        i[1]
        == "Operational Maintainability (In how many hours the system is brought to ideal state) (Hours)"
    ):
        # Process each row
        for index, row in df.iterrows():
            # Assuming C1 is K, C2 is L, and C5 is O in your original function
            result = operational_maintainability_util(row["C1"], row["C2"], row["C5"])
            results.append(result)
        # results.append("Operational Maintainability (In how many hours the system is brought to ideal state) (Hours)")

    elif i[1] == "Safety (Mission completion safety)":
        # Process each row
        for index, row in df.iterrows():
            # Assuming C1 is K, C2 is L, and C5 is O in your original function
            result = mission_completion_safety_util(row["C1"], row["C2"], row["C5"])
            results.append(result)
        # results.append("Safety (Mission completion safety)")

    elif i[1] == "Safety (Human safety) (Hazard related)":
        # Process each row
        for index, row in df.iterrows():
            # Assuming C1 is K, C2 is L, and C5 is O in your original function
            result = human_safety_util(row["C1"], row["C2"], row["C5"])
            results.append(result)
        # results.append("Safety (Human safety) (Hazard related)")

    elif i[1] == "Safety (Operational Environment)":
        # Process each row
        for index, row in df.iterrows():
            # Assuming C1 is K, C2 is L, and C5 is O in your original function
            result = operational_environment_util(row["C1"], row["C2"], row["C5"])
            results.append(result)
        # results.append("Safety (Operational Environment)")

    elif i[1] == "Maintenance (Pending MAJOR defects)":
        # Process each row
        for index, row in df.iterrows():
            # Assuming C1 is K, C2 is L, and C5 is O in your original function
            result = Pending_major_defects_util(row["C1"], row["C2"], row["C5"])
            results.append(result)
        # results.append("Maintenance (Pending MAJOR defects)")

    elif i[1] == "Maintenance (Pending preventive maintenance)":
        # Process each row
        for index, row in df.iterrows():
            # Assuming C1 is K, C2 is L, and C5 is O in your original function
            result = Pending_preventive_maintenance_util(
                row["C1"], row["C2"], row["C5"]
            )
            results.append(result)
        # results.append("Maintenance (Pending preventive maintenance)")

    elif i[1] == "Allowable Utilisation Factor (For equal utilisation of equipment)":
        # Process each row
        for index, row in df.iterrows():
            # Assuming C1 is K, C2 is L, and C5 is O in your original function
            result = allowable_utilisation_factor_util(row["C1"], row["C2"], row["C5"])
            results.append(result)
        # results.append("Allowable Utilisation Factor (For equal utilisation of equipment)")
    print(df)
    print("probabs", results)
    return results
