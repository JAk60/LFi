# If direct lethal combat is imminent
# If nuclear weapons are involved
# If mission requires immediate enemy neutralization
# If personnel face immediate life-threatening risks
# If strategic military assets are under direct threat
# If enemy combatants are actively engaging
# If mission involves capturing high-value military targets
# If precision strikes against critical infrastructure required
# If potential for mass casualty scenario exists
# If total military force projection is necessary

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

@labeling_function(pre=[convert_to_lower], label=ClassLabels.High)
def HighCritical_LF1(x):
    log_file = f"D:/IITB/LF/LFs/Criticality/csv/HighCritical_LF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.High if extractor.apply_rule('If direct lethal combat is imminent.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.High)
def HighCritical_LF2(x):
    log_file = f"D:/IITB/LF/LFs/Criticality/csv/HighCritical_LF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.High if extractor.apply_rule('If nuclear weapons are involved.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.High)
def HighCritical_LF3(x):
    log_file = f"D:/IITB/LF/LFs/Criticality/csv/HighCritical_LF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.High if extractor.apply_rule('If mission requires immediate enemy neutralization.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.High)
def HighCritical_LF4(x):
    log_file = f"D:/IITB/LF/LFs/Criticality/csv/HighCritical_LF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.High if extractor.apply_rule('If personnel face immediate life-threatening risks.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.High)
def HighCritical_LF5(x):
    log_file = f"D:/IITB/LF/LFs/Criticality/csv/HighCritical_LF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.High if extractor.apply_rule('If strategic military assets are under direct threat.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.High)
def HighCritical_LF6(x):
    log_file = f"D:/IITB/LF/LFs/Criticality/csv/HighCritical_LF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.High if extractor.apply_rule('If enemy combatants are actively engaging.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.High)
def HighCritical_LF7(x):
    log_file = f"D:/IITB/LF/LFs/Criticality/csv/HighCritical_LF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.High if extractor.apply_rule('If mission involves capturing high-value military targets.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.High)
def HighCritical_LF8(x):
    log_file = f"D:/IITB/LF/LFs/Criticality/csv/HighCritical_LF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.High if extractor.apply_rule('If precision strikes against critical infrastructure required.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.High)
def HighCritical_LF9(x):
    log_file = f"D:/IITB/LF/LFs/Criticality/csv/HighCritical_LF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.High if extractor.apply_rule('If potential for mass casualty scenario exists.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.High)
def HighCritical_LF10(x):
    log_file = f"D:/IITB/LF/LFs/Criticality/csv/HighCritical_LF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result = ClassLabels.High if extractor.apply_rule('If total military force projection is necessary.', x) else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])
    return result

# Collect the labeling functions in a list
High_Critical_LFS = [
    HighCritical_LF1,
    HighCritical_LF2,
    HighCritical_LF3,
    HighCritical_LF4,
    HighCritical_LF5,
    HighCritical_LF6,
    HighCritical_LF7,
    HighCritical_LF8,
    HighCritical_LF9,
    HighCritical_LF10,
]

