
# 1. If the mission requires consistent performance under all conditions.  
# 2. If success depends on minimizing the risk of system or equipment failure.  
# 3. If operational redundancy is critical to ensure uninterrupted functionality.  
# 4. If all mission components must operate within defined tolerances at all times.  
# 5. If mission-critical systems must be thoroughly tested and validated beforehand.  
# 6. If operational plans emphasize robustness over speed or flexibility.  
# 7. If environmental factors demand highly dependable equipment and personnel.  
# 8. If fallback mechanisms are essential to recover from potential failures.  
# 9. If reliability is prioritized to protect lives and mission outcomes.  
# 10. If long-term operational success depends on fault-free execution throughout.  




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


class ClassLabels:
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_RELIABILITY)
def MAXIMUM_RELIABILITY_LF1(x):
    log_file = f"D:/IITB/LF/LFs/ObjectiveFunction/csv/MAXIMUM_RELIABILITY_LF1_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_RELIABILITY if extractor.apply_rule(
        'If the mission requires consistent performance under all conditions.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_RELIABILITY)
def MAXIMUM_RELIABILITY_LF2(x):
    log_file = f"D:/IITB/LF/LFs/ObjectiveFunction/csv/MAXIMUM_RELIABILITY_LF2_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_RELIABILITY if extractor.apply_rule(
        'If success depends on minimizing the risk of system or equipment failure.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_RELIABILITY)
def MAXIMUM_RELIABILITY_LF3(x):
    log_file = f"D:/IITB/LF/LFs/ObjectiveFunction/csv/MAXIMUM_RELIABILITY_LF3_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_RELIABILITY if extractor.apply_rule(
        'If operational redundancy is critical to ensure uninterrupted functionality.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_RELIABILITY)
def MAXIMUM_RELIABILITY_LF4(x):
    log_file = f"D:/IITB/LF/LFs/ObjectiveFunction/csv/MAXIMUM_RELIABILITY_LF4_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_RELIABILITY if extractor.apply_rule(
        'If all mission components must operate within defined tolerances at all times.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_RELIABILITY)
def MAXIMUM_RELIABILITY_LF5(x):
    log_file = f"D:/IITB/LF/LFs/ObjectiveFunction/csv/MAXIMUM_RELIABILITY_LF5_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_RELIABILITY if extractor.apply_rule(
        'If mission-critical systems must be thoroughly tested and validated beforehand.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_RELIABILITY)
def MAXIMUM_RELIABILITY_LF6(x):
    log_file = f"D:/IITB/LF/LFs/ObjectiveFunction/csv/MAXIMUM_RELIABILITY_LF6_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_RELIABILITY if extractor.apply_rule(
        'If operational plans emphasize robustness over speed or flexibility.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_RELIABILITY)
def MAXIMUM_RELIABILITY_LF7(x):
    log_file = f"D:/IITB/LF/LFs/ObjectiveFunction/csv/MAXIMUM_RELIABILITY_LF7_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_RELIABILITY if extractor.apply_rule(
        'If environmental factors demand highly dependable equipment and personnel.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_RELIABILITY)
def MAXIMUM_RELIABILITY_LF8(x):
    log_file = f"D:/IITB/LF/LFs/ObjectiveFunction/csv/MAXIMUM_RELIABILITY_LF8_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_RELIABILITY if extractor.apply_rule(
        'If fallback mechanisms are essential to recover from potential failures.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_RELIABILITY)
def MAXIMUM_RELIABILITY_LF9(x):
    log_file = f"D:/IITB/LF/LFs/ObjectiveFunction/csv/MAXIMUM_RELIABILITY_LF9_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_RELIABILITY if extractor.apply_rule(
        'If reliability is prioritized to protect lives and mission outcomes.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_RELIABILITY)
def MAXIMUM_RELIABILITY_LF10(x):
    log_file = f"D:/IITB/LF/LFs/ObjectiveFunction/csv/MAXIMUM_RELIABILITY_LF10_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_RELIABILITY if extractor.apply_rule(
        'If long-term operational success depends on fault-free execution throughout.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


MAXIMUM_RELIABILITY_LFS = [
    MAXIMUM_RELIABILITY_LF1, MAXIMUM_RELIABILITY_LF2, MAXIMUM_RELIABILITY_LF3, MAXIMUM_RELIABILITY_LF4, MAXIMUM_RELIABILITY_LF5, MAXIMUM_RELIABILITY_LF6, MAXIMUM_RELIABILITY_LF7, MAXIMUM_RELIABILITY_LF8, MAXIMUM_RELIABILITY_LF9, MAXIMUM_RELIABILITY_LF10
]