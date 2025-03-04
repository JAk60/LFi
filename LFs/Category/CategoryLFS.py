import enum

from .maintenanceLF import MaintenanceLFS
from .missionLF import MissionLFS


class ClassLabels(enum.Enum):
    Maintenance = 0
    Mission = 1


CategoryLF = MaintenanceLFS + MissionLFS
# rules = LFSet("Category_LF")
# rules.add_lf_list(CategoryLF)

# # processed_data_path="../LFs/data/processed/"
# full_path = "../../data/processed/version6/full.csv"
# df_full = pd.read_csv(full_path)
# all_tasks = df_full.columns[1:]
# print("---->>all tasks",all_tasks)

# X_V, X_feats_V, Y_V, X_T, X_feats_T, Y_T, X_L, Y_L, X_feats_L, X_U, X_feats_U = process_data(
#     is_data_split=True,
#     model="JL",
#     processed_data_path="../../data/processed/",
#     version=6,
#     labels="Category",
#     test_per=0.15,
#     val_per=0.15,
#     label_per=0.2,
#     seed=42,
#     print_shape=False
# )
# print(X_V, X_feats_V, Y_V, X_T, X_feats_T, Y_T, X_L, Y_L, X_feats_L, X_U, X_feats_U)
# V_path_pkl='../category/result/output.pkl'
# path_json='../category/result/output.json'
# sms_noisy_labels = PreLabels(name="sms",
#                                data=X_V,
#                                gold_labels=Y_V,
#                                data_feats=X_feats_V,
#                                rules=rules,
#                                labels_enum=ClassLabels,
#                                num_classes=2)
# sms_noisy_labels.generate_pickle(V_path_pkl)
# sms_noisy_labels.generate_json(path_json)
