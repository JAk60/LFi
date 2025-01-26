# If mission is purely observational
# If no direct personnel threat exists
# If routine maritime patrol conducted
# If environmental monitoring is primary goal
# If communication and documentation are key objectives
# If standard navigation protocols are followed
# If civilian maritime safety is focus
# If equipment maintenance is primary task
# If training or simulation exercises conducted
# If standard international maritime law compliance is goal

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

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Low)
def LowCritical_LF1(x):
    log_file = f"./csv/LowCritical_LF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Low if extractor.apply_rule('If mission is purely observational.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Low)
def LowCritical_LF2(x):
    log_file = f"./csv/LowCritical_LF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Low if extractor.apply_rule('If no direct personnel threat exists.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Low)
def LowCritical_LF3(x):
    log_file = f"./csv/LowCritical_LF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Low if extractor.apply_rule('If routine maritime patrol conducted.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Low)
def LowCritical_LF4(x):
    log_file = f"./csv/LowCritical_LF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Low if extractor.apply_rule('If environmental monitoring is primary goal.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Low)
def LowCritical_LF5(x):
    log_file = f"./csv/LowCritical_LF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Low if extractor.apply_rule('If communication and documentation are key objectives.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Low)
def LowCritical_LF6(x):
    log_file = f"./csv/LowCritical_LF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Low if extractor.apply_rule('If standard navigation protocols are followed.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Low)
def LowCritical_LF7(x):
    log_file = f"./csv/LowCritical_LF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Low if extractor.apply_rule('If civilian maritime safety is focus.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Low)
def LowCritical_LF8(x):
    log_file = f"./csv/LowCritical_LF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Low if extractor.apply_rule('If equipment maintenance is primary task.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Low)
def LowCritical_LF9(x):
    log_file = f"./csv/LowCritical_LF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Low if extractor.apply_rule('If training or simulation exercises conducted.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Low)
def LowCritical_LF10(x):
    log_file = f"./csv/LowCritical_LF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.Low if extractor.apply_rule('If standard international maritime law compliance is goal.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

# Collect the labeling functions in a list
Low_Critical_LFS = [
    LowCritical_LF1,
    LowCritical_LF2,
    LowCritical_LF3,
    LowCritical_LF4,
    LowCritical_LF5,
    LowCritical_LF6,
    LowCritical_LF7,
    LowCritical_LF8,
    LowCritical_LF9,
    LowCritical_LF10,
]

