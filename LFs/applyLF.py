import os
import numpy as np
import pandas as pd
from spear.labeling import PreLabels
from utils import extract_unique_labels 

def run_applyLF(
    X_V, X_feats_V, Y_V, X_T, X_feats_T, Y_T, X_L, Y_L, X_feats_L, X_U, X_feats_U,
    ClassLabels,
    rules,
    version=1,
    labels="Category",
    label_instances=None,
    model="JL",
    seed=42,
    V_path_pkl=None,
    T_path_pkl=None,
    U_path_pkl=None,
    L_path_pkl=None,
    path_json=None
):
    """
    Apply Labeling Functions (LFs) to datasets and save the resulting noisy labels.

    Parameters:
    - X_V, X_feats_V, Y_V: Validation dataset and features
    - X_T, X_feats_T, Y_T: Test dataset and features
    - X_L, Y_L, X_feats_L: Labeled dataset and features
    - X_U, X_feats_U: Unlabeled dataset and features
    - version: Version of the data pipeline
    - labels: Column name containing labels
    - label_instances: List of unique labels (optional)
    - model: Model name
    - seed: Random seed
    - V_path_pkl: Path to save validation pickle
    - path_json: Path to save JSON files
    """
    print("---> Running applyLF")

    # Extract unique labels if not provided
    if not label_instances:
        full_path = f"../data/processed/version{version}/full.csv"
        df_full = pd.read_csv(full_path)
        label_instances = extract_unique_labels(df_full, labels)

    label_instances.sort()
    print("Unique Labels:", label_instances)

    # # Design labeling functions
    # ClassLabels, rules = design_lf(labels, label_instances, version=version)
    # num_classes = len(label_instances)

    # Process datasets
    datasets = [
        (X_V, Y_V, X_feats_V, V_path_pkl, "Validation"),
        (X_L, Y_L, X_feats_L, L_path_pkl, "Labeled"),
        (X_T, Y_T, X_feats_T, T_path_pkl, "Test"),
        (X_U,[], X_feats_U,U_path_pkl,"Unlabeled")
    ]

    for data, gold_labels, data_feats, pkl_path, dataset_name in datasets:
        if dataset_name == "Unlabeled":
            context_noisy_labels = PreLabels(
                name=labels,
                data=data,
                # gold_labels=gold_labels,
                data_feats=data_feats,
                rules=rules,
                labels_enum=ClassLabels,
                num_classes=len(ClassLabels)
            )
        else:
            context_noisy_labels = PreLabels(
            name=labels,
            data=data,
            gold_labels=gold_labels,
            data_feats=data_feats,
            rules=rules,
            labels_enum=ClassLabels,
            num_classes=len(ClassLabels)
        )
        if pkl_path:
            context_noisy_labels.generate_pickle(pkl_path)
            print(f"{dataset_name} Pickle Path:", pkl_path)
        if dataset_name == "Validation" and path_json:
            context_noisy_labels.generate_json(path_json)
            print("JSON Path:", path_json)

if __name__ == "__main__":
    print("Please provide the required parameters to run the function.")
