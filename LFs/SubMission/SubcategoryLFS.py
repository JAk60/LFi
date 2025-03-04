import enum

from .combatLF import Combat_LFS
from .exerciseLF import Exercise_LFS
from .fleetsupportLF import Fleetsupport_LFS
from .humanitarianLF import Humanitarian_LFS
from .sortieLF import Sortie_LFS


class ClassLabels(enum.Enum):
    Combat = 0
    Exercise = 1
    Fleetsupport = 2
    Sortie = 3
    Miscellaneous = 4
    Humanitarian = 5


THRESHOLD = 0.6

SubMissionLF = (
    Combat_LFS + Exercise_LFS + Fleetsupport_LFS + Humanitarian_LFS + Sortie_LFS
)
print(SubMissionLF)

# rules = LFSet("Sub - mission_LF")
# rules.add_lf_list(SubcategoryLF)

# from spear.labeling import PreLabels
# from helper.utils import process_data
# import pandas as pd

# # processed_data_path="../LFs/data/processed/"
# full_path = "/home/user/IITB/LFi/data/processed/version7/full.csv"
# df_full = pd.read_csv(full_path)
# all_tasks = df_full.columns[1:]
# print("---->>all tasks", all_tasks)

# X_V, X_feats_V, Y_V, X_T, X_feats_T, Y_T, X_L, Y_L, X_feats_L, X_U, X_feats_U = process_data(
#     is_data_split=True,
#     model="JL",
#     processed_data_path="./data/processed/",
#     version=6,
#     labels="Sub - mission",
#     test_per=0.15,
#     val_per=0.15,
#     label_per=0.2,
#     seed=42,
#     print_shape=False
# )
# print(X_V, X_feats_V, Y_V, X_T, X_feats_T, Y_T, X_L, Y_L, X_feats_L, X_U, X_feats_U)
# print("Y_V===================>>>", Y_V)
# # V_path_pkl='../SubMission/result/SubMission.pkl'
# # path_json='../SubMission/result/SubMission.json'
# # subcategory_noisy_labels = PreLabels(name="Subcat",
# #                                data=X_L,
# #                                gold_labels=Y_L,
# #                                data_feats=X_feats_L,
# #                                rules=rules,
# #                                labels_enum=ClassLabels,
# #                                num_classes=5)
# # subcategory_noisy_labels.generate_pickle(V_path_pkl)
# # subcategory_noisy_labels.generate_json(path_json)
