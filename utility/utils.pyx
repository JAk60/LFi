# cython: language_level=3
# cython: boundscheck=False
# cython: wraparound=False
# cython: cdivision=True

import os
import numpy as np
cimport numpy as np
import pandas as pd
from itertools import permutations
import logging
from libc.math cimport sqrt
import pyodbc
from .Equipment.cython_utils import gt
from .Equipment.cython_utils import da
from .Equipment.cython_utils import ac
from .Equipment.cython_utils import srgm
from .Equipment.cython_utils import vessel
from .cython_utils.permanent import process_matrices

# Type definitions
ctypedef np.float64_t DTYPE_t
np.import_array()

cdef class DependabilityCalculator:
    """Calculator for system dependability metrics"""

    cdef public str mode
    cdef object _dotenv_loaded
    cdef object logger
    cdef object cursor
    cdef object cnxn

    def __cinit__(self):
        """Initialize database connection"""
        try:
            self.cnxn = pyodbc.connect(
                driver="{ODBC Driver 18 for SQL Server}",
                server="localhost",
                database="Utility",
                uid="sa",
                pwd="Camlab110",
                port=1433,
                TrustServerCertificate="yes",
            )
            self.cursor = self.cnxn.cursor()
        except pyodbc.Error as e:
            self.logger.critical(f"Database connection error: {e}")
            raise

    def __init__(self, str log_file="dependability_log.log"):
        """Initialize the calculator with logging configuration"""
        from dotenv import load_dotenv
        self._dotenv_loaded = load_dotenv()
        self.mode = os.getenv("MODE", "PROD").upper()
        self.logger = logging.getLogger(__name__)
        self.setup_logger(log_file)

    def __dealloc__(self):
        """Clean up database connection"""
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'cnxn') and self.cnxn:
            self.cnxn.close()

    cpdef void setup_logger(self, str log_file):
        """Set up logging configuration"""
        self.logger.handlers = []
        file_handler = logging.FileHandler(log_file)
        log_level = logging.INFO if self.mode == "DEV" else logging.CRITICAL
        self.logger.setLevel(log_level)
        file_handler.setLevel(log_level)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    cpdef void log_and_print(self, str message):
        """Log message and optionally print it in DEV mode"""
        if self.mode == "DEV":
            print(message)
        self.logger.info(message)

    cpdef dict get_kn_data(self):
        """Get K-N configuration data for different phases and equipment"""
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

    cpdef double filter_probabilities_for_phase(self, x, list probabilities, str phase, str equipment) except? -1:
        """Filter probabilities based on phase and equipment type"""
        cdef dict kn_data = self.get_kn_data()
        cdef dict phase_data = kn_data.get(phase, {}).get(equipment, {})

        if not phase_data:
            return 0.0

        cdef list s_values = phase_data.get("S", [])
        cdef list utility_all = [
            prob
            for prob, idx in zip(probabilities, range(len(probabilities)))
            if idx + 1 in s_values
        ]

        if not utility_all:
            return 0.0

        return min(utility_all)

    cpdef object process_turbine_data(self, object row):
        """Process turbine data and create DataFrame"""
        # Convert pyodbc.Row to tuple
        data_tuple = tuple(row)
        
        # Extract and convert values
        cdef list c1_values = [float(x) for x in data_tuple[5].split(",")]
        cdef list c5_values = [float(x) for x in data_tuple[6].split(",")]
        cdef dict df_dict = {"C1": c1_values, "C5": c5_values}

        # Process ammunition types
        if data_tuple[1] == "Capability (Ammunition types)":
            if data_tuple[7] == 3:
                df_dict["C2"] = [2]
                df_dict["C3"] = [2]
                df_dict["C4"] = [1]

        # Process fuel acceptance
        elif data_tuple[1] == "Capability (Multiple fuel acceptance) (%)":
            if data_tuple[7] == 1:
                df_dict.update({
                    "C2": [0.05] * 4,
                    "C3": [0.05] * 4,
                    "C4": [0.05] * 4
                })
            elif data_tuple[7] == 2:
                df_dict.update({
                    "C2": [0.5] * 4,
                    "C3": [0.5] * 4,
                    "C4": [0.5] * 4
                })
            elif data_tuple[7] == 3:
                df_dict.update({
                    "C2": [0.4, 0.4, 0.3, 0.3],
                    "C3": [0.4, 0.4, 0.3, 0.3],
                    "C4": [0.4, 0.4, 0.3, 0.3]
                })

        # Process maintenance data
        elif data_tuple[1] in ["Maintenance (Pending MAJOR defects)",
                             "Maintenance (Pending preventive maintenance)"]:
            if data_tuple[7] in [1, 3]:
                df_dict.update({
                    "C2": [x + 1 for x in c1_values],
                    "C3": [x + 2 for x in c1_values],
                    "C4": [x + 3 for x in c1_values]
                })
            elif data_tuple[7] == 2:
                if data_tuple[1] == "Maintenance (Pending MAJOR defects)":
                    df_dict.update({
                        "C2": [x + 1 for x in c1_values],
                        "C3": [x + 2 for x in c1_values],
                        "C4": [x + 3 for x in c1_values]
                    })
                else:  # Pending preventive maintenance
                    df_dict.update({
                        "C2": [x + 2 for x in c1_values],
                        "C3": [x + 3 for x in c1_values],
                        "C4": [x + 4 for x in c1_values]
                    })

        # Process multipliers
        if data_tuple[1] != "Capability (Ammunition types)":
            for i, multiplier in enumerate([data_tuple[8], data_tuple[9], data_tuple[10]], 2):
                if multiplier is not None:
                    col_name = f"C{i}"
                    if col_name not in df_dict:
                        df_dict[col_name] = [x * float(multiplier) for x in c1_values]

        return pd.DataFrame(df_dict)


    cpdef list get_row_minimums_nonzero(self, object df):
        """Calculate minimum non-zero values for each row"""
        # Explicitly convert DataFrame to numpy array
        cdef np.ndarray[DTYPE_t, ndim=2] arr = df.to_numpy(dtype=np.float64)
        arr[arr == 0] = float("inf")  # Replace zeros with infinity
        return np.where(arr == float("inf"), 0, np.min(arr, axis=1)).tolist()

    cpdef object normalize_dataframe(self, object df):
        """Normalize DataFrame values by column maximums"""
        # Explicit conversion to numpy array
        cdef np.ndarray[DTYPE_t, ndim=2] arr = df.to_numpy(dtype=np.float64)
        cdef np.ndarray[DTYPE_t, ndim=1] max_values = np.maximum(np.max(arr, axis=0), 1e-10)
        return pd.DataFrame(arr / max_values, index=df.index, columns=df.columns)

    cpdef np.ndarray[DTYPE_t, ndim=1] normalize_permanents(self, list permanents):
        """Normalize permanent values"""
        cdef np.ndarray[DTYPE_t, ndim=1] permanents_array = np.array(permanents, dtype=np.float64)
        cdef double total = np.sum(permanents_array)
        return permanents_array / total if total > 0 else permanents_array

    cpdef list multiply_lists(self, list list1, list list2):
        """Multiply corresponding elements of two lists"""
        if len(list1) != len(list2):
            raise ValueError("Lists must have same length")
        return [x * y for x, y in zip(list1, list2)]


    cpdef object create_importance_matrix(self):
        """Create importance matrix for calculations"""
        data = {
            "Capacity": [0, 0.6, 0.4, 0.5, 0.2, 0.5, 0.4, 0.1, 0.1, 0.1],
            "Capability": [0.4, 0, 0.3, 0.3, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1],
            "Reliability": [0.6, 0.7, 0, 0.6, 0.3, 0.6, 0.5, 0.1, 0.1, 0.1],
            "Op. Availability": [0.5, 0.7, 0.4, 0, 0.3, 0.5, 0.4, 0.1, 0.1, 0.1],
            "Op. Maintainability": [0.8, 0.8, 0.7, 0.7, 0, 0.7, 0.7, 0.1, 0.1, 0.1],
            "Safety": [0.5, 0.8, 0.4, 0.5, 0.3, 0, 0.4, 0.1, 0.1, 0.1],
            "Maintenance": [0.6, 0.8, 0.5, 0.6, 0.3, 0.6, 0, 0.1, 0.1, 0.1],
            "Stealth": [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0, 0.7, 0.7],
            "Non Vulnerability": [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.3, 0, 0.5],
            "Recoverability": [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.3, 0.5, 0],
        }

        index = [
            "Capacity", "Capability", "Reliability", "Op. Availability",
            "Op. Maintainability", "Safety", "Maintenance", "Stealth",
            "Non Vulnerability", "Recoverability"
        ]

        # Convert to a Pandas DataFrame
        return pd.DataFrame(data, index=index, dtype=np.float64)  # Ensure all values are numeric


    cpdef object process_equipment_df(self, object df):
        """Process equipment DataFrame and calculate grouped values"""
        columns = [
            "Capacity", "Capability", "Reliability", "Op. Availability",
            "Op. Maintainability", "Safety", "Maintenance", "Stealth",
            "Non Vulnerability", "Recoverability"
        ]
        cdef object result_df = pd.DataFrame(columns=columns, index=df.index)

        for idx in df.index:
            row = df.loc[idx]
            grouped_values = []

            if idx == "Gas Turbine":
                grouped_values = [
                    min(row[["N1", "N2", "N3"]]),
                    min(row[["N4", "N5", "N6"]]),
                    row["N7"], row["N8"], row["N9"],
                    min(row[["N10", "N11", "N12"]]),
                    min(row[["N13", "N14", "N15"]])
                ]
            elif idx == "Diesel Engine":
                grouped_values = [
                    min(row[["N1", "N2", "N3"]]),
                    row["N4"], row["N5"], row["N6"], row["N7"],
                    min(row[["N8", "N9", "N10"]]),
                    min(row[["N11", "N12", "N13"]])
                ]
            elif idx == "AC":
                grouped_values = [
                    row["N1"], row["N2"], row["N3"], row["N4"], row["N5"],
                    min(row[["N6", "N7", "N8"]]),
                    min(row[["N9", "N10", "N11"]])
                ]
            elif idx == "SRGM":
                grouped_values = [
                    min(row[["N1", "N2", "N3"]]),
                    min(row[["N4", "N5", "N6", "N7"]]),
                    row["N8"], row["N9"], row["N10"],
                    min(row[["N11", "N12", "N13"]]),
                    min(row[["N14", "N15", "N16"]])
                ]
            elif idx == "VESSEL":
                grouped_values = [
                    min(row[["N1", "N2"]]),
                    min(row[["N3", "N4", "N5", "N6"]]),
                    row["N7"], row["N8"], row["N9"],
                    min(row[["N10", "N11", "N12"]]),
                    min(row[["N13", "N14", "N15"]]),
                    min(row[["N16", "N17", "N18"]]),
                    row["N19"],
                    row["N20"]
                ]

            # Pad with zeros to ensure 10 columns
            grouped_values += [0] * (10 - len(grouped_values))
            result_df.loc[idx] = grouped_values

        return result_df

    def normalize_dataframe(self,np.ndarray[np.float64_t, ndim=2] df):
        """
        Normalizes a 2D NumPy array by dividing each column by its maximum value.
        Columns with a max value of 0 remain unchanged.

        Args:
            df (np.ndarray): Input 2D NumPy array to be normalized.

        Returns:
            np.ndarray: Normalized NumPy array.
        """
        cdef int rows = df.shape[0]
        cdef int cols = df.shape[1]
        cdef np.ndarray[np.float64_t, ndim=1] max_values = np.max(df, axis=0)
        cdef np.ndarray[np.float64_t, ndim=2] normalized_df = np.empty_like(df)

        cdef int i, j
        for j in range(cols):
            if max_values[j] != 0:
                for i in range(rows):
                    normalized_df[i, j] = df[i, j] / max_values[j]
            else:
                for i in range(rows):
                    normalized_df[i, j] = df[i, j]  # Keep original values

        return normalized_df

    cpdef object depalgo(self, int phase):
        """Calculate dependability algorithm for given phase"""
        import pyodbc
        import pandas as pd

        cdef list equipment_types = ["Gas Turbine", "Diesel Engine", "AC", "SRGM", "VESSEL"]
        cdef dict all_n_values = {equipment: [] for equipment in equipment_types}
        cdef tuple phases = ((1, "Harbour"), (2, "Cruise"), (3, "Action"))
        cdef str selected_phase = ""

        for num, name in phases:
            if num == phase:
                selected_phase = name
                break

        if not selected_phase:
            raise ValueError(f"Invalid phase ID: {phase}")

        print(f"Selected phase: {selected_phase}")  # Debugging

        for equipment_type in equipment_types:
            try:
                print(f"Processing {equipment_type}")  # Debugging

                self.cursor.execute("""
                    SELECT * FROM Parameter
                    WHERE EquipmentName=? AND PhaseID=?
                """, (equipment_type, phase))

                parameters = self.cursor.fetchall()
                print(f"Fetched {len(parameters)} records for {equipment_type}")  # Debugging

                if not parameters:
                    self.log_and_print(f"No parameters found for {equipment_type} in phase {selected_phase}.")
                    continue  # Skip to next equipment

                for param in parameters:
                    v = self.process_turbine_data(param)
                    c = []
                    N = None

                    try:
                        if equipment_type == "Gas Turbine":
                            c = gt.gt_super_function(v, tuple(param))
                            N = self.filter_probabilities_for_phase(param[1], c, selected_phase, "GT")
                        elif equipment_type == "Diesel Engine":
                            c = da.da_super_function(v, tuple(param))
                            N = self.filter_probabilities_for_phase(param[1], c, selected_phase, "DA")
                        elif equipment_type == "AC":
                            c = ac.ac_super_function(v, tuple(param)).tolist()
                            N = self.filter_probabilities_for_phase(param[1], c, selected_phase, "AC")
                        elif equipment_type == "SRGM":
                            c = srgm.srgm_super_function(v, tuple(param))
                            N = self.filter_probabilities_for_phase(param[1], c, selected_phase, "SRGM")
                        elif equipment_type == "VESSEL":
                            c = vessel.vessel_super_function(v, tuple(param))
                            N = self.filter_probabilities_for_phase(param[1], c, selected_phase, "VESSEL")

                        if N is not None:
                            all_n_values[equipment_type].append(N)
                            self.log_and_print(f"{param[1]} : {equipment_type} with {selected_phase} has Utility: {N}")
                    except Exception as e:
                        print(f"Error in calculations for {equipment_type}: {e}")  # Debugging
                        self.logger.critical(f"Error in calculations for {equipment_type}: {e}")
                        continue  # Skip this iteration if failure occurs
            except pyodbc.Error as e:
                print(f"Database error: {e}")  # Debugging
                self.logger.critical(f"Database query error: {e}")
                raise

        print("Finished processing all equipment")  # Debugging

        # Pad all lists to length 20
        for key in all_n_values:
            all_n_values[key].extend([0] * (20 - len(all_n_values[key])))

        print("wtf")  # Debugging
        df = pd.DataFrame.from_dict(all_n_values, orient='index')
        df.columns = [f"N{i+1}" for i in range(20)]

        self.log_and_print(f"\nPhase {phase} DataFrame:\n{df.to_string()}")
        print("utilities calculated")  # Debugging
        return df

    cpdef tuple calculate_dependability(self):
        """Calculate final dependability values"""
        cdef list phase_wise_weighted_dependability_values = []
        cdef double dep, euclidean_distance, dependability
        cdef int phase
        cdef np.ndarray[DTYPE_t, ndim=2] normalized_matrix_np, importance_matrix_np, result_array
        cdef np.ndarray[DTYPE_t, ndim=1] ideal_vector, phase_values

        for phase in [1,2,3]:
            # Get phase data
            df = self.depalgo(phase)
            print("----->>> depalgo done")
            self.log_and_print(f"Processing phase {phase}")

            # Process equipment data
            result_df = self.process_equipment_df(df)
            print("----->>> process_equipment_df done")
            self.log_and_print(f"Equipment DF for phase {phase}:\n{result_df.to_string()}")
            print("result_df type:", type(result_df))
            print("result_df shape (if available):", getattr(result_df, 'shape', 'No shape attribute'))
            print("Is result_df already a numpy array?:", isinstance(result_df, np.ndarray))
            # Convert to numpy arrays
            result_array = np.asarray(result_df.values, dtype=np.float64)
            print("----->>> result_array done",result_array)
            importance_array = np.asarray(self.create_importance_matrix(), dtype=np.float64)
            # importance_array = self.create_importance_matrix()
            
            print("importance_array created:", importance_array)
            print("importance_array dtype:", importance_array.dtype)
            print("importance_array shape:", importance_array.shape)

            # Normalize importance array
            normalized_matrix_np = self.normalize_dataframe(result_array)
            print("normalized_matrix_np :", normalized_matrix_np)

            # Ensure shape consistency before passing to process_matrices
            #if normalized_matrix_np.shape[1] != importance_array.shape[1]:
               # raise ValueError("Shape mismatch: normalized_matrix_np and importance_array must have the same number of columns.")

            # Process matrices
            print("normalized_matrix_np :", normalized_matrix_np)
            print("normalized_matrix_np :", importance_array.shape)
            normalized = process_matrices(importance_array, normalized_matrix_np, 5)
            print("process_matrices raned :",normalized)

            # Calculate minimum values from the original result array
            #min_mask = result_array == 0
            #result_array[min_mask] = float('inf')  # Temporarily replace zeros with inf
            #minimum_list = np.min(result_array, axis=1).tolist()
            min_values = []
            for row in result_array:
                if np.all(row == 0):  # Check if all elements in the row are zero
                    min_values.append(0.0)  # Or some other default value like NaN
                else:
                    min_values.append(np.min(np.where(row == 0, np.inf, row)))

            minimum_list = min_values 
            print("minimum_list raned :",minimum_list)

            res = self.multiply_lists(minimum_list, normalized)
            dep = sum(res)
            phase_wise_weighted_dependability_values.append(dep)

            self.log_and_print(f"Phase {phase} dependability: {dep}")

        # Calculate final dependability using Euclidean distance
        ideal_vector = np.array([1.0, 1.0, 1.0], dtype=np.float64)
        phase_values = np.array(phase_wise_weighted_dependability_values, dtype=np.float64)

        euclidean_distance = sqrt(np.sum((ideal_vector - phase_values) ** 2))
        dependability = (1.73 - euclidean_distance) / 1.73

        self.log_and_print(f"Final dependability: {dependability}")
        self.log_and_print(f"Phase-wise values: {phase_wise_weighted_dependability_values}")

        return (float(dependability), list(phase_wise_weighted_dependability_values))
