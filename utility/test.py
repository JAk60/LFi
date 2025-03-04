from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional, Union
import pandas as pd
import numpy as np
from itertools import permutations
from math import sqrt
import logging
from pathlib import Path




@dataclass
class EquipmentData:
    """Data structure for equipment configuration"""
    k: Union[int, str]
    N: int
    S: List[int]


@dataclass
class PhaseConfig:
    """Configuration data for a specific phase"""
    GT: Optional[EquipmentData] = None
    DA: Optional[EquipmentData] = None
    AC: Optional[EquipmentData] = None
    VESSEL: Optional[EquipmentData] = None
    SRGM: Optional[EquipmentData] = None


class DependabilityCalculator:
    """Calculator for system dependability metrics"""
    
    def __init__(self, log_file: str = "dependability_log.log"):
        """Initialize the calculator with logging configuration"""
        self._setup_logger(log_file)
        self.phase_config = self._initialize_phase_config()
        self.equipment_types = ["Gas Turbine", "Diesel Engine", "AC", "SRGM", "VESSEL"]
        self.phases = [(1, "Harbour"), (2, "Cruise"), (3, "Action")]

    def _setup_logger(self, log_file: str) -> None:
        """Configure logging settings"""
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            filemode="w"
        )

    def _initialize_phase_config(self) -> Dict[str, PhaseConfig]:
        """Initialize phase configuration data"""
        return {
            "Harbour": PhaseConfig(
                GT=EquipmentData(k=4, N=4, S=[1, 2, 3, 4]),
                DA=EquipmentData(k=4, N=4, S=[1, 2, 3, 4]),
                AC=EquipmentData(k=5, N=5, S=[1, 2, 3, 4, 5]),
                VESSEL=EquipmentData(k=1, N=1, S=[1])
            ),
            "Cruise": PhaseConfig(
                GT=EquipmentData(k="1+1", N=4, S=[2, 4]),
                DA=EquipmentData(k=3, N=4, S=[1, 2, 3]),
                AC=EquipmentData(k=3, N=5, S=[2, 4, 5]),
                VESSEL=EquipmentData(k=1, N=1, S=[1])
            ),
            "Action": PhaseConfig(
                GT=EquipmentData(k=4, N=4, S=[1, 2, 3, 4]),
                DA=EquipmentData(k=4, N=4, S=[1, 2, 3, 4]),
                AC=EquipmentData(k=5, N=5, S=[1, 2, 3, 4, 5]),
                SRGM=EquipmentData(k=1, N=1, S=[1]),
                VESSEL=EquipmentData(k=1, N=1, S=[1])
            )
        }

    def log_and_print(self, message: str) -> None:
        """Log and print a message"""
        print(message)
        logging.info(message)

    @staticmethod
    def process_turbine_data(self,data_tuple: Tuple) -> pd.DataFrame:
        """Process turbine data and return a DataFrame"""
        c1_values = [float(x) for x in data_tuple[5].split(",")]
        c5_values = [float(x) for x in data_tuple[6].split(",")]
        df_dict = {"C1": c1_values, "C5": c5_values}

        # Process different capability types
        if data_tuple[1] == "Capability (Ammunition types)":
            if data_tuple[7] == 3:
                df_dict.update({"C2": [2], "C3": [2], "C4": [1]})

        elif data_tuple[1] == "Capability (Multiple fuel acceptance) (%)":
            fuel_values = {
                1: [0.05] * 4,
                2: [0.5] * 4,
                3: [0.4, 0.4, 0.3, 0.3]
            }
            if data_tuple[7] in fuel_values:
                value = fuel_values[data_tuple[7]]
                df_dict.update({f"C{i}": value for i in range(2, 5)})

        # Process maintenance types
        elif data_tuple[1] in ["Maintenance (Pending MAJOR defects)", 
                             "Maintenance (Pending preventive maintenance)"]:
            self._process_maintenance_data(data_tuple, c1_values, df_dict)

        # Apply multipliers
        self._apply_multipliers(data_tuple, df_dict)

        return pd.DataFrame(df_dict)
    def _get_phase_data(self, phase):
        """
        Retrieve and format phase-specific data.
        
        Args:
            phase (int): Phase number (1: Harbour, 2: Cruise, 3: Action)
        
        Returns:
            pd.DataFrame: DataFrame with 20 columns of equipment data
        """
        # Initialize equipment types
        equipment_types = ["Gas Turbine", "Diesel Engine", "AC", "SRGM", "VESSEL"]
        all_n_values = {equipment: [] for equipment in equipment_types}
        
        # Map phase numbers to names
        phase_names = {1: "Harbour", 2: "Cruise", 3: "Action"}
        selected_phase = phase_names[phase]
        
        # Create DataFrame with equipment types as index
        df = pd.DataFrame(
            index=equipment_types,
            columns=[f"N{i+1}" for i in range(20)],
            data=0  # Initialize with zeros
        )
        
        return df

    @staticmethod
    def _process_matrices(importance_matrix: pd.DataFrame, 
                        normalized_matrix: pd.DataFrame, 
                        num_matrices: int = 5) -> np.ndarray:
        """
        Process matrices and calculate permanents.
        
        Args:
            importance_matrix: Base importance matrix
            normalized_matrix: Normalized data matrix
            num_matrices: Number of matrices to process
            
        Returns:
            np.ndarray: Normalized permanent values
        """
        def permanent(matrix: np.ndarray) -> float:
            n = matrix.shape[0]
            perm = permutations(range(n))
            return sum(np.prod([matrix[i, p[i]] for i in range(n)]) for p in perm)

        permanents = []
        for i in range(num_matrices):
            new_matrix = importance_matrix.copy()
            for j in range(10):
                new_matrix.iloc[j, j] = normalized_matrix.iloc[i, j]
            matrix_array = new_matrix.values.astype(float)
            permanents.append(permanent(matrix_array))

        normalized = np.array(permanents)
        return normalized / np.sum(normalized) if np.sum(normalized) != 0 else normalized

    def _process_equipment_df(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Process equipment DataFrame with specific grouping logic.
        
        Args:
            df: Input DataFrame with equipment data
            
        Returns:
            pd.DataFrame: Processed DataFrame with calculated values
        """
        columns = [
            "Capacity", "Capability", "Reliability", "Op. Availability",
            "Op. Maintainability", "Safety", "Maintenance", "Stealth",
            "Non Vulnerability", "Recoverability"
        ]
        
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
                    min(row[["N13", "N14", "N15"]])
                ]
            
            elif idx == "Diesel Engine":
                grouped_values = [
                    min(row[["N1", "N2", "N3"]]),
                    row["N4"],
                    row["N5"],
                    row["N6"],
                    row["N7"],
                    min(row[["N8", "N9", "N10"]]),
                    min(row[["N11", "N12", "N13"]])
                ]
            
            elif idx == "AC":
                grouped_values = [
                    row["N1"],
                    row["N2"],
                    row["N3"],
                    row["N4"],
                    row["N5"],
                    min(row[["N6", "N7", "N8"]]),
                    min(row[["N9", "N10", "N11"]])
                ]
            
            elif idx == "SRGM":
                grouped_values = [
                    min(row[["N1", "N2", "N3"]]),
                    min(row[["N4", "N5", "N6", "N7"]]),
                    row["N8"],
                    row["N9"],
                    row["N10"],
                    min(row[["N11", "N12", "N13"]]),
                    min(row[["N14", "N15", "N16"]])
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
                    row["N20"]
                ]
            
            # Fill remaining values with 0 to ensure exactly 10 columns
            grouped_values += [0] * (10 - len(grouped_values))
            result_df.loc[idx] = grouped_values
        
        return result_df

    @staticmethod
    def _create_importance_matrix() -> pd.DataFrame:
        """
        Create the importance matrix for calculations.
        
        Returns:
            pd.DataFrame: Importance matrix with predefined values
        """
        columns = [
            "Capacity", "Capability", "Reliability", "Op. Availability",
            "Op. Maintainability", "Safety", "Maintenance", "Stealth",
            "Non Vulnerability", "Recoverability"
        ]
        
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
            "Recoverability": [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.3, 0.5, "A10"]
        }
        
        return pd.DataFrame(data, index=columns)

    def filter_probabilities_for_phase(self, x: str, probabilities: List[float], 
                                    phase: str, equipment: str) -> float:
        """
        Filter probabilities based on phase and equipment data.
        
        Args:
            x: Parameter identifier
            probabilities: List of probability values
            phase: Phase name
            equipment: Equipment type
            
        Returns:
            float: Filtered utility value
        """
        self.log_and_print(f"{phase} {equipment}")
        phase_config = self.phase_config.get(phase, PhaseConfig())
        equipment_data = getattr(phase_config, equipment, None)
        
        if not equipment_data:
            return 0
        
        self.log_and_print(str(equipment_data))
        self.log_and_print(str(probabilities))
        
        utility_all = [
            prob
            for prob, idx in zip(probabilities, range(len(probabilities)))
            if idx + 1 in equipment_data.S
        ]
        
        utility = min(utility_all) if utility_all else 0
        self.log_and_print(f"-------------->>>> {x} {utility} {utility_all}")
        return utility

    def depalgo(self, phase: int, cursor) -> pd.DataFrame:
        """
        Calculate dependability algorithm for a specific phase.
        
        Args:
            phase: Phase number
            cursor: Database cursor for fetching parameters
            
        Returns:
            pd.DataFrame: Processed phase data
        """
        df = self._get_phase_data(phase)
        phase_name = dict(self.phases)[phase]
        
        for equipment_type in self.equipment_types:
            query = "SELECT * FROM Parameter WHERE EquipmentName=? AND PhaseID=?"
            cursor.execute(query, (equipment_type, phase))
            parameters = cursor.fetchall()
            
            for param in parameters:
                v = self.process_turbine_data(param)
                c = []
                
                # Map equipment types to their processing functions
                equipment_map = {
                    "Gas Turbine": ("gt_super_function", "GT"),
                    "Diesel Engine": ("da_super_function", "DA"),
                    "AC": ("ac_super_function", "AC"),
                    "SRGM": ("srgm_super_function", "SRGM"),
                    "VESSEL": ("vessel_super_function", "VESSEL")
                }
                
                if equipment_type in equipment_map:
                    func_name, eq_code = equipment_map[equipment_type]
                    # Note: These super functions need to be implemented based on your specific needs
                    # c = getattr(self, func_name)(v, param)
                    N = self.filter_probabilities_for_phase(param[1], c, phase_name, eq_code)
                    
                    if N is not None:
                        all_n_values = df.loc[equipment_type].tolist()
                        if len(all_n_values) < 20:
                            all_n_values.append(N)
                            all_n_values.extend([0] * (20 - len(all_n_values)))
                            df.loc[equipment_type] = all_n_values
                        
                        self.log_and_print(
                            f"{param[1]} : {equipment_type} with {phase_name} has Utility: {N}"
                        )
        
        return df

    @staticmethod
    def _process_maintenance_data(data_tuple: Tuple, c1_values: List[float], 
                                df_dict: Dict) -> None:
        """Process maintenance-related data"""
        if data_tuple[1] == "Maintenance (Pending MAJOR defects)":
            if data_tuple[7] in [1, 2, 3]:
                df_dict.update({
                    "C2": [x + 1 for x in c1_values],
                    "C3": [x + 2 for x in c1_values],
                    "C4": [x + 3 for x in c1_values]
                })
        elif data_tuple[1] == "Maintenance (Pending preventive maintenance)":
            if data_tuple[7] in [1, 2]:
                df_dict.update({
                    "C2": [x + 2 for x in c1_values],
                    "C3": [x + 3 for x in c1_values],
                    "C4": [x + 4 for x in c1_values]
                })

    @staticmethod
    def _apply_multipliers(data_tuple: Tuple, df_dict: Dict) -> None:
        """Apply multipliers to the data dictionary"""
        if data_tuple[1] != "Capability (Ammunition types)":
            for i, multiplier in enumerate(data_tuple[8:11], 2):
                if multiplier is not None:
                    df_dict[f"C{i}"] = [x * float(multiplier) for x in df_dict["C1"]]

    def calculate_dependability(self) -> float:
        """Calculate overall system dependability"""
        phase_dependabilities = []
        
        for phase_num in [1, 2, 3]:
            df = self._calculate_phase_dependability(phase_num)
            phase_dependabilities.append(df)
            
        return self._calculate_final_dependability(phase_dependabilities)

    def _calculate_phase_dependability(self, phase: int) -> float:
        """Calculate dependability for a specific phase"""
        df = self._get_phase_data(phase)
        result_df = self._process_equipment_df(df)
        normalized_matrix = self._normalize_dataframe(result_df)
        importance_matrix = self._create_importance_matrix()
        
        normalized = self._process_matrices(importance_matrix, normalized_matrix)
        minimum_list = self._get_row_minimums_nonzero(result_df)
        res = self._multiply_lists(minimum_list, normalized)
        
        return sum(res)

    def _calculate_final_dependability(self, phase_values: List[float]) -> float:
        """Calculate final dependability score"""
        ideal_vector = [1, 1, 1]
        euclidean_distance = sqrt(sum((i - j) ** 2 
                                for i, j in zip(ideal_vector, phase_values)))
        return (1.73 - euclidean_distance) / 1.73

    @staticmethod
    def _create_importance_matrix() -> pd.DataFrame:
        """Create the importance matrix for calculations"""
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
        # Matrix values would be defined here...
        return pd.DataFrame(data, index=index)  # Complete matrix definition

    @staticmethod
    def _normalize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
        """Normalize DataFrame values"""
        max_values = df.max()
        normalized_df = df.copy()
        
        for col in df.columns:
            if max_values[col] != 0:
                normalized_df[col] = df[col] / max_values[col]
                
        return normalized_df

    @staticmethod
    def _get_row_minimums_nonzero(df: pd.DataFrame) -> List[float]:
        """Get minimum non-zero values for each row"""
        return df.replace(0, float("inf")).min(axis=1).replace(float("inf"), 0).tolist()

    @staticmethod
    def _multiply_lists(list1: List[float], list2: List[float]) -> List[float]:
        """Multiply corresponding elements of two lists"""
        if len(list1) != len(list2):
            raise ValueError("Lists must have equal length")
        return [a * b for a, b in zip(list1, list2)]


if __name__ == "__main__":
    calculator = DependabilityCalculator()
    result = calculator.calculate_dependability()
    print(f"Final dependability: {result:.4f}")