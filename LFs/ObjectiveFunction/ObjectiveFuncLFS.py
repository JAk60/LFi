import enum

from .maximumAvailabilityLF import MAXIMUM_AVAILABILITYLFS
from .maximumConformanceLF import MAXIMUM_CONFORMANCELFS
from .maximumReliabilityLF import MAXIMUM_RELIABILITY_LFS
from .minimumCostLF import MINIMUM_COST_LFS
from .minimumDowntimeLF import MINIMUM_DOWNTIMELFS
from .minimumRiskLF import MinimumRisk_LFS
from .minimumTimeLF import MinimumTime_LFS


class ClassLabels(enum.Enum):
    MINIMUM_TIME = 0
    MAXIMUM_AVAILABILITY = 1
    MAXIMUM_CONFORMANCE = 2
    MAXIMUM_RELIABILITY = 3
    MINIMUM_COST = 4
    MINIMUM_DOWNTIME = 5
    MINIMUM_RISK = 6


THRESHOLD = 0.6

ObjectiveFunctionLF = (
    MAXIMUM_AVAILABILITYLFS
    + MAXIMUM_CONFORMANCELFS
    + MAXIMUM_RELIABILITY_LFS
    + MINIMUM_COST_LFS
    + MINIMUM_DOWNTIMELFS
    + MinimumRisk_LFS
    + MinimumTime_LFS
)
print(ObjectiveFunctionLF)

# rules = LFSet("Objective function_LF")
# rules.add_lf_list(ObjectiveFuncLF)

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
#     labels="Objective function",
#     test_per=0.15,
#     val_per=0.15,
#     label_per=0.2,
#     seed=42,
#     print_shape=False
# )
# print(X_V, X_feats_V, Y_V, X_T, X_feats_T, Y_T, X_L, Y_L, X_feats_L, X_U, X_feats_U)
# print("Y_V===================>>>", Y_V)
# V_path_pkl='../Objective function/result/Objective function.pkl'
# path_json='../Objective function/result/Objective function.json'
# Objective_function_noisy_labels = PreLabels(name="ObjFunc",
#                                data=X_L,
#                                gold_labels=Y_L,
#                                data_feats=X_feats_L,
#                                rules=rules,
#                                labels_enum=ClassLabels,
#                                num_classes=5)
# Objective_function_noisy_labels.generate_pickle(V_path_pkl)
# Objective_function_noisy_labels.generate_json(path_json)
