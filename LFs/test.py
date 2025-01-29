from importlib import import_module
from typing import Tuple, List
from enum import Enum
import os
import sys

# Add the LFs directory to Python path if not already there
LFS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "LFs")
if LFS_DIR not in sys.path:
    sys.path.append(LFS_DIR)

MultilabelOrNot = {
    'Category': False,
    'Sub - mission': False,
    'Criticality': False,
    'Level': False,
    'Action': False,
    'Entity': False,
    'From': False,
    'Task Objective': True,
    'Constraints': True,
    'Objective function': True,
}

# Task name transformation mapping
TASK_NAME_MAPPING = {
    'Sub - mission': 'SubMission',
    'Task Objective': 'TaskObjective',
    'Objective function': 'ObjectiveFunction'
}

# Updated MODULE_MAPPING to match actual folder structure
MODULE_MAPPING = {
    "Action": "Action.ActionLFS",
    "Category": "category.CategoryLFS",
    "Constraints": "Constraints.ConstraintsLFS",
    "Criticality": "Criticality.CriticalityLFS",
    "Entity": "Entity.EntityLFS",
    "Level": "Level.LevelLFS",
    "ObjectiveFunction": "ObjectiveFunction.ObjectiveFuncLFS",
    "SubMission": "SubMission.SubcategoryLFS",
    "TaskObjective": "TaskObjective.TaskObjectiveLFS",
}

def normalize_task_name(task_name: str) -> str:
    """
    Normalizes task names to match the MODULE_MAPPING keys.
    """
    # First check if there's a direct mapping
    if task_name in TASK_NAME_MAPPING:
        return TASK_NAME_MAPPING[task_name]
    
    # If no direct mapping, return the original name
    return task_name

def get_task_components(task_name: str) -> Tuple[Enum, List]:
    """
    Dynamically imports ClassLabels and LFs for a given task using the module mapping.
    """
    try:
        # Normalize the task name to match MODULE_MAPPING keys
        normalized_task_name = normalize_task_name(task_name)
        
        if normalized_task_name not in MODULE_MAPPING:
            raise ImportError(f"No module mapping found for task {task_name} (normalized: {normalized_task_name})")
        
        # Get the module path
        module_path = MODULE_MAPPING[normalized_task_name]
        
        # Import the module
        module = import_module(module_path)
        
        # Get ClassLabels and LF list
        class_labels = getattr(module, "ClassLabels")
        task_lfs = getattr(module, f"{normalized_task_name}LF")
        
        return class_labels, task_lfs
        
    except ImportError as e:
        raise ImportError(f"Failed to import components for task {task_name}: {str(e)}")
    except AttributeError as e:
        raise AttributeError(f"Failed to find required attributes for task {task_name}: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        print("Testing import for Sub - mission...")
        ClassLabels, task_lfs = get_task_components("Sub - mission")
        print("Success!")
        print(f"ClassLabels: {ClassLabels}")
        print(f"Task LFs: {task_lfs}")
    except Exception as e:
        print(f"Error: {str(e)}")