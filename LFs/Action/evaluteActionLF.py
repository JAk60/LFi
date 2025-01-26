
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
    EVALUTE=0
    IDENTIFY=1
    SELECT_K_OUT_OF_N=2


THRESHOLD = 0.6

# Keywords for classification
trigWord1 = {"fleet", "task force", "maritime operations", "deployment", "patrol", "exercise", "amphibious assault", "maritime security", "maneuvers", "fleet admiral", "base", "aviation", "seaborne operation", "vessel", "blockade", "warfare", "strategy",
             "surveillance", "convoy", "anti-submarine warfare", "combat", "mission objectives", "reconnaissance", "domain awareness", "presence", "drills", "escort", "fleet maneuvers", "operations center", "interception", "mission", "enemy", "war", "mission,", "mission's"}

trigWord2 = {"Repair", "Overhaul", "Refit", "Inspection", "Service", "Check-up", "Refurbishment", "Restoration", "Tune-up", "Fix", "Upgrade", "Restoration", "Refurbishment", "Inspection", "Overhaul", "Retrofit", "Revamp",
             "Refurbish", "Tune", "Lubrication", "Cleaning", "Calibration", "Testing", "Adjustment", "Replacement", "Painting", "Welding", "Greasing", "Polishing", "Troubleshooting", "maintenance", "annual", "repair", "restoration"}


@preprocessor()
def convert_to_lower(x):
    return x.lower().strip()
@labeling_function(pre=[convert_to_lower], label=ClassLabels.EVALUTE)
def EVALUATEACTION_LF1(x):
    log_file = f"./csv/EVALUATEACTION_LF1_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.EVALUTE if extractor.apply_rule(
        'If the mission requires assessing the effectiveness of current strategies.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EVALUTE)
def EVALUATEACTION_LF2(x):
    log_file = f"./csv/EVALUATEACTION_LF2_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.EVALUTE if extractor.apply_rule(
        'If the performance of critical systems needs to be reviewed.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EVALUTE)
def EVALUATEACTION_LF3(x):
    log_file = f"./csv/EVALUATEACTION_LF3_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.EVALUTE if extractor.apply_rule(
        'If the impact of recent changes or updates must be evaluated.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EVALUTE)
def EVALUATEACTION_LF4(x):
    log_file = f"./csv/EVALUATEACTION_LF4_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.EVALUTE if extractor.apply_rule(
        'If the efficiency of resource allocation needs to be assessed.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EVALUTE)
def EVALUATEACTION_LF5(x):
    log_file = f"./csv/EVALUATEACTION_LF5_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.EVALUTE if extractor.apply_rule(
        'If the readiness of personnel and equipment must be evaluated.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EVALUTE)
def EVALUATEACTION_LF6(x):
    log_file = f"./csv/EVALUATEACTION_LF6_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.EVALUTE if extractor.apply_rule(
        'If the success of ongoing operations needs to be measured.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EVALUTE)
def EVALUATEACTION_LF7(x):
    log_file = f"./csv/EVALUATEACTION_LF7_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.EVALUTE if extractor.apply_rule(
        'If the risks and threats to the mission must be evaluated.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EVALUTE)
def EVALUATEACTION_LF8(x):
    log_file = f"./csv/EVALUATEACTION_LF8_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.EVALUTE if extractor.apply_rule(
        'If the compliance with operational protocols needs to be assessed.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EVALUTE)
def EVALUATEACTION_LF9(x):
    log_file = f"./csv/EVALUATEACTION_LF9_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.EVALUTE if extractor.apply_rule(
        'If the effectiveness of training programs must be evaluated.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EVALUTE)
def EVALUATEACTION_LF10(x):
    log_file = f"./csv/EVALUATEACTION_LF10_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.EVALUTE if extractor.apply_rule(
        'If the overall mission progress needs to be reviewed.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

EVALUATE_ACTION_LFS = [
    EVALUATEACTION_LF1, EVALUATEACTION_LF2, EVALUATEACTION_LF3, EVALUATEACTION_LF4, EVALUATEACTION_LF5, EVALUATEACTION_LF6, EVALUATEACTION_LF7, EVALUATEACTION_LF8, EVALUATEACTION_LF9, EVALUATEACTION_LF10
]