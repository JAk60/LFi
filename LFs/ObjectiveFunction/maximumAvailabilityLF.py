
# 1. If the mission requires prolonged operational readiness over extended periods.  
# 2. If resources must be conserved to sustain availability throughout the mission.  
# 3. If backup systems and redundancy are essential for uninterrupted operations.  
# 4. If personnel rotations are planned to maintain continuous readiness.  
# 5. If mission success depends on minimizing downtime of critical assets.  
# 6. If logistics prioritize steady resupply and resource replenishment.  
# 7. If operational goals emphasize endurance over speed.  
# 8. If systems are designed to handle long-term deployments without failure.  
# 9. If the mission demands adaptability to varying conditions for sustained performance.  
# 10. If maintaining operational presence over time is critical to strategic objectives.  


from LFs import LOGGING_ENABLED
from helper.mistral import SentenceExtractor
from helper.con_scorer import word_similarity
from spear.labeling import labeling_function, ABSTAIN, preprocessor, LFSet
from pickle import TRUE
import numpy as np
import re
import enum
import csv
import logging
from datetime import datetime
import sys


sys.path.append('../../')


extractor = SentenceExtractor()


class ClassLabels(enum.Enum):
    MINIMUM_TIME = 0
    MAXIMUM_AVAILABILITY = 1
    MAXIMUM_CONFORMANCE = 2
    MAXIMUM_RELIABILITY = 3
    MINIMUM_COST = 4
    MINIMUM_DOWNTIME = 5
    MINIMUM_RISK = 6


THRESHOLD = 0.6

# Keywords for classification
trigWord1 = {"fleet", "task force", "maritime operations", "deployment", "patrol", "exercise", "amphibious assault", "maritime security", "maneuvers", "fleet admiral", "base", "aviation", "seaborne operation", "vessel", "blockade", "warfare", "strategy",
             "surveillance", "convoy", "anti-submarine warfare", "combat", "mission objectives", "reconnaissance", "domain awareness", "presence", "drills", "escort", "fleet maneuvers", "operations center", "interception", "mission", "enemy", "war", "mission,", "mission's"}

trigWord2 = {"Repair", "Overhaul", "Refit", "Inspection", "Service", "Check-up", "Refurbishment", "Restoration", "Tune-up", "Fix", "Upgrade", "Restoration", "Refurbishment", "Inspection", "Overhaul", "Retrofit", "Revamp",
             "Refurbish", "Tune", "Lubrication", "Cleaning", "Calibration", "Testing", "Adjustment", "Replacement", "Painting", "Welding", "Greasing", "Polishing", "Troubleshooting", "maintenance", "annual", "repair", "restoration"}


@preprocessor()
def convert_to_lower(x):
    return x.lower().strip()

@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_AVAILABILITY)
def MAXIMUM_AVAILABILITY_LF1(x):

    result = ClassLabels.MAXIMUM_AVAILABILITY if extractor.apply_rule(
        'If the mission requires prolonged operational readiness over extended periods.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MAXIMUM_AVAILABILITY_LF1_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_AVAILABILITY)
def MAXIMUM_AVAILABILITY_LF2(x):

    result = ClassLabels.MAXIMUM_AVAILABILITY if extractor.apply_rule(
        'If resources must be conserved to sustain availability throughout the mission.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MAXIMUM_AVAILABILITY_LF2_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_AVAILABILITY)
def MAXIMUM_AVAILABILITY_LF3(x):

    result = ClassLabels.MAXIMUM_AVAILABILITY if extractor.apply_rule(
        'If backup systems and redundancy are essential for uninterrupted operations.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MAXIMUM_AVAILABILITY_LF3_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_AVAILABILITY)
def MAXIMUM_AVAILABILITY_LF4(x):

    result = ClassLabels.MAXIMUM_AVAILABILITY if extractor.apply_rule(
        'If personnel rotations are planned to maintain continuous readiness.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MAXIMUM_AVAILABILITY_LF4_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_AVAILABILITY)
def MAXIMUM_AVAILABILITY_LF5(x):

    result = ClassLabels.MAXIMUM_AVAILABILITY if extractor.apply_rule(
        'If mission success depends on minimizing downtime of critical assets.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MAXIMUM_AVAILABILITY_LF5_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_AVAILABILITY)
def MAXIMUM_AVAILABILITY_LF6(x):

    result = ClassLabels.MAXIMUM_AVAILABILITY if extractor.apply_rule(
        'If logistics prioritize steady resupply and resource replenishment.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MAXIMUM_AVAILABILITY_LF6_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_AVAILABILITY)
def MAXIMUM_AVAILABILITY_LF7(x):

    result = ClassLabels.MAXIMUM_AVAILABILITY if extractor.apply_rule(
        'If operational goals emphasize endurance over speed.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MAXIMUM_AVAILABILITY_LF7_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_AVAILABILITY)
def MAXIMUM_AVAILABILITY_LF8(x):

    result = ClassLabels.MAXIMUM_AVAILABILITY if extractor.apply_rule(
        'If systems are designed to handle long-term deployments without failure.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MAXIMUM_AVAILABILITY_LF8_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_AVAILABILITY)
def MAXIMUM_AVAILABILITY_LF9(x):

    result = ClassLabels.MAXIMUM_AVAILABILITY if extractor.apply_rule(
        'If the mission demands adaptability to varying conditions for sustained performance.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MAXIMUM_AVAILABILITY_LF9_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_AVAILABILITY)
def MAXIMUM_AVAILABILITY_LF10(x):

    result = ClassLabels.MAXIMUM_AVAILABILITY if extractor.apply_rule(
        'If maintaining operational presence over time is critical to strategic objectives.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MAXIMUM_AVAILABILITY_LF10_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


MAXIMUM_AVAILABILITYLFS = [
    MAXIMUM_AVAILABILITY_LF1, MAXIMUM_AVAILABILITY_LF2, MAXIMUM_AVAILABILITY_LF3, MAXIMUM_AVAILABILITY_LF4, MAXIMUM_AVAILABILITY_LF5, MAXIMUM_AVAILABILITY_LF6, MAXIMUM_AVAILABILITY_LF7, MAXIMUM_AVAILABILITY_LF8, MAXIMUM_AVAILABILITY_LF9, MAXIMUM_AVAILABILITY_LF10
]