import os
import sys
from enum import Enum
from importlib import import_module
from typing import List, Tuple

from jl import run_jl

# hyperparmeter tuning
loss_func_mask = [1, 1, 1, 1, 1, 1, 1]
batch_size = 32
lr_fm = 0.0005
lr_gm = 0.01
use_accuracy_score = True
feature_model = "nn"
n_features = 768
n_hidden = 512
metric_avg = "micro"
n_epochs = 100
start_len = 7
stop_len = 10
is_qt = True
is_qc = True
qt = 0.9
qc = 0.85
# Add the LFs directory to Python path if not already there
LFS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "LFs")
if LFS_DIR not in sys.path:
    sys.path.append(LFS_DIR)

MultilabelOrNot = {
    "Category": False,
    "SubMission": False,
    "Criticality": False,
    "Level": False,
    "Action": False,
    "Entity": False,
    "From": False,
    "TaskObjective": True,
    "Constraints": True,
    "ObjectiveFunction": True,
}

# labels name transformation mapping
TASK_NAME_MAPPING = {
    "SubMission": "SubMission",
    "TaskObjective": "TaskObjective",
    "ObjectiveFunction": "ObjectiveFunction",
}

# Updated MODULE_MAPPING to match actual folder structure
MODULE_MAPPING = {
    "Action": "Action.ActionLFS",
    "Category": "Category.CategoryLFS",
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
    Normalizes labels names to match the MODULE_MAPPING keys.
    """
    # First check if there's a direct mapping
    if task_name in TASK_NAME_MAPPING:
        return TASK_NAME_MAPPING[task_name]

    # If no direct mapping, return the original name
    return task_name


def get_task_components(task_name: str) -> Tuple[Enum, List]:
    """
    Dynamically imports ClassLabels and LFs for a given labels using the module mapping.
    """
    try:
        # Normalize the labels name to match MODULE_MAPPING keys
        normalized_task_name = normalize_task_name(task_name)

        if normalized_task_name not in MODULE_MAPPING:
            raise ImportError(
                f"No module mapping found for labels {task_name} (normalized: {normalized_task_name})"
            )

        # Get the module path
        module_path = MODULE_MAPPING[normalized_task_name]

        # Import the module
        module = import_module(module_path)

        # Get ClassLabels and LF list
        class_labels = module.ClassLabels
        task_lfs = getattr(module, f"{normalized_task_name}LF")

        return class_labels, task_lfs

    except ImportError as e:
        raise ImportError(
            f"Failed to import components for labels {task_name}: {e!s}"
        )
    except AttributeError as e:
        raise AttributeError(
            f"Failed to find required attributes for labels {task_name}: {e!s}"
        )


# ClassLabels, task_lfs = get_task_components("Sub - mission")
# print(ClassLabels)
# print(task_lfs)
# ['Category', 'Sub - mission', 'Criticality', 'Level', 'Action', 'Entity',
#        'From', 'labels Objective', 'Constraints', 'Objective function']
# Modified main code
import pandas as pd
from applyLF import run_applyLF
from utils import extract_unique_labels

from helper.utils import process_data
from spear.labeling import LFSet

# Load data
full_path = "/home/user/IITB/LFi/data/processed/version7/full.csv"
df_full = pd.read_csv(full_path)
# all_tasks = df_full.columns[1:]
# print("---->>all tasks", all_tasks)
all_tasks = [
    # 'Category',
    # 'SubMission',
    # 'Criticality',
    # 'Level',
    # 'Action',
    "Entity",
    # 'From',
    # 'TaskObjective',
    # 'Constraints',
    # 'ObjectiveFunction'
]
for labels in all_tasks:
    print(f"Processing labels: {labels}")

    # Get ClassLabels and LFs for current labels
    ClassLabels, task_lfs = get_task_components(labels)
    multilabel = MultilabelOrNot[labels]
    # Create LFSet
    rules = LFSet(f"{labels}_LF")
    rules.add_lf_list(task_lfs)

    # Process data
    X_V, X_feats_V, Y_V, X_T, X_feats_T, Y_T, X_L, Y_L, X_feats_L, X_U, X_feats_U = (
        process_data(
            is_data_split=False,
            model="JL",
            processed_data_path="/home/user/IITB/LFi/data/processed/",
            version=7,
            labels=labels,
            test_per=0.15,
            val_per=0.15,
            label_per=0.2,
            multilabel=multilabel,
            seed=42,
            print_shape=True,
        )
    )

    # Extract labels and run LFs
    label_instances = extract_unique_labels(df_full, labels)
    label_instances.sort()
    # Generate output files

    V_path_pkl = f"/home/user/IITB/LFi/LFs/{labels}/result/{labels}_pickle_V.pkl"
    T_path_pkl = f"/home/user/IITB/LFi/LFs/{labels}/result/{labels}_pickle_T.pkl"
    U_path_pkl = f"/home/user/IITB/LFi/LFs/{labels}/result/{labels}_pickle_U.pkl"
    L_path_pkl = f"/home/user/IITB/LFi/LFs/{labels}/result/{labels}_pickle_L.pkl"
    path_json = f"/home/user/IITB/LFi/LFs/{labels}/result/{labels}.json"

    # Run apply LF
    run_applyLF(
        X_V,
        X_feats_V,
        Y_V,
        X_T,
        X_feats_T,
        Y_T,
        X_L,
        Y_L,
        X_feats_L,
        X_U,
        X_feats_U,
        version=7,
        labels=labels,
        label_instances=label_instances,
        model="JL",
        seed=42,
        ClassLabels=ClassLabels,
        rules=rules,
        V_path_pkl=V_path_pkl,
        T_path_pkl=T_path_pkl,
        U_path_pkl=U_path_pkl,
        L_path_pkl=L_path_pkl,
        path_json=path_json,
    )
    run_jl(
        version=7,
        labels=labels,
        model="JL",
        loss_func_mask=loss_func_mask,
        batch_size=batch_size,
        lr_fm=lr_fm,
        lr_gm=lr_gm,
        use_accuracy_score=use_accuracy_score,
        feature_model=feature_model,
        n_features=n_features,
        n_hidden=n_hidden,
        metric_avg=metric_avg,
        n_epochs=n_epochs,
        start_len=start_len,
        stop_len=stop_len,
        is_qt=is_qt,
        is_qc=is_qc,
        qt=qt,
        qc=qc,
        V_path_pkl=V_path_pkl,
        T_path_pkl=T_path_pkl,
        U_path_pkl=U_path_pkl,
        L_path_pkl=L_path_pkl,
        path_json=path_json,
    )
