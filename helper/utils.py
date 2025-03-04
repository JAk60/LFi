import numpy as np
import pandas as pd
import os
import sys

sys.path.append("../../")
sys.path.append("../")
sys.path.append("../codes/")

from sklearn.model_selection import train_test_split
from task_utils import embedding
import sys


def label_map(label_instances):
    """
    Create a mapping of labels to unique integer indices.

    Args:
        label_instances (list): List of unique label names

    Returns:
        dict: Mapping of label names to integer indices
    """
    return {label: idx for idx, label in enumerate(label_instances)}


from sklearn.preprocessing import MultiLabelBinarizer
from typing import Dict, List, Tuple


def get_category_labels() -> Dict[str, List[str]]:
    """Returns predefined categories and their labels"""
    return {
        "TaskObjective": [
            "Gun firing",
            "Interrogation and interception",
            "Maintenance scheduling",
            "Miscellaneous",
            "Missile firing",
            "Search and rescue",
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
            "Workshop availability",
        ],
        "ObjectiveFunction": [
            "Maximum availability",
            "Maximum conformance",
            "Maximum reliability",
            "Minimum cost",
            "Minimum downtime",
            "Minimum risk",
            "Minimum time",
        ],
    }


def encode_labels_multilabel(
    labels_series: pd.Series, labels: str
) -> Tuple[np.ndarray, MultiLabelBinarizer]:
    """
    Encode labels using MultiLabelBinarizer for multi-label classification.

    Args:
        labels_series: Series containing comma-separated labels
        labels: Labels name to get valid labels ("TaskObjective", "Constraints", or "Objective function")

    Returns:
        Tuple of (encoded labels array, fitted MultiLabelBinarizer)
    """
    # Split comma-separated strings into lists
    label_lists = labels_series.str.split(",").apply(
        lambda x: [item.strip() for item in x]
    )

    # Initialize MultiLabelBinarizer with the valid classes for the labels
    valid_labels = get_category_labels()[labels]
    mlb = MultiLabelBinarizer(classes=valid_labels)

    # Transform the labels
    encoded_labels = mlb.fit_transform(label_lists)

    return encoded_labels, mlb


def load_and_preprocess_data_with_embeddings(
    full_path: str = "../data/processed/version2/full.csv",
    embedding_path: str = "../data/processed/version2/full.npy",
    labels: str = "TaskObjective",
    is_generate_embed: bool = False,
) -> Tuple[pd.Series, np.ndarray, np.ndarray, pd.DataFrame, MultiLabelBinarizer]:
    """
    Loads data and creates encodings using MultiLabelBinarizer.

    Args:
        full_path: Path to CSV file
        embedding_path: Path to embeddings
        labels: Which labels to encode ("TaskObjective", "Constraints", or "Objective function")
        is_generate_embed: Whether to generate new embeddings

    Returns:
        Tuple of (raw text, embeddings, encoded labels, full dataframe, fitted MultiLabelBinarizer)
    """
    # Load the dataset
    df_full = pd.read_csv(full_path)
    X = df_full["Scenario"]

    # Handle embeddings
    if not os.path.exists(embedding_path) and is_generate_embed:
        features = embedding.scenarios_embedding(list(df_full["Scenario"]))
        np.save(embedding_path, features)

    # Load embeddings
    with open(embedding_path, "rb") as f:
        X_feats = np.load(f)

    # Verify labels exists
    categories = get_category_labels()
    if labels not in categories:
        raise ValueError(f"Labels must be one of {list(categories.keys())}")

    # Create encodings using MultiLabelBinarizer
    Y, mlb = encode_labels_multilabel(df_full[labels], labels)

    # Print shape information
    print("\nEncoding details:")
    print(f"Selected labels: {labels}")
    print(f"Number of {labels} labels: {len(categories[labels])}")
    print(f"X shape (scenarios): {X.shape}")
    print(f"Y shape (labels): {Y.shape}")
    print("Label meanings:")
    for idx, label in enumerate(mlb.classes_):
        print(f"  Position {idx}: {label}")

    return X, X_feats, Y, df_full


def get_unique_labels(df, labels_column):
    """
    Get unique labels by splitting comma-separated label lists.

    Args:
        df (pandas.DataFrame): Input DataFrame
        labels_column (str): Name of the column containing labels

    Returns:
        list: Sorted unique labels
    """
    # Split comma-separated labels and create a set of unique labels
    all_labels = set()
    for labels_str in df[labels_column]:
        labels = [label.strip() for label in labels_str.split(",")]
        all_labels.update(labels)

    return sorted(list(all_labels))


def divide_labeled_unlabeled(X_train, X_feats_train, Y_train, label_per, seed=42):
    """
    Randomly divide training data into labeled and unlabeled subsets.

    Args:
        X_train (np.array): Input data
        X_feats_train (np.array): Input features
        Y_train (np.array): Input labels
        label_per (float): Percentage of data to be labeled
        seed (int, optional): Random seed for reproducibility. Defaults to 42.

    Returns:
        tuple: Labeled and unlabeled data and feature subsets
    """
    # Set the random seed for reproducibility
    if seed is not None:
        np.random.seed(seed)

    # Determine the number of labeled samples
    num_samples = X_train.shape[0]
    num_labeled = int(label_per * num_samples)

    # Generate a random permutation of indices
    indices = np.random.permutation(num_samples)

    # Split indices into labeled and unlabeled
    labeled_indices = indices[:num_labeled]
    unlabeled_indices = indices[num_labeled:]

    # Create labeled and unlabeled subsets
    X_L = X_train[labeled_indices]
    X_feats_L = X_feats_train[labeled_indices]
    Y_L = Y_train[labeled_indices]

    X_U = X_train[unlabeled_indices]
    X_feats_U = X_feats_train[unlabeled_indices]

    return X_L, X_feats_L, Y_L, X_U, X_feats_U


def load_data_full(
    full_path="../data/processed/version2/full.csv",
    embedding_path="../data/processed/version2/full.npy",
    labels="Category",
    is_generate_embed=False,
):
    """
    Load full dataset with scenarios, embeddings, and labels.

    Args:
        full_path (str): Path to the full CSV file
        embedding_path (str): Path to the embedding numpy file
        labels (str, optional): Column name for labels. Defaults to "Category"
        is_generate_embed (bool, optional): Generate embeddings if not exist. Defaults to False

    Returns:
        tuple: Scenarios, scenario features, label indices, and original DataFrame
    """
    df_full = pd.read_csv(full_path)
    X = df_full["Scenario"]

    # if file embedding file is not exist please create the embedding
    print(os.path.exists(embedding_path), is_generate_embed)
    if not os.path.exists(embedding_path) and is_generate_embed:
        features = embedding.scenarios_embedding(list(df_full["Scenario"]))
        np.save(embedding_path, features)

    with open(embedding_path, "rb") as f:
        X_feats = np.load(f)

    label_instances = get_unique_labels(df_full, labels)

    label_map_dict = label_map(label_instances)

    Y = df_full[labels]
    Y = df_full[labels].map(label_map_dict)
    Y = Y.to_numpy()

    return X, X_feats, Y, df_full


def load_data_train_test_split(
    processed_data_path="../data/processed/",
    version=2,
    is_data_split=True,
    labels="Category",
    multilabel=False,
    is_generate_embed=True,
):
    """
    Load dataset with optional train-test split.

    Args:
        processed_data_path (str): Base path to processed data
        version (int, optional): Data version. Defaults to 2
        is_data_split (bool, optional): Whether data is pre-split. Defaults to True
        labels (str, optional): Column name for labels. Defaults to "Category"
        is_generate_embed (bool, optional): Generate embeddings if not exist. Defaults to False

    Returns:
        tuple: Depending on data split, returns various dataset configurations
    """
    if is_data_split:
        # Paths for training, validation, and test files
        train_path = f"{processed_data_path}version{version}/train.csv"
        train_embedding_path = f"{processed_data_path}version{version}/train.npy"
        val_path = f"{processed_data_path}version{version}/val.csv"
        print("val_path", val_path)
        val_embedding_path = f"{processed_data_path}version{version}/val.npy"
        test_path = f"{processed_data_path}version{version}/test.csv"
        test_embedding_path = f"{processed_data_path}version{version}/test.npy"
        if multilabel:
            X_train, X_feats_train, Y_train, df_train = (
                load_and_preprocess_data_with_embeddings(
                    train_path, train_embedding_path, labels, is_generate_embed
                )
            )

            # Load validation data
            X_val, X_feats_val, Y_val, df_val = (
                load_and_preprocess_data_with_embeddings(
                    val_path, val_embedding_path, labels, is_generate_embed
                )
            )

            # Load test data
            X_test, X_feats_test, Y_test, df_test = (
                load_and_preprocess_data_with_embeddings(
                    test_path, test_embedding_path, labels, is_generate_embed
                )
            )

            return (
                X_train,
                X_feats_train,
                Y_train,
                X_val,
                X_feats_val,
                Y_val,
                X_test,
                X_feats_test,
                Y_test,
                df_train,
                df_val,
                df_test,
            )
        else:
            # Load training data
            X_train, X_feats_train, Y_train, df_train = load_data_full(
                train_path, train_embedding_path, labels, is_generate_embed
            )

            # Load validation data
            X_val, X_feats_val, Y_val, df_val = load_data_full(
                val_path, val_embedding_path, labels, is_generate_embed
            )

            # Load test data
            X_test, X_feats_test, Y_test, df_test = load_data_full(
                test_path, test_embedding_path, labels, is_generate_embed
            )

            return (
                X_train,
                X_feats_train,
                Y_train,
                X_val,
                X_feats_val,
                Y_val,
                X_test,
                X_feats_test,
                Y_test,
                df_train,
                df_val,
                df_test,
            )

    else:
        # Load the full data
        full_path = f"{processed_data_path}version{version}/full.csv"
        embedding_path = f"{processed_data_path}version{version}/full.npy"
        if multilabel:
            X, X_feats, Y, df_full = load_and_preprocess_data_with_embeddings(
                full_path, embedding_path, labels, is_generate_embed
            )
        else:
            X, X_feats, Y, df_full = load_data_full(
                full_path, embedding_path, labels, is_generate_embed
            )
        return X, X_feats, Y, df_full


def get_various_data(
    X, Y, X_feats, val_per=0.15, test_per=0.15, label_per=0.1, U_per=None, seed=42
):
    """
    Split data into validation, test, labeled, and unlabeled sets.

    Args:
        X (np.array): Input data
        Y (np.array): Input labels
        X_feats (np.array): Input features
        val_per (float, optional): Validation data percentage. Defaults to 0.15
        test_per (float, optional): Test data percentage. Defaults to 0.15
        label_per (float, optional): Labeled data percentage. Defaults to 0.1
        U_per (float, optional): Unlabeled data percentage. Defaults to None
        seed (int, optional): Random seed. Defaults to 42

    Returns:
        tuple: Validation, test, labeled, and unlabeled data splits
    """
    validation_size = int(val_per * len(X))
    test_size = int(test_per * len(X))
    train_size = len(X) - validation_size - test_size
    L_size = int(label_per * train_size)
    if not U_per:
        U_size = train_size - L_size
    else:
        U_size = U_per * train_size

    if seed is not None:
        np.random.seed(seed)

    index = np.arange(X.size)
    index = np.random.permutation(index)
    X = X[index]
    Y = Y[index]
    X_feats = X_feats[index]

    X_V = X[-validation_size:]
    Y_V = Y[-validation_size:]
    X_feats_V = X_feats[-validation_size:]

    X_T = X[-(validation_size + test_size) : -validation_size]
    Y_T = Y[-(validation_size + test_size) : -validation_size]
    X_feats_T = X_feats[-(validation_size + test_size) : -validation_size]

    X_L = X[-(validation_size + test_size + L_size) : -(validation_size + test_size)]
    Y_L = Y[-(validation_size + test_size + L_size) : -(validation_size + test_size)]
    X_feats_L = X_feats[
        -(validation_size + test_size + L_size) : -(validation_size + test_size)
    ]

    X_U = X[:U_size]
    X_feats_U = X_feats[:U_size]

    return X_V, Y_V, X_feats_V, X_T, Y_T, X_feats_T, X_L, Y_L, X_feats_L, X_U, X_feats_U


def get_test_U_data(X, Y, X_feats, test_per=0.30, U_per=None, random_seed=42):
    """
    Split data into test and unlabeled sets.

    Args:
        X (np.array): Input data
        Y (np.array): Input labels
        X_feats (np.array): Input features
        test_per (float, optional): Test data percentage. Defaults to 0.30
        U_per (float, optional): Unlabeled data percentage. Defaults to None
        random_seed (int, optional): Random seed. Defaults to 42

    Returns:
        tuple: Test and unlabeled data splits
    """
    test_size = int(test_per * len(X))

    if random_seed is not None:
        np.random.seed(random_seed)

    if U_per is None:
        U_size = X.size - test_size
    else:
        U_size = U_per * X.size

    index = np.arange(X.size)
    index = np.random.permutation(index)
    X = X[index]
    Y = Y[index]
    X_feats = X_feats[index]

    X_T = X[-test_size:]
    Y_T = Y[-test_size:]
    X_feats_T = X_feats[-test_size:]

    X_U = X[:U_size]
    X_feats_U = X_feats[:U_size]

    return X_T, Y_T, X_feats_T, X_U, X_feats_U


def train_test_split_df(df, labels, test_size=0.15, val_size=0.15, random_state=42):
    """
    Stratified train-test-validation split for DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame
        labels (str): Column name for stratification
        test_size (float, optional): Test data percentage. Defaults to 0.15
        val_size (float, optional): Validation data percentage. Defaults to 0.15
        random_state (int, optional): Random seed. Defaults to 42

    Returns:
        tuple: Train, validation, and test DataFrames
    """
    val_test_size = test_size + val_size
    test_size = test_size / val_test_size

    df_train, df_test_val = train_test_split(
        df, test_size=val_test_size, random_state=42, stratify=df[labels]
    )
    df_val, df_test = train_test_split(
        df_test_val, test_size=test_size, random_state=42, stratify=df_test_val[labels]
    )

    # Checking the resulting splits
    print(
        f"Training : {df_train.shape}, Validation : {df_val.shape}, Test : {df_test.shape}"
    )
    print(
        f"Training : {df_train[labels].value_counts()}, Validation : {df_val[labels].value_counts()}, Test : {df_test[labels].value_counts()}"
    )

    return df_train, df_val, df_test


def reverse_train_test_split(df_train, df_val, df_test):
    """
    Combine split DataFrames back into a single DataFrame.

    Args:
        df_train (pd.DataFrame): Training DataFrame
        df_val (pd.DataFrame): Validation DataFrame
        df_test (pd.DataFrame): Test DataFrame

    Returns:
        pd.DataFrame: Recombined DataFrame
    """
    # Combine the validation and test DataFrames
    df_test_val = pd.concat([df_val, df_test])

    # Combine the training DataFrame with the combined validation and test DataFrames
    df = pd.concat([df_train, df_test_val])

    # Checking the resulting combined DataFrame
    print(f"Combined DataFrame : {df.shape}")

    return df


def print_all_shapes(
    X_V, Y_V, X_feats_V, X_T, Y_T, X_feats_T, X_L, Y_L, X_feats_L, X_U, X_feats_U
):
    """
    Print shapes of all input variables.

    Args:
        X_V, Y_V, X_feats_V: Validation data and features
        X_T, Y_T, X_feats_T: Test data and features
        X_L, Y_L, X_feats_L: Labeled data and features
        X_U, X_feats_U: Unlabeled data and features
    """
    print(f"X_V shape: {X_V.shape}")
    print(f"Y_V shape: {Y_V.shape}")
    print(f"X_feats_V shape: {X_feats_V.shape}")
    print(f"X_T shape: {X_T.shape}")
    print(f"Y_T shape: {Y_T.shape}")
    print(f"X_feats_T shape: {X_feats_T.shape}")
    print(f"X_L shape: {X_L.shape}")
    print(f"Y_L shape: {Y_L.shape}")
    print(f"X_feats_L shape: {X_feats_L.shape}")
    print(f"X_U shape: {X_U.shape}")
    print(f"X_feats_U shape: {X_feats_U.shape}")


def process_data(
    is_data_split=True,
    model="LR",
    processed_data_path="../LFs/data/processed",
    version=1,
    labels="TaskObjective",
    test_per=0.15,
    val_per=0.15,
    label_per=None,
    multilabel=True,  # Set this to True
    seed=42,
    print_shape=False,
):
    """
        Comprehensive data processing function for different machine learning scenarios.

    Args:
        is_data_split (bool, optional): Whether data is pre-split. Defaults to True
        model (str, optional): Model type for processing. Defaults to "LR"
        processed_data_path (str, optional): Path to processed data. Defaults to "../LFs/data/processed"
        version (int, optional): Data version. Defaults to 1
        labels (str, optional): Column name for labels. Defaults to "Category"
        test_per (float, optional): Test data percentage. Defaults to 0.15
        val_per (float, optional): Validation data percentage. Defaults to 0.15
        label_per (float, optional): Labeled data percentage. Defaults to None
        seed (int, optional): Random seed. Defaults to 42
        print_shape (bool, optional): Whether to print data shapes. Defaults to False

    Returns:
        tuple: Processed data splits for validation, test, labeled, and unlabeled sets
    """
    if not is_data_split:
        X, X_feats, Y, df_full = load_data_train_test_split(
            processed_data_path=processed_data_path,
            version=version,
            is_data_split=is_data_split,
            multilabel=multilabel,
            labels=labels,
        )

        if model == "CAGE":
            X_T, Y_T, X_feats_T, X_U, X_feats_U = get_test_U_data(
                X, Y, X_feats, test_per=test_per, U_per=None, random_seed=seed
            )
            # Initialize empty arrays with correct shape for validation and labeled sets
            X_V = np.array([])
            Y_V = np.zeros((0, Y.shape[1]))  # Keep correct number of columns
            X_feats_V = np.zeros(
                (0, X_feats.shape[1])
            )  # Keep correct number of features
            X_L = np.array([])
            Y_L = np.zeros((0, Y.shape[1]))
            X_feats_L = np.zeros((0, X_feats.shape[1]))

        elif model == "JL":
            (
                X_V,
                Y_V,
                X_feats_V,
                X_T,
                Y_T,
                X_feats_T,
                X_L,
                Y_L,
                X_feats_L,
                X_U,
                X_feats_U,
            ) = get_various_data(
                X,
                Y,
                X_feats,
                val_per=val_per,
                test_per=test_per,
                label_per=label_per,
                U_per=None,
                seed=seed,
            )
    else:
        (
            X_train,
            X_feats_train,
            Y_train,
            X_V,
            X_feats_V,
            Y_V,
            X_T,
            X_feats_T,
            Y_T,
            df_train,
            df_val,
            df_test,
        ) = load_data_train_test_split(
            processed_data_path=processed_data_path,
            version=version,
            is_data_split=is_data_split,
            labels=labels,
            multilabel=multilabel,
            is_generate_embed=True,
        )

        if model == "CAGE":
            # Concatenate validation with unlabeled data
            X_U = np.concatenate((X_train, X_V)) if len(X_V) > 0 else X_train
            X_feats_U = (
                np.vstack((X_feats_train, X_feats_V))
                if len(X_feats_V) > 0
                else X_feats_train
            )

            # Initialize empty arrays with correct shape
            X_V = np.array([])
            Y_V = np.zeros((0, Y_train.shape[1]))  # Keep correct number of columns
            X_feats_V = np.zeros((0, X_feats_train.shape[1]))
            X_L = np.array([])
            Y_L = np.zeros((0, Y_train.shape[1]))
            X_feats_L = np.zeros((0, X_feats_train.shape[1]))

        elif model == "JL":
            X_L, X_feats_L, Y_L, X_U, X_feats_U = divide_labeled_unlabeled(
                X_train, X_feats_train, Y_train, label_per, seed
            )

    if print_shape:
        print_all_shapes(
            X_V,
            Y_V,
            X_feats_V,
            X_T,
            Y_T,
            X_feats_T,
            X_L,
            Y_L,
            X_feats_L,
            X_U,
            X_feats_U,
        )

    # # Validate shapes before returning
    # if len(Y_V) > 0:
    #     assert Y_V.shape[1] == 6, f"Y_V should have 6 columns, got {Y_V.shape[1]}"
    # if len(Y_T) > 0:
    #     assert Y_T.shape[1] == 6, f"Y_T should have 6 columns, got {Y_T.shape[1]}"
    # if len(Y_L) > 0:
    #     assert Y_L.shape[1] == 6, f"Y_L should have 6 columns, got {Y_L.shape[1]}"

    return X_V, X_feats_V, Y_V, X_T, X_feats_T, Y_T, X_L, Y_L, X_feats_L, X_U, X_feats_U
