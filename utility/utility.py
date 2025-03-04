import os
from dotenv import load_dotenv
import pandas as pd
import numpy as np
from itertools import permutations
import logging
from math import sqrt
import pyodbc
import random
from .Equipment.cython_utils import gt
from .Equipment.cython_utils import da
from .Equipment.cython_utils import ac
# from .Equipment.ac import ac_super_function
from .Equipment.cython_utils import srgm
from .Equipment.cython_utils import vessel
from .cython_utils.permanent import process_matrices

cnxn = pyodbc.connect(
    driver="{ODBC Driver 18 for SQL Server}",
    server="192.168.109.215",
    database="Utility",
    uid="sa",
    pwd="Camlab110",
    port=1433,
    TrustServerCertificate="yes",
)

cursor = cnxn.cursor()
load_dotenv()
class DependabilityCalculator:
    """Calculator for system dependability metrics"""

    def __init__(self, log_file: str = "dependability_log.log"):
        """Initialize the calculator with logging configuration"""
        self.mode = os.getenv("MODE", "PROD").upper()
        self._setup_logger(log_file)

    def _setup_logger(self, log_file):
        log_level = logging.INFO if self.mode == "DEV" else logging.CRITICAL
        logging.basicConfig(
            filename=log_file,
            level=log_level,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    def get_kn_data(self):
        return {
            "Harbour": {
                "GT": {"k": 4, "N": 4, "S": [1, 2, 3, 4]},
                "DA": {"K": 4, "N": 4, "S": [1, 2, 3, 4]},
                "AC": {"K": 5, "N": 5, "S": [1, 2, 3, 4, 5]},
                "VESSEL": {"K": 1, "N": 1, "S": [1]},
            },
            "Cruise": {
                "GT": {"k": "1+1", "N": 4, "S": [2, 4]},
                "DA": {"K": 3, "N": 4, "S": [1, 2, 3]},
                "AC": {"K": 3, "N": 5, "S": [2, 4, 5]},
                "VESSEL": {"K": 1, "N": 1, "S": [1]},
            },
            "Action": {
                "GT": {"k": 4, "N": 4, "S": [1, 2, 3, 4]},
                "DA": {"K": 4, "N": 4, "S": [1, 2, 3, 4]},
                "AC": {"K": 5, "N": 5, "S": [1, 2, 3, 4, 5]},
                "SRGM": {"K": 1, "N": 1, "S": [1]},
                "VESSEL": {"K": 1, "N": 1, "S": [1]},
            },
        }

    def filter_probabilities_for_phase(self, x, probabilities, phase, equipment):
        print(phase, equipment)
        kn_data = self.get_kn_data()
        phase_data = kn_data.get(phase, {}).get(equipment, {})
        print(phase_data)

        if not phase_data:
            return []  # Return empty list if phase not found

        s_values = phase_data.get("S", [])
        print(probabilities)
        # Filter probabilities based on indices from S values
        utility_all = [
            prob
            for prob, idx in zip(probabilities, range(len(probabilities)))
            if idx + 1 in s_values
        ]
        utility = 0
        if utility_all:
            utility = min(utility_all)
        print("-------------->>>>", x, utility, utility_all)
        return utility

    def log_and_print(self, message):
        if self.mode == "DEV":
            print(message)
            logging.info(message)

    def process_turbine_data(self, data_tuple):
        # 'Maintenance (Pending MAJOR defects)'
        # 'Maintenance (Pending preventive maintenance)'
        # 'Capability (Multiple fuel acceptance) (%)'
        # Extract the string of values and convert to list
        c1_values = [float(x) for x in data_tuple[5].split(",")]
        c5_values = [float(x) for x in data_tuple[6].split(",")]

        # Randomize C5 values by ±10%
        c5_values = [x + x * (random.uniform(-0.1, 0.1)) for x in c5_values]

        # Initialize DataFrame with C1 and C5
        df_dict = {"C1": c1_values}

        if data_tuple[1] == "Capability (Ammunition types)":
            if data_tuple[7] == 3:
                df_dict["C2"] = [2]
                df_dict["C3"] = [2]
                df_dict["C4"] = [1]
            pass

        if data_tuple[1] == "Capability (Multiple fuel acceptance) (%)":
            print("it entered")
            if data_tuple[7] == 1:
                df_dict["C2"] = [0.05, 0.05, 0.05, 0.05]
                df_dict["C3"] = [0.05, 0.05, 0.05, 0.05]
                df_dict["C4"] = [0.05, 0.05, 0.05, 0.05]
            elif data_tuple[7] == 2:
                df_dict["C2"] = [0.5, 0.5, 0.5, 0.5]
                df_dict["C3"] = [0.5, 0.5, 0.5, 0.5]
                df_dict["C4"] = [0.5, 0.5, 0.5, 0.5]
            elif data_tuple[7] == 3:
                df_dict["C2"] = [0.4, 0.4, 0.3, 0.3]
                df_dict["C3"] = [0.4, 0.4, 0.3, 0.3]
                df_dict["C4"] = [0.4, 0.4, 0.3, 0.3]

        if data_tuple[1] in [
            "Maintenance (Pending MAJOR defects)",
            "Maintenance (Pending preventive maintenance)",
        ] and (data_tuple[7] == 1 or data_tuple[7] == 3):
            # Add 1 to each element of C1 to create C2
            df_dict["C2"] = [x + 1 for x in c1_values]
            df_dict["C3"] = [x + 2 for x in c1_values]
            df_dict["C4"] = [x + 3 for x in c1_values]
        elif data_tuple[1] == "Maintenance (Pending MAJOR defects)" and data_tuple[7] == 2:
            df_dict["C2"] = [x + 1 for x in c1_values]
            df_dict["C3"] = [x + 2 for x in c1_values]
            df_dict["C4"] = [x + 3 for x in c1_values]
        elif data_tuple[1] == "Maintenance (Pending preventive maintenance)" and (
            data_tuple[7] == 1 or data_tuple[7] == 2
        ):
            df_dict["C2"] = [x + 2 for x in c1_values]
            df_dict["C3"] = [x + 3 for x in c1_values]
            df_dict["C4"] = [x + 4 for x in c1_values]

        # Only add columns for non-None multipliers
        if data_tuple[8] is not None and data_tuple[1] != "Capability (Ammunition types)":
            multiplier_c2 = float(data_tuple[8])
            df_dict["C2"] = [x * multiplier_c2 for x in c1_values]

        if data_tuple[9] is not None and data_tuple[1] != "Capability (Ammunition types)":
            multiplier_c3 = float(data_tuple[9])
            df_dict["C3"] = [x * multiplier_c3 for x in c1_values]

        if data_tuple[10] is not None and data_tuple[1] != "Capability (Ammunition types)":
            multiplier_c4 = float(data_tuple[10])
            df_dict["C4"] = [x * multiplier_c4 for x in c1_values]

        df_dict["C5"] = c5_values
        # Create DataFrame
        df = pd.DataFrame(df_dict)
        return df

    def get_row_minimums_nonzero(self, df):
        """
        Function to calculate the minimum value of each row in a DataFrame,
        considering only values greater than 0.

        Args:
        df (pd.DataFrame): Input DataFrame

        Returns:
        list: List of minimum nonzero values for each row
        """
        return df.replace(0, float("inf")).min(axis=1).replace(float("inf"), 0).tolist()

    def normalize_dataframe(self, df):
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

    def normalize_permanents(self, permanents):
        # Convert to numpy array for easier calculation
        permanents_array = np.array(permanents)

        # Calculate the sum of all permanents
        total = np.sum(permanents_array)

        # Divide each permanent by the total to normalize
        normalized_permanents = permanents_array / total

        return normalized_permanents

    def multiply_lists(self, list1, list2):
        if len(list1) != len(list2):
            raise ValueError("Both lists must have the same length")

        return [a * b for a, b in zip(list1, list2)]

    def create_importance_matrix(self):
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

        return pd.DataFrame(data, index=index)

    # def process_matrices(self, importance_matrix, normalized_matrix, num_matrices=5):
    #     def permanent(matrix):
    #         n = matrix.shape[0]
    #         perm = permutations(range(n))
    #         return sum(np.prod([matrix[i, p[i]] for i in range(n)]) for p in perm)

    #     new_matrices = []
    #     permanents = []

    #     for i in range(num_matrices):
    #         new_matrix = importance_matrix.copy()
    #         for j in range(10):
    #             new_matrix.iloc[j, j] = normalized_matrix.iloc[i, j]
    #         new_matrices.append(new_matrix)

    #         matrix_array = new_matrix.values.astype(float)
    #         permanents.append(permanent(matrix_array))

    #     normalized = np.array(permanents)
    #     normalized = (
    #         normalized / np.sum(normalized) if np.sum(normalized) != 0 else normalized
    #     )
    #     return normalized

    def process_equipment_df(self, df):
        """
        Process DataFrame to calculate minimums of specific groups for different equipment types.
        Returns a new DataFrame with exactly 5 rows and 10 columns (filled with 0 if needed).
        """
        columns = [
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
        # Define the fixed structure for result_df
        result_df = pd.DataFrame(columns=columns, index=df.index)

        for idx in df.index:
            row = df.loc[idx]
            grouped_values = []

            if idx == "Gas Turbine":
                grouped_values = [
                    min(row[["N1", "N2", "N3"]]),
                    min(row[["N4", "N5", "N6"]]),
                    row["N7"],
                    row["N8"],
                    row["N9"],
                    min(row[["N10", "N11", "N12"]]),
                    min(row[["N13", "N14", "N15"]]),
                ]

            elif idx == "Diesel Engine":
                grouped_values = [
                    min(row[["N1", "N2", "N3"]]),
                    row["N4"],
                    row["N5"],
                    row["N6"],
                    row["N7"],
                    min(row[["N8", "N9", "N10"]]),
                    min(row[["N11", "N12", "N13"]]),
                ]

            elif idx == "AC":
                grouped_values = [
                    row["N1"],
                    row["N2"],
                    row["N3"],
                    row["N4"],
                    row["N5"],
                    min(row[["N6", "N7", "N8"]]),
                    min(row[["N9", "N10", "N11"]]),
                ]

            elif idx == "SRGM":
                grouped_values = [
                    min(row[["N1", "N2", "N3"]]),
                    min(row[["N4", "N5", "N6", "N7"]]),
                    row["N8"],
                    row["N9"],
                    row["N10"],
                    min(row[["N11", "N12", "N13"]]),
                    min(row[["N14", "N15", "N16"]]),
                ]

            elif idx == "VESSEL":
                grouped_values = [
                    min(row[["N1", "N2"]]),
                    min(row[["N3", "N4", "N5", "N6"]]),
                    row["N7"],
                    row["N8"],
                    row["N9"],
                    min(row[["N10", "N11", "N12"]]),
                    min(row[["N13", "N14", "N15"]]),
                    min(row[["N16", "N17", "N18"]]),
                    row["N19"],
                    row["N20"],
                ]

            # Fill remaining values with 0 to ensure exactly 10 columns
            grouped_values += [0] * (10 - len(grouped_values))

            # Assign values to result DataFrame
            result_df.loc[idx] = grouped_values
        return result_df

    def depalgo(self, phase):
        # Initialize the DataFrame with specific equipment types
        equipment_types = ["Gas Turbine", "Diesel Engine", "AC", "SRGM", "VESSEL"]

        # Dictionary to store all N_values for each equipment
        all_n_values = {equipment: [] for equipment in equipment_types}

        # Define phases as a tuple
        phases = ((1, "Harbour"), (2, "Cruise"), (3, "Action"))

        # Get the phase name from the phase number
        selected_phase = next(name for num, name in phases if num == phase)

        # Process each equipment type separately
        for equipment_type in equipment_types:
            # Get parameters for this specific equipment
            query = """SELECT * FROM Parameter WHERE EquipmentName=? AND PhaseID=?"""
            cursor.execute(query, (equipment_type, phase))
            parameters = cursor.fetchall()

            for param in parameters:
                v = self.process_turbine_data(param)
                c = []

                # Process based on equipment type
                if equipment_type == "Gas Turbine":
                    c = gt.gt_super_function(v, param)
                    N = self.filter_probabilities_for_phase(param[1], c, selected_phase, "GT")
                elif equipment_type == "Diesel Engine":
                    c = da.da_super_function(v, param)
                    N = self.filter_probabilities_for_phase(param[1], c, selected_phase, "DA")
                elif equipment_type == "AC":
                    c = ac.ac_super_function(v, param)
                    N = self.filter_probabilities_for_phase(param[1], c, selected_phase, "AC")
                elif equipment_type == "SRGM":
                    c = srgm.srgm_super_function(v, param)
                    N = self.filter_probabilities_for_phase(param[1], c, selected_phase, "SRGM")
                elif equipment_type == "VESSEL":
                    c = vessel.vessel_super_function(v, param)
                    N = self.filter_probabilities_for_phase(
                        param[1], c, selected_phase, "VESSEL"
                    )

                if N is not None:
                    all_n_values[equipment_type].append(N)
                    logging.info(
                        f"{param[1]} : {equipment_type} with {selected_phase} has Utility: {N}"
                    )

        # Ensure all lists have exactly 20 elements, filling missing ones with 0
        for key in all_n_values:
            all_n_values[key] = all_n_values[key] + [0] * (20 - len(all_n_values[key]))

        # Convert dictionary to DataFrame (transpose to get 20 columns)
        df = pd.DataFrame.from_dict(all_n_values, orient="index")

        # Ensure DataFrame has 20 columns
        df = df.iloc[:, :20]  # Trim if extra
        while df.shape[1] < 20:
            df[df.shape[1]] = 0  # Add missing columns

        # Rename columns as N1, N2, ..., N20
        df.columns = [f"N{i + 1}" for i in range(0, 20)]

        # Log final DataFrame
        logging.info("\nFinal DataFrame:")
        logging.info("\n" + df.to_string())

        return df

    def calculate_dependability(self):
        phase_wise_weighted_dependability_values = []
        for phase in [1, 2, 3]:
            df = self.depalgo(phase)  # Get the 20-column DataFrames
            # self.log_and_print(f"Phase {phase} - Original DataFrame:\n{df}")

            result_df = self.process_equipment_df(df)  # Process it using grouping logic
            # self.log_and_print(f"\nProcessed DataFrame with minimums:\n{result_df}")

            normalized_matrix = self.normalize_dataframe(result_df) #(5,10)
            importance_matrix = self.create_importance_matrix() #(10,10)
            # self.log_and_print(f"Importance Matrix: {importance_matrix}")

            normalized = process_matrices(importance_matrix, normalized_matrix,num_matrices=5)
            # self.log_and_print(f"Normalized permanents: {normalized}")
            # self.log_and_print(f"Sum of normalized permanents: {np.sum(normalized)}")

            minimum_list = self.get_row_minimums_nonzero(result_df)
            # self.log_and_print(f"minimum_list: {minimum_list}")
            res = self.multiply_lists(minimum_list, normalized)
            # self.log_and_print(f"Multiplication Result: {res}")

            dep = sum(res)
            # self.log_and_print(f"Phase {phase} Dependability: {dep}")

            phase_wise_weighted_dependability_values.append(dep)
            ideal_vector = [1, 1, 1]
            # self.log_and_print(
            #     f"Updated phase-wise weighted dependability values: {phase_wise_weighted_dependability_values}"
            # )
            euclidean_distance = sqrt(
                sum(
                    (i - j) ** 2
                    for i, j in zip(ideal_vector, phase_wise_weighted_dependability_values)
                )
            )
            dependability = (1.73 - euclidean_distance) / 1.73
        return dependability ,phase_wise_weighted_dependability_values

# Example usage
if __name__ == "__main__":
    calculator = DependabilityCalculator()
    print("Final dependability:", calculator.calculate_dependability())
