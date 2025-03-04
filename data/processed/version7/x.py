import numpy as np
import os
import pandas as pd


def verify_data_consistency(csv_path, npy_path):
    """Verify consistency between CSV and NPY files"""
    print("\n=== Data Consistency Check ===")
    if not os.path.exists(csv_path) or not os.path.exists(npy_path):
        print("❌ One or both files missing!")
        return False

    df = pd.read_csv(csv_path)
    embeddings = np.load(npy_path)

    # Print record counts and shapes
    print(f"CSV records: {len(df)}, Shape: {df.shape}")
    print(f"Embedding records: {embeddings.shape[0]}, Shape: {embeddings.shape}")
    print(f"CSV last modified: {os.path.getmtime(csv_path)}")
    print(f"NPY last modified: {os.path.getmtime(npy_path)}")

    return len(df) == embeddings.shape[0]


if __name__ == "__main__":
    csv_path = "/home/user/IITB/LFi/data/processed/version7/full.csv"
    npy_path = "/home/user/IITB/LFi/data/processed/version7/full.npy"

    # First verify data consistency
    is_consistent = verify_data_consistency(csv_path, npy_path)
    print(f"\nData consistency check passed: {is_consistent}")
