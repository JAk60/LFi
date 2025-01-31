# If diplomatic resolution is still possible
# If potential conflict exists without direct engagement
# If strategic positioning requires cautionary measures
# If military presence serves as deterrence
# If intelligence gathering is primary objective
# If limited military intervention might be required
# If monitoring high-risk zones is necessary
# If potential escalation risk is moderate
# If protective security deployment is needed
# If maritime territorial integrity is challenged

import re
import enum
import csv
import logging
from datetime import datetime
import sys


sys.path.append('../../')

from spear.labeling import labeling_function, ABSTAIN, preprocessor, LFSet

from helper.con_scorer import word_similarity
from helper.mistral import SentenceExtractor

extractor = SentenceExtractor()

import enum
class ClassLabels(enum.Enum):
    High = 0
    Mid = 1
    Low = 2

THRESHOLD = 0.6

# Keywords for classification
trigWord1 = {"fleet", "task force", "maritime operations", "deployment", "patrol", "exercise", "amphibious assault", "maritime security", "maneuvers", "fleet admiral", "base", "aviation", "seaborne operation", "vessel", "blockade", "warfare", "strategy", "surveillance", "convoy", "anti-submarine warfare", "combat", "mission objectives", "reconnaissance", "domain awareness", "presence", "drills", "escort", "fleet maneuvers", "operations center", "interception","mission","enemy","war", "mission,","mission's"}

trigWord2 = {"Repair", "Overhaul", "Refit", "Inspection", "Service", "Check-up", "Refurbishment", "Restoration", "Tune-up", "Fix", "Upgrade", "Restoration", "Refurbishment", "Inspection", "Overhaul", "Retrofit", "Revamp", "Refurbish", "Tune", "Lubrication", "Cleaning", "Calibration", "Testing", "Adjustment", "Replacement", "Painting", "Welding", "Greasing", "Polishing", "Troubleshooting","maintenance","annual","repair","restoration"}

@preprocessor()
def convert_to_lower(x):
    return x.lower().strip()

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mid)
def MidCritical_LF1(x):
    # log_file = f"/home/user/IITB/LFi/LFs/Criticality/csv/MidCritical_LF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Mid if extractor.apply_rule('If diplomatic resolution is still possible.', x) else ABSTAIN
    # with open(log_file, 'a', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mid)
def MidCritical_LF2(x):
    # log_file = f"/home/user/IITB/LFi/LFs/Criticality/csv/MidCritical_LF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Mid if extractor.apply_rule('If potential conflict exists without direct engagement.', x) else ABSTAIN
    # with open(log_file, 'a', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mid)
def MidCritical_LF3(x):
    # log_file = f"/home/user/IITB/LFi/LFs/Criticality/csv/MidCritical_LF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Mid if extractor.apply_rule('If strategic positioning requires cautionary measures.', x) else ABSTAIN
    # with open(log_file, 'a', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mid)
def MidCritical_LF4(x):
    # log_file = f"/home/user/IITB/LFi/LFs/Criticality/csv/MidCritical_LF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Mid if extractor.apply_rule('If military presence serves as deterrence.', x) else ABSTAIN
    # with open(log_file, 'a', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mid)
def MidCritical_LF5(x):
    # log_file = f"/home/user/IITB/LFi/LFs/Criticality/csv/MidCritical_LF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Mid if extractor.apply_rule('If intelligence gathering is primary objective.', x) else ABSTAIN
    # with open(log_file, 'a', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mid)
def MidCritical_LF6(x):
    # log_file = f"/home/user/IITB/LFi/LFs/Criticality/csv/MidCritical_LF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Mid if extractor.apply_rule('If limited military intervention might be required.', x) else ABSTAIN
    # with open(log_file, 'a', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mid)
def MidCritical_LF7(x):
    # log_file = f"/home/user/IITB/LFi/LFs/Criticality/csv/MidCritical_LF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Mid if extractor.apply_rule('If monitoring high-risk zones is necessary.', x) else ABSTAIN
    # with open(log_file, 'a', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mid)
def MidCritical_LF8(x):
    # log_file = f"/home/user/IITB/LFi/LFs/Criticality/csv/MidCritical_LF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Mid if extractor.apply_rule('If potential escalation risk is moderate.', x) else ABSTAIN
    # with open(log_file, 'a', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mid)
def MidCritical_LF9(x):
    # log_file = f"/home/user/IITB/LFi/LFs/Criticality/csv/MidCritical_LF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Mid if extractor.apply_rule('If protective security deployment is needed.', x) else ABSTAIN
    # with open(log_file, 'a', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mid)
def MidCritical_LF10(x):
    # log_file = f"/home/user/IITB/LFi/LFs/Criticality/csv/MidCritical_LF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Mid if extractor.apply_rule('If maritime territorial integrity is challenged.', x) else ABSTAIN
    # with open(log_file, 'a', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([datetime.now(), x, result])
    return result

# Collect the labeling functions in a list
Mid_Critical_LFS = [
    MidCritical_LF1,
    MidCritical_LF2,
    MidCritical_LF3,
    MidCritical_LF4,
    MidCritical_LF5,
    MidCritical_LF6,
    MidCritical_LF7,
    MidCritical_LF8,
    MidCritical_LF9,
    MidCritical_LF10,
]

