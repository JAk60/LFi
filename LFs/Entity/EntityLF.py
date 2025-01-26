from shipEntityLF import ENTITY_SHIP_LFS
from workShopEntityLF import ENTITY_WORKSHOP_LFS
from equipmentEntityLF import ENTITY_EQUIPMENT_LFS

import enum
from spear.labeling import labeling_function, ABSTAIN, preprocessor, LFSet

class ClassLabels:
    EVALUTE=0
    iDENTIFY=1
    SELECT_K_OUT_OF_N=2

THRESHOLD = 0.6

EntityLF = ENTITY_SHIP_LFS + ENTITY_WORKSHOP_LFS +ENTITY_EQUIPMENT_LFS
print(EntityLF)

rules = LFSet("Entity_LF")
rules.add_lf_list(EntityLF)

from spear.labeling import PreLabels
from helper.utils import process_data
import pandas as pd

# processed_data_path="../LFs/data/processed/"
full_path = "../data/processed/version6/full.csv"
df_full = pd.read_csv(full_path)
all_tasks = df_full.columns[1:]
print("---->>all tasks", all_tasks)

X_V, X_feats_V, Y_V, X_T, X_feats_T, Y_T, X_L, Y_L, X_feats_L, X_U, X_feats_U = process_data(
    is_data_split=True,
    model="JL",
    processed_data_path="../data/processed/",
    version=6,
    labels="Entity",
    test_per=0.15,
    val_per=0.15,
    label_per=0.2,
    seed=42,
    print_shape=False
)
print(X_V, X_feats_V, Y_V, X_T, X_feats_T, Y_T, X_L, Y_L, X_feats_L, X_U, X_feats_U)
print("Y_V===================>>>", Y_V)
V_path_pkl='../Entity/result/Entity.pkl'
path_json='../Entity/result/Entity.json'
Entity_noisy_labels = PreLabels(name="entity",
                               data=X_L,
                               gold_labels=Y_L,
                               data_feats=X_feats_L,
                               rules=rules,
                               labels_enum=ClassLabels,
                               num_classes=5)
Entity_noisy_labels.generate_pickle(V_path_pkl)
Entity_noisy_labels.generate_json(path_json)