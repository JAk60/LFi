import sys
sys.path.append('../../') 
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
@labeling_function(pre=[convert_to_lower], label=ClassLabels.IDENTIFY)
def IDENTIFYACTION_LF1(x):

    result = ClassLabels.IDENTIFY if extractor.apply_rule(
        'If the mission requires identifying potential threats to operations.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/IDENTIFYACTION_LF1_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.IDENTIFY)
def IDENTIFYACTION_LF2(x):

    result = ClassLabels.IDENTIFY if extractor.apply_rule(
        'If key opportunities for improvement must be identified.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/IDENTIFYACTION_LF2_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.IDENTIFY)
def IDENTIFYACTION_LF3(x):

    result = ClassLabels.IDENTIFY if extractor.apply_rule(
        'If critical points of failure need to be identified.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/IDENTIFYACTION_LF3_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.IDENTIFY)
def IDENTIFYACTION_LF4(x):

    result = ClassLabels.IDENTIFY if extractor.apply_rule(
        'If essential resources for mission success must be identified.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/IDENTIFYACTION_LF4_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.IDENTIFY)
def IDENTIFYACTION_LF5(x):

    result = ClassLabels.IDENTIFY if extractor.apply_rule(
        'If key personnel for special assignments need to be identified.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/IDENTIFYACTION_LF5_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.IDENTIFY)
def IDENTIFYACTION_LF6(x):

    result = ClassLabels.IDENTIFY if extractor.apply_rule(
        'If optimal times for mission execution must be identified.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/IDENTIFYACTION_LF6_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.IDENTIFY)
def IDENTIFYACTION_LF7(x):

    result = ClassLabels.IDENTIFY if extractor.apply_rule(
        'If areas requiring additional training need to be identified.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/IDENTIFYACTION_LF7_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.IDENTIFY)
def IDENTIFYACTION_LF8(x):

    result = ClassLabels.IDENTIFY if extractor.apply_rule(
        'If critical systems needing maintenance must be identified.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/IDENTIFYACTION_LF8_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.IDENTIFY)
def IDENTIFYACTION_LF9(x):

    result = ClassLabels.IDENTIFY if extractor.apply_rule(
        'If high-risk zones for operations must be identified.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/IDENTIFYACTION_LF9_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.IDENTIFY)
def IDENTIFYACTION_LF10(x):

    result = ClassLabels.IDENTIFY if extractor.apply_rule(
        'If key stakeholders for collaboration need to be identified.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/IDENTIFYACTION_LF10_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result

IDENTIFY_ACTION_LFS = [
    IDENTIFYACTION_LF1, IDENTIFYACTION_LF2, IDENTIFYACTION_LF3, IDENTIFYACTION_LF4, IDENTIFYACTION_LF5, IDENTIFYACTION_LF6, IDENTIFYACTION_LF7, IDENTIFYACTION_LF8, IDENTIFYACTION_LF9, IDENTIFYACTION_LF10
]