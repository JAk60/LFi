from importlib import import_module
from typing import Tuple, List
from enum import Enum

import os
import sys
from importlib import import_module
from typing import Tuple, List
from enum import Enum

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
    'SubMission': False,
    'Criticality': False,
    'Level': False,
    'Action': False,
    'Entity': False,
    'From': False,
    'TaskObjective': True,
    'Constraints': True,
    'ObjectiveFunction': True,
}

# Task name transformation mapping
TASK_NAME_MAPPING = {
    'SubMission': 'SubMission',
    'TaskObjective': 'TaskObjective',
    'ObjectiveFunction': 'ObjectiveFunction'
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


# ClassLabels, task_lfs = get_task_components("Sub - mission")
# print(ClassLabels)
# print(task_lfs)
# ['Category', 'Sub - mission', 'Criticality', 'Level', 'Action', 'Entity',
#        'From', 'Task Objective', 'Constraints', 'Objective function']
# Modified main code
from applyLF import run_applyLF
from utils import extract_unique_labels
from spear.labeling import PreLabels, LFSet
from helper.utils import process_data
import pandas as pd

# Load data
full_path = "/home/user/IITB/LFi/data/processed/version7/full.csv"
df_full = pd.read_csv(full_path)
# all_tasks = df_full.columns[1:]
# print("---->>all tasks", all_tasks)
all_tasks=[
# 'Category', 
# 'SubMission', 
# 'Criticality',
# 'Level',
# 'Action',
'Entity',
# 'From',
# 'TaskObjective', 
# 'Constraints', 
# 'ObjectiveFunction'
]
for task in all_tasks:
    print(f"Processing task: {task}")
    
    # Get ClassLabels and LFs for current task
    ClassLabels, task_lfs = get_task_components(task)
    multilabel=MultilabelOrNot[task]
    # Create LFSet
    rules = LFSet(f"{task}_LF")
    rules.add_lf_list(task_lfs)
    
    # Process data
    X_V, X_feats_V, Y_V, X_T, X_feats_T, Y_T, X_L, Y_L, X_feats_L, X_U, X_feats_U = process_data(
        is_data_split=False,
        model="JL",
        processed_data_path="/home/user/IITB/LFi/data/processed/",
        version=7,
        labels=task,
        test_per=0.15,
        val_per=0.15,
        label_per=0.2,
        multilabel=multilabel,
        seed=42,
        print_shape=False
    )
    
    # Extract labels and run LFs
    label_instances = extract_unique_labels(df_full, task)
    label_instances.sort()  
    # Generate output files
    V_path_pkl = f'/home/user/IITB/LFi/LFs/{task}/result/{task}_pickle_V.pkl'
    T_path_pkl = f'/home/user/IITB/LFi/LFs/{task}/result/{task}_pickle_T.pkl'
    U_path_pkl = f'/home/user/IITB/LFi/LFs/{task}/result/{task}_pickle_U.pkl'
    L_path_pkl = f'/home/user/IITB/LFi/LFs/{task}/result/{task}_pickle_L.pkl'
    path_json = f'/home/user/IITB/LFi/LFs/{task}/result/{task}.json'
    
    # Run apply LF
    run_applyLF(
        X_V, X_feats_V, Y_V, X_T, X_feats_T, Y_T, X_L, Y_L, X_feats_L, X_U, X_feats_U,
        version=7,
        labels=task,
        label_instances=label_instances,
        model="JL",
        seed=42,
        ClassLabels=ClassLabels,
        rules=rules,
        V_path_pkl=V_path_pkl,
        T_path_pkl=T_path_pkl,
        U_path_pkl=U_path_pkl,
        L_path_pkl=L_path_pkl,
        path_json=path_json
    )