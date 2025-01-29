from highCLF import High_Critical_LFS
from lowCLF import Low_Critical_LFS
from midCLF import Mid_Critical_LFS
import enum
from spear.labeling import labeling_function, ABSTAIN, preprocessor, LFSet
class ClassLabels(enum.Enum):
    High = 0
    Mid = 1
    Low = 2
    

THRESHOLD = 0.6

CriticalityLF = High_Critical_LFS + Low_Critical_LFS +Mid_Critical_LFS
print(CriticalityLF)

# rules = LFSet("Criticality_LF")
# rules.add_lf_list(CriticalityLF)

# from spear.labeling import PreLabels
# from helper.utils import process_data
# import pandas as pd

# # processed_data_path="../LFs/data/processed/"
# full_path = "../data/processed/version6/full.csv"
# df_full = pd.read_csv(full_path)
# all_tasks = df_full.columns[1:]
# print("---->>all tasks", all_tasks)

# X_V, X_feats_V, Y_V, X_T, X_feats_T, Y_T, X_L, Y_L, X_feats_L, X_U, X_feats_U = process_data(
#     is_data_split=True,
#     model="JL",
#     processed_data_path="../data/processed/",
#     version=6,
#     labels="Criticality",
#     test_per=0.15,
#     val_per=0.15,
#     label_per=0.2,
#     seed=42,
#     print_shape=False
# )
# print(X_V, X_feats_V, Y_V, X_T, X_feats_T, Y_T, X_L, Y_L, X_feats_L, X_U, X_feats_U)
# print("Y_V===================>>>", Y_V)
# V_path_pkl='../criticality/result/Criticality.pkl'
# path_json='../criticality/result/Criticality.json'
# subcategory_noisy_labels = PreLabels(name="criticality",
#                                data=X_L,
#                                gold_labels=Y_L,
#                                data_feats=X_feats_L,
#                                rules=rules,
#                                labels_enum=ClassLabels,
#                                num_classes=3)
# subcategory_noisy_labels.generate_pickle(V_path_pkl)
# subcategory_noisy_labels.generate_json(path_json)