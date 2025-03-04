import enum
import os

from .activitysequencesLF import ACTIVITY_SEQUENCESLFS
from .balancingloadsLF import BALANCING_LOADSLFS
from .capabilityLF import CAPABILITYLFS
from .conformanceLF import CONFORMANCELFS
from .enduranceLF import ENDURANCELFS
from .fleetavailabilityLF import FLEET_AVAILABILITYLFS
from .fuelLF import FUELLFS
from .logistictimeLF import LOGISTIC_TIMELFS
from .manpoweravailabilityLF import MANPOWER_AVAILABILITYLFS
from .rationLF import RATIONLFS
from .reliabilityLF import RELIABILITYLFS
from .riskscoreLF import RISK_SCORELFS
from .shipclassLF import SHIP_CLASSLFS
from .sparesavailabilityLF import SPARES_AVAILABILITYLFS
from .speedLF import SPEEDLFS
from .workinghoursLF import WORKING_HOURSLFS
from .workshopavailabilityLF import WORKSHOP_AVAILABILITYLFS

print(os.getcwd())


class ClassLabels(enum.Enum):
    ACTIVITY_SEQUENCES = 0
    BALANCING_LOADS = 1
    CAPABILITY = 2
    CONFORMANCE = 3
    ENDURANCE = 4
    FLEET_AVAILABILITY = 5
    FUEL = 6
    LOGISTIC_TIME = 7
    MANPOWER_AVAILABILITY = 8
    RATION = 9
    RELIABILITY = 10
    RISK_SCORE = 11
    SHIP_CLASS = 12
    SPARES_AVAILABILITY = 13
    SPEED = 14
    WORKING_HOURS = 15
    WORKSHOP_AVAILABILITY = 16


THRESHOLD = 0.6

ConstraintsLF = (
    ACTIVITY_SEQUENCESLFS
    + BALANCING_LOADSLFS
    + CAPABILITYLFS
    + CONFORMANCELFS
    + ENDURANCELFS
    + FLEET_AVAILABILITYLFS
    + FUELLFS
    + LOGISTIC_TIMELFS
    + MANPOWER_AVAILABILITYLFS
    + RATIONLFS
    + RELIABILITYLFS
    + RISK_SCORELFS
    + SHIP_CLASSLFS
    + SPARES_AVAILABILITYLFS
    + SPEEDLFS
    + WORKING_HOURSLFS
    + WORKSHOP_AVAILABILITYLFS
)

print(ConstraintsLF)

# rules = LFSet("Constraints_LF")
# rules.add_lf_list(ConstraintsLF)

# from spear.labeling import PreLabels
# from helper.utils import process_data
# import pandas as pd

# # processed_data_path="../LFs/data/processed/"
# full_path = "../../data/processed/version7/full.csv"
# df_full = pd.read_csv(full_path)
# all_tasks = df_full.columns[1:]
# print("---->>all tasks", all_tasks)

# X_V, X_feats_V, Y_V, X_T, X_feats_T, Y_T, X_L, Y_L, X_feats_L, X_U, X_feats_U = process_data(
#     is_data_split=False,
#     model="JL",
#     processed_data_path="../../data/processed/",
#     version=7,
#     labels="Constraints",
#     test_per=0.15,
#     val_per=0.15,
#     label_per=0.2,
#     multilabel=True,
#     seed=42,
#     print_shape=False
# )
# print(X_V, X_feats_V, Y_V, X_T, X_feats_T, Y_T, X_L, Y_L, X_feats_L, X_U, X_feats_U)
# print("Y_V===================>>>", Y_V)
# V_path_pkl='/home/user/IITB/LFi/LFs/Constraints/result/Constraints.pkl'
# path_json='/home/user/IITB/LFi/LFs/Constraints/result/Constraints.json'
# Constraints_noisy_labels = PreLabels(name="constraints",
#                                data=X_T,
#                                gold_labels=Y_T,
#                                data_feats=X_feats_T,
#                                rules=rules,
#                                labels_enum=ClassLabels,
#                                num_classes=17)
# Constraints_noisy_labels.generate_pickle(V_path_pkl)
# Constraints_noisy_labels.generate_json(path_json)
