from .identifyActionLF import IDENTIFY_ACTION_LFS
from .selectKoutofNLF import SELECT_K_OUT_OF_N_ACTION_LFS
from .evaluteActionLF import EVALUATE_ACTION_LFS
import sys
sys.path.append('../../')
import enum
from spear.labeling import labeling_function, ABSTAIN, preprocessor, LFSet
import os
print(os.getcwd())

class ClassLabels(enum.Enum):
    EVALUTE = 0
    iDENTIFY = 1
    SELECT_K_OUT_OF_N = 2

THRESHOLD = 0.6

ActionLF = SELECT_K_OUT_OF_N_ACTION_LFS + IDENTIFY_ACTION_LFS +EVALUATE_ACTION_LFS
print(ActionLF)

# rules = LFSet("Action_LF")
# rules.add_lf_list(ActionLF)

# from spear.labeling import PreLabels
# from helper.utils import process_data
# import pandas as pd

# # processed_data_path="../LFs/data/processed/"
# full_path = "../../data/processed/version6/full.csv"
# df_full = pd.read_csv(full_path)
# all_tasks = df_full.columns[1:]
# print("---->>all tasks", all_tasks)

# X_V, X_feats_V, Y_V, X_T, X_feats_T, Y_T, X_L, Y_L, X_feats_L, X_U, X_feats_U = process_data(
#     is_data_split=True,
#     model="JL",
#     processed_data_path="../../data/processed/",
#     version=6,
#     labels="Action",
#     test_per=0.15,
#     val_per=0.15,
#     label_per=0.2,
#     seed=42,
#     print_shape=False
# )
# print(X_V, X_feats_V, Y_V, X_T, X_feats_T, Y_T, X_L, Y_L, X_feats_L, X_U, X_feats_U)
# print("Y_V===================>>>", Y_V)
# V_path_pkl='../Action/result/Action.pkl'
# path_json='../Action/result/Action.json'
# Action_noisy_labels = PreLabels(name="action",
#                                data=X_L,
#                                gold_labels=Y_L,
#                                data_feats=X_feats_L,
#                                rules=rules,
#                                labels_enum=ClassLabels,
#                                num_classes=3)
# Action_noisy_labels.generate_pickle(V_path_pkl)
# Action_noisy_labels.generate_json(path_json)