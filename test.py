import pandas as pd
import numpy as np
import os
from typing import Dict, List, Tuple

def get_category_labels() -> Dict[str, List[str]]:
    """Returns predefined categories and their labels"""
    return {
        "Task Objective": [
            "Gun firing",
            "Interrogation and interception",
            "Maintenance scheduling",
            "Miscellaneous",
            "Missile firing",
            "Search and rescue"
        ],
        "Constraints": [
            "Activity sequences",
            "Balancing loads",
            "Capability",
            "Conformance",
            "Endurance",
            "Fleet availability",
            "Fuel",
            "Logistic time",
            "Manpower availability",
            "Ration",
            "Reliability",
            "Risk score",
            "Ship class",
            "Spares availability",
            "Speed",
            "Working hours",
            "Workshop availability"
        ],
        "Objective function": [
            "Maximum availability",
            "Maximum conformance",
            "Maximum reliability",
            "Minimum cost",
            "Minimum downtime",
            "Minimum risk",
            "Minimum time"
        ]
    }

def encode_specific_category(
    labels_str: str, 
    category_labels: List[str]
) -> np.ndarray:
    """
    Encode labels for a specific labels only.
    
    Args:
        labels_str: Comma-separated string of labels
        category_labels: List of valid labels for the chosen labels
        
    Returns:
        One-hot encoded array for the specific labels
    """
    encoding = np.zeros(len(category_labels))
    for label in labels_str.split(','):
        label = label.strip()
        if label in category_labels:
            idx = category_labels.index(label)
            encoding[idx] = 1
    return encoding

def load_and_preprocess_data_with_embeddings(
    full_path: str = "../data/processed/version2/full.csv",
    embedding_path: str = "../data/processed/version2/full.npy",
    labels: str = "Task Objective",  # Now expects specific labels
    is_generate_embed: bool = False
) -> Tuple[pd.Series, np.ndarray, np.ndarray, pd.DataFrame]:
    """
    Loads data and creates encodings for a specific labels only.
    
    Args:
        full_path: Path to CSV file
        embedding_path: Path to embeddings
        labels: Which labels to encode ("Task Objective", "Constraints", or "Objective function")
        is_generate_embed: Whether to generate new embeddings
        
    Returns:
        Tuple of (raw text, embeddings, labels-specific encoded labels, full dataframe)
    """
    # Load the dataset
    df_full = pd.read_csv(full_path)
    X = df_full["Scenario"]
    
    # Handle embeddings
    if not os.path.exists(embedding_path) and is_generate_embed:
        features = embedding.scenarios_embedding(list(df_full["Scenario"]))
        np.save(embedding_path, features)
    
    # Load embeddings
    with open(embedding_path, 'rb') as f:
        X_feats = np.load(f)
    
    # Get labels for specific labels
    categories = get_category_labels()
    if labels not in categories:
        raise ValueError(f"Labels must be one of {list(categories.keys())}")
    
    category_labels = categories[labels]
    
    # Create encodings for specific labels only
    Y = np.array([
        encode_specific_category(label_list, category_labels)
        for label_list in df_full["Labels"]
    ])
    
    # Print shape information
    print(f"\nEncoding details:")
    print(f"Selected labels: {labels}")
    print(f"Number of {labels} labels: {len(category_labels)}")
    print(f"X shape (scenarios): {X.shape}")
    print(f"Y shape (labels): {Y.shape}")
    print(f"Label meanings:")
    for idx, label in enumerate(category_labels):
        print(f"  Position {idx}: {label}")
    
    return X, X_feats, Y, df_full