
# 1. If the mission requires strict adherence to pre-defined protocols and standards.  
# 2. If operational procedures are governed by stringent regulatory requirements.  
# 3. If success depends on following established guidelines without deviation.  
# 4. If mission activities are subject to legal, ethical, or international compliance.  
# 5. If consistency in execution is critical to avoid operational risks.  
# 6. If deviations from the plan compromise mission integrity or outcomes.  
# 7. If reporting and documentation standards must be precisely followed.  
# 8. If collaboration with external entities demands strict conformance to agreements.  
# 9. If operational audits are anticipated, requiring flawless compliance.  
# 10. If mission objectives emphasize uniformity and precision over flexibility.  


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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_CONFORMANCE)
def MAXIMUM_CONFORMANCE_LF1(x):
    log_file = f"./csv/MAXIMUM_CONFORMANCE_LF1_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_CONFORMANCE if extractor.apply_rule(
        'If the mission requires strict adherence to pre-defined protocols and standards.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_CONFORMANCE)
def MAXIMUM_CONFORMANCE_LF2(x):
    log_file = f"./csv/MAXIMUM_CONFORMANCE_LF2_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_CONFORMANCE if extractor.apply_rule(
        'If operational procedures are governed by stringent regulatory requirements.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_CONFORMANCE)
def MAXIMUM_CONFORMANCE_LF3(x):
    log_file = f"./csv/MAXIMUM_CONFORMANCE_LF3_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_CONFORMANCE if extractor.apply_rule(
        'If success depends on following established guidelines without deviation.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_CONFORMANCE)
def MAXIMUM_CONFORMANCE_LF4(x):
    log_file = f"./csv/MAXIMUM_CONFORMANCE_LF4_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_CONFORMANCE if extractor.apply_rule(
        'If mission activities are subject to legal, ethical, or international compliance.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_CONFORMANCE)
def MAXIMUM_CONFORMANCE_LF5(x):
    log_file = f"./csv/MAXIMUM_CONFORMANCE_LF5_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_CONFORMANCE if extractor.apply_rule(
        'If consistency in execution is critical to avoid operational risks.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_CONFORMANCE)
def MAXIMUM_CONFORMANCE_LF6(x):
    log_file = f"./csv/MAXIMUM_CONFORMANCE_LF6_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_CONFORMANCE if extractor.apply_rule(
        'If deviations from the plan compromise mission integrity or outcomes.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_CONFORMANCE)
def MAXIMUM_CONFORMANCE_LF7(x):
    log_file = f"./csv/MAXIMUM_CONFORMANCE_LF7_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_CONFORMANCE if extractor.apply_rule(
        'If reporting and documentation standards must be precisely followed.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_CONFORMANCE)
def MAXIMUM_CONFORMANCE_LF8(x):
    log_file = f"./csv/MAXIMUM_CONFORMANCE_LF8_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_CONFORMANCE if extractor.apply_rule(
        'If collaboration with external entities demands strict conformance to agreements.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_CONFORMANCE)
def MAXIMUM_CONFORMANCE_LF9(x):
    log_file = f"./csv/MAXIMUM_CONFORMANCE_LF9_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_CONFORMANCE if extractor.apply_rule(
        'If operational audits are anticipated, requiring flawless compliance.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MAXIMUM_CONFORMANCE)
def MAXIMUM_CONFORMANCE_LF10(x):
    log_file = f"./csv/MAXIMUM_CONFORMANCE_LF10_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MAXIMUM_CONFORMANCE if extractor.apply_rule(
        'If mission objectives emphasize uniformity and precision over flexibility.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

MAXIMUM_CONFORMANCELFS = [
    MAXIMUM_CONFORMANCE_LF1, MAXIMUM_CONFORMANCE_LF2, MAXIMUM_CONFORMANCE_LF3, MAXIMUM_CONFORMANCE_LF4, MAXIMUM_CONFORMANCE_LF5, MAXIMUM_CONFORMANCE_LF6, MAXIMUM_CONFORMANCE_LF7, MAXIMUM_CONFORMANCE_LF8, MAXIMUM_CONFORMANCE_LF9, MAXIMUM_CONFORMANCE_LF10
]