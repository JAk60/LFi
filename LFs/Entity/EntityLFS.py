import enum

from .equipmentEntityLF import ENTITY_EQUIPMENT_LFS
from .shipEntityLF import ENTITY_SHIP_LFS
from .workShopEntityLF import ENTITY_WORKSHOP_LFS


class ClassLabels(enum.Enum):
    EQUIPMENT = 0
    SHIP = 1
    WORKSHOP = 2


THRESHOLD = 0.6

EntityLF = ENTITY_SHIP_LFS + ENTITY_WORKSHOP_LFS + ENTITY_EQUIPMENT_LFS
print(EntityLF)

# rules = LFSet("Entity_LF")
# rules.add_lf_list(EntityLF)

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
#     processed_data_path="/home/user/IITB/LFi/data/processed/",
#     version=6,
#     labels="Entity",
#     test_per=0.15,
#     val_per=0.15,
#     label_per=0.2,
#     multilabel=False,
#     seed=42,
#     print_shape=False
# )
# print(X_V, X_feats_V, Y_V, X_T, X_feats_T, Y_T, X_L, Y_L, X_feats_L, X_U, X_feats_U)
# print("Y_V===================>>>", Y_V)
# V_path_pkl='../Entity/result/Entity.pkl'
# path_json='../Entity/result/Entity.json'
# V_path_pkl='../criticality/result/Criticality.pkl'
# path_json='../criticality/result/Criticality.json'
# labeling_path = f"/home/user/IITB/LFi/LFs/results"
# full_labeling = os.path.join(labeling_path, f"Criticality.csv")
# V_path_labeling = os.path.join(labeling_path, f"Criticality_V.csv")
# T_path_labeling = os.path.join(labeling_path, f"Criticality_T.csv")
# L_path_labeling = os.path.join(labeling_path, f"Criticality_L.csv")
# U_path_labeling = os.path.join(labeling_path, f"Entity_U.csv")
# fig_path = f"/home/user/IITB/LFi/LFs/results"
# all_task_plot = f"/home/user/IITB/LFi/LFs/results/Criticality.png"
# full_plot = os.path.join(fig_path, f"Criticality.png")
# V_path_plot = os.path.join(fig_path, f"Criticality_V.png")
# T_path_plot = os.path.join(fig_path, f"Criticality_T.png")
# L_path_plot = os.path.join(fig_path, f"Criticality_L.png")
# U_path_plot = "/home/user/IITB/LFi/LFs/results/Entity_U.png"
# Entity_noisy_labels = PreLabels(name="entity",
#                                data=X_L,
#                                gold_labels=Y_L,
#                                data_feats=X_feats_L,
#                                rules=rules,
#                                labels_enum=ClassLabels,
#                                num_classes=len(ClassLabels))
# analyse = Entity_noisy_labels.analyse_lfs(plot=True)
# # display(analyse)
# analyse.to_csv(U_path_labeling, index =False)
# plot_df_bar(df=analyse, mode =  "aggregate" , fig_path = U_path_plot)
# # Entity_noisy_labels.generate_pickle(V_path_pkl)
# # Entity_noisy_labels.generate_json(path_json)
