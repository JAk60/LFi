import pandas as pd
import numpy as np
from itertools import permutations


# Normalize the matrix data
def normalize_dataframe(df):
    """
    Normalizes a DataFrame by dividing each column by its maximum value,
    while preserving columns with a maximum value of 0 (keeping them unchanged).

    Args:
    df (pd.DataFrame): The input DataFrame to be normalized.

    Returns:
    pd.DataFrame: A new DataFrame with normalized values.
    """
    # Get the maximum values for each column
    max_values = df.max()

    # Create a copy of the original DataFrame for the normalized values
    normalized_df = df.copy()

    # Normalize only the columns with a non-zero max value
    for col in df.columns:
        if max_values[col] != 0:
            normalized_df[col] = df[col] / max_values[col]
        else:
            normalized_df[col] = df[col]  # Keep the original if max is zero

    return normalized_df


# normalized_matrix = normalize_dataframe(result_df)

# Define the matrix data based on the image
data = {
    "Capacity": ["A1", 0.6, 0.4, 0.5, 0.2, 0.5, 0.4, 0.1, 0.1, 0.1],
    "Capability": [0.4, "A2", 0.3, 0.3, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1],
    "Reliability": [0.6, 0.7, "A3", 0.6, 0.3, 0.6, 0.5, 0.1, 0.1, 0.1],
    "Op. Availability": [0.5, 0.7, 0.4, "A4", 0.3, 0.5, 0.4, 0.1, 0.1, 0.1],
    "Op. Maintainability": [0.8, 0.8, 0.7, 0.7, "A5", 0.7, 0.7, 0.1, 0.1, 0.1],
    "Safety": [0.5, 0.8, 0.4, 0.5, 0.3, "A6", 0.4, 0.1, 0.1, 0.1],
    "Maintenance": [0.6, 0.8, 0.5, 0.6, 0.3, 0.6, "A7", 0.1, 0.1, 0.1],
    "Stealth": [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, "A8", 0.7, 0.7],
    "Non Vulnerability": [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.3, "A9", 0.5],
    "Recoverability": [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.3, 0.5, "A10"],
}

# Define row labels
index = [
    "Capacity",
    "Capability",
    "Reliability",
    "Op. Availability",
    "Op. Maintainability",
    "Safety",
    "Maintenance",
    "Stealth",
    "Non Vulnerability",
    "Recoverability",
]

# Create the DataFrame
importance_matrix = pd.DataFrame(data, index=index)

# Display the DataFrame
print("Importance Matrix:")
print(importance_matrix)


# Calculate the permanent of a matrix
def permanent(matrix):
    n = matrix.shape[0]
    perm = permutations(range(n))
    return sum(np.prod([matrix[i, p[i]] for i in range(n)]) for p in perm)


new_matrices = []
permanents = []

for i in range(5):
    new_matrix = importance_matrix.copy()
    for j in range(10):
        new_matrix.iloc[j, j] = normalized_matrix.iloc[i, j]
    new_matrices.append(new_matrix)

    # Convert DataFrame to numpy array for permanent calculation
    matrix_array = new_matrix.values.astype(float)
    perm = permanent(matrix_array)
    permanents.append(perm)

# Display the new matrices in DataFrame format along with their permanents
for i, (matrix, perm) in enumerate(zip(new_matrices, permanents)):
    print(f"Matrix {i + 1} (using row {normalized_matrix.index[i]}):")
    print(matrix.to_string())
    print(f"\nPermanent of Matrix {i + 1}: {perm}")
    print("\n" + "=" * 50 + "\n")

# permanents.sort()


# Normalize permanents
def normalize_permanents(permanents):
    # Convert to numpy array for easier calculation
    permanents_array = np.array(permanents)

    # Calculate the sum of all permanents
    total = np.sum(permanents_array)

    # Divide each permanent by the total to normalize
    normalized_permanents = permanents_array / total

    return normalized_permanents


# normalized = normalize_permanents(permanents)

# print("Original permanents:", permanents)
# print("Normalized permanents:", normalized)
# print("Sum of normalized permanents:", np.sum(normalized))


import pandas as pd


def get_row_minimums_nonzero(df):
    """
    Function to calculate the minimum value of each row in a DataFrame,
    considering only values greater than 0.

    Args:
    df (pd.DataFrame): Input DataFrame

    Returns:
    list: List of minimum nonzero values for each row
    """
    return df.replace(0, float("inf")).min(axis=1).replace(float("inf"), 0).tolist()


# minimum_list=get_row_minimums_nonzero(result_df)


def multiply_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length")

    return [a * b for a, b in zip(list1, list2)]


# # res = multiply_lists(minimum_list, normalized)
# print(res)  # Output: [5, 12, 21, 32]
# print(sum(res))
