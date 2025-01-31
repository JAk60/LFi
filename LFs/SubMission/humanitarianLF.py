# 1. If mission addresses immediate human survival needs.

# 2. If operation provides emergency medical assistance.

# 3. If deployment supports population in disaster zones.

# 4. If objective focuses on saving lives and reducing suffering.

# 5. If mission involves distributing critical relief supplies.

# 6. If operation requires minimal military engagement.

# 7. If goal is to protect vulnerable civilian populations.

# 8. If mission follows international humanitarian protocols.

# 9. If operation supports rapid crisis response.

# 10. If objective prioritizes human welfare over military tactics.


from pickle import TRUE
import numpy as np
import re
import enum
import csv
import logging
from datetime import datetime
import sys

sys.path.append('../../')

from LFs import LOGGING_ENABLED
from spear.labeling import labeling_function, ABSTAIN, preprocessor, LFSet

from helper.con_scorer import word_similarity
from helper.mistral import SentenceExtractor

extractor = SentenceExtractor()

class ClassLabels(enum.Enum):
    Combat = 0
    Exercise = 1
    Fleetsupport = 2
    Sortie = 3
    Humanitarian = 4

THRESHOLD = 0.6

# Keywords for classification
trigWord1 = {"fleet", "task force", "maritime operations", "deployment", "patrol", "exercise", "amphibious assault", "maritime security", "maneuvers", "fleet admiral", "base", "aviation", "seaborne operation", "vessel", "blockade", "warfare", "strategy", "surveillance", "convoy", "anti-submarine warfare", "combat", "mission objectives", "reconnaissance", "domain awareness", "presence", "drills", "escort", "fleet maneuvers", "operations center", "interception","mission","enemy","war", "mission,","mission's"}

trigWord2 = {"Repair", "Overhaul", "Refit", "Inspection", "Service", "Check-up", "Refurbishment", "Restoration", "Tune-up", "Fix", "Upgrade", "Restoration", "Refurbishment", "Inspection", "Overhaul", "Retrofit", "Revamp", "Refurbish", "Tune", "Lubrication", "Cleaning", "Calibration", "Testing", "Adjustment", "Replacement", "Painting", "Welding", "Greasing", "Polishing", "Troubleshooting","maintenance","annual","repair","restoration"}

@preprocessor()
def convert_to_lower(x):
    return x.lower().strip()

# Combat Labeling Functions
@labeling_function(pre=[convert_to_lower], label=ClassLabels.Humanitarian)
def Humanitarian_LF1(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Humanitarian_LF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Humanitarian if extractor.apply_rule(
        'If mission addresses immediate human survival needs.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Humanitarian)
def Humanitarian_LF2(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Humanitarian_LF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Humanitarian if extractor.apply_rule(
        'If operation provides emergency medical assistance.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Humanitarian)
def Humanitarian_LF3(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Humanitarian_LF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Humanitarian if extractor.apply_rule(
        'If deployment supports population in disaster zones.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Humanitarian)
def Humanitarian_LF4(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Humanitarian_LF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Humanitarian if extractor.apply_rule(
        'If objective focuses on saving lives and reducing suffering.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Humanitarian)
def Humanitarian_LF5(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Humanitarian_LF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Humanitarian if extractor.apply_rule(
        'If mission involves distributing critical relief supplies.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Humanitarian)
def Humanitarian_LF6(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Humanitarian_LF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Humanitarian if extractor.apply_rule(
        'If operation requires minimal military engagement.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Humanitarian)
def Humanitarian_LF7(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Humanitarian_LF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Humanitarian if extractor.apply_rule(
        'If goal is to protect vulnerable civilian populations.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Humanitarian)
def Humanitarian_LF8(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Humanitarian_LF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Humanitarian if extractor.apply_rule(
        'If mission follows international humanitarian protocols.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Humanitarian)
def Humanitarian_LF9(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Humanitarian_LF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Humanitarian if extractor.apply_rule(
        'If operation supports rapid crisis response.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Humanitarian)
def Humanitarian_LF10(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Humanitarian_LF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Humanitarian if extractor.apply_rule(
        'If objective prioritizes human welfare over military tactics.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result
# Create LFSet and add all labeling functions
Humanitarian_LFS = [
    Humanitarian_LF1, Humanitarian_LF2, Humanitarian_LF3, Humanitarian_LF4, Humanitarian_LF5, Humanitarian_LF6, Humanitarian_LF7, Humanitarian_LF8, Humanitarian_LF9, Humanitarian_LF10
]
