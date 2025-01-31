
# 1. If the operation involves direct interrogation of suspects.

# 2. If the use of interception techniques is authorized for the mission.

# 3. If the target is to be interrogated for critical information.

# 4. If the situation demands immediate interception of communications.

# 5. If the enemy is within interception range and poses a threat.

# 6. If the tactical plan includes coordinated interrogation efforts.

# 7. If the objective can only be achieved through interrogation.

# 8. If the rules of engagement specify the use of interception methods.

# 9. If the hostile forces are equipped with communication devices.

# 10. If the mission requires continuous interception to gather intelligence.


import os
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

import enum

class ClassLabels(enum.Enum):
    Gunfiring = 0
    InterrogationInterception = 1
    MaintenanceScheduling = 2
    MissileFiring = 3
    SearchAndRescue = 4


THRESHOLD = 0.6

# Keywords for classification
trigWord1 = {"fleet", "task force", "maritime operations", "deployment", "patrol", "exercise", "amphibious assault", "maritime security", "maneuvers", "fleet admiral", "base", "aviation", "seaborne operation", "vessel", "blockade", "warfare", "strategy", "surveillance", "convoy", "anti-submarine warfare", "Gunfiring", "mission objectives", "reconnaissance", "domain awareness", "presence", "drills", "escort", "fleet maneuvers", "operations center", "interception","mission","enemy","war", "mission,","mission's"}

trigWord2 = {"Repair", "Overhaul", "Refit", "Inspection", "Service", "Check-up", "Refurbishment", "Restoration", "Tune-up", "Fix", "Upgrade", "Restoration", "Refurbishment", "Inspection", "Overhaul", "Retrofit", "Revamp", "Refurbish", "Tune", "Lubrication", "Cleaning", "Calibration", "Testing", "Adjustment", "Replacement", "Painting", "Welding", "Greasing", "Polishing", "Troubleshooting","maintenance","annual","repair","restoration"}

@preprocessor()
def convert_to_lower(x):
    return x.lower().strip()


@labeling_function(pre=[convert_to_lower], label=ClassLabels.InterrogationInterception)
def InterrogationInterceptionLF1(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/InterrogationInterceptionLF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.InterrogationInterception if extractor.apply_rule(
        'If the operation involves direct interrogation of suspects.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.InterrogationInterception)
def InterrogationInterceptionLF2(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/InterrogationInterceptionLF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.InterrogationInterception if extractor.apply_rule(
        'If the use of interception techniques is authorized for the mission.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.InterrogationInterception)
def InterrogationInterceptionLF3(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/InterrogationInterceptionLF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.InterrogationInterception if extractor.apply_rule(
        'If the target is to be interrogated for critical information.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.InterrogationInterception)
def InterrogationInterceptionLF4(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/InterrogationInterceptionLF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.InterrogationInterception if extractor.apply_rule(
        'If the situation demands immediate interception of communications.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.InterrogationInterception)
def InterrogationInterceptionLF5(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/InterrogationInterceptionLF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.InterrogationInterception if extractor.apply_rule(
        'If the enemy is within interception range and poses a threat.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.InterrogationInterception)
def InterrogationInterceptionLF6(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/InterrogationInterceptionLF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.InterrogationInterception if extractor.apply_rule(
        'If the tactical plan includes coordinated interrogation efforts.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.InterrogationInterception)
def InterrogationInterceptionLF7(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/InterrogationInterceptionLF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.InterrogationInterception if extractor.apply_rule(
        'If the objective can only be achieved through interrogation.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.InterrogationInterception)
def InterrogationInterceptionLF8(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/InterrogationInterceptionLF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.InterrogationInterception if extractor.apply_rule(
        'If the rules of engagement specify the use of interception methods.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.InterrogationInterception)
def InterrogationInterceptionLF9(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/InterrogationInterceptionLF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.InterrogationInterception if extractor.apply_rule(
        'If the hostile forces are equipped with communication devices.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.InterrogationInterception)
def InterrogationInterceptionLF10(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/InterrogationInterceptionLF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.InterrogationInterception if extractor.apply_rule(
        'If the mission requires continuous interception to gather intelligence.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


# Create LFSet and add all labeling functions
InterrogationInterceptionLFS = [
    InterrogationInterceptionLF1, InterrogationInterceptionLF2, InterrogationInterceptionLF3, InterrogationInterceptionLF4, InterrogationInterceptionLF5, InterrogationInterceptionLF6, InterrogationInterceptionLF7, InterrogationInterceptionLF8, InterrogationInterceptionLF9, InterrogationInterceptionLF10
]
