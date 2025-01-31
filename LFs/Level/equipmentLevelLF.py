
from Level import LOGGING_ENABLED
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
    FLEET=0
    SHIP=1
    EQUIPMENT=2


THRESHOLD = 0.6

# Keywords for classification
trigWord1 = {"fleet", "task force", "maritime operations", "deployment", "patrol", "exercise", "amphibious assault", "maritime security", "maneuvers", "fleet admiral", "base", "aviation", "seaborne operation", "vessel", "blockade", "warfare", "strategy",
             "surveillance", "convoy", "anti-submarine warfare", "combat", "mission objectives", "reconnaissance", "domain awareness", "presence", "drills", "escort", "fleet maneuvers", "operations center", "interception", "mission", "enemy", "war", "mission,", "mission's"}

trigWord2 = {"Repair", "Overhaul", "Refit", "Inspection", "Service", "Check-up", "Refurbishment", "Restoration", "Tune-up", "Fix", "Upgrade", "Restoration", "Refurbishment", "Inspection", "Overhaul", "Retrofit", "Revamp",
             "Refurbish", "Tune", "Lubrication", "Cleaning", "Calibration", "Testing", "Adjustment", "Replacement", "Painting", "Welding", "Greasing", "Polishing", "Troubleshooting", "maintenance", "annual", "repair", "restoration"}


@preprocessor()
def convert_to_lower(x):
    return x.lower().strip()

@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def EQUIPMENTLEVEL_LF1(x):

    result = ClassLabels.EQUIPMENT if extractor.apply_rule(
        'If technical maintenance or repair of specific equipment is required.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
            log_file = f"/home/user/IITB/LFi/LFs/Level/csv/EQUIPMENTLEVEL_LF1_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
            with open(log_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def EQUIPMENTLEVEL_LF2(x):

    result = ClassLabels.EQUIPMENT if extractor.apply_rule(
        'If ensuring the operational readiness of specific equipment is necessary.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
            log_file = f"/home/user/IITB/LFi/LFs/Level/csv/EQUIPMENTLEVEL_LF2_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
            with open(log_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def EQUIPMENTLEVEL_LF3(x):

    result = ClassLabels.EQUIPMENT if extractor.apply_rule(
        'If calibration, testing, or diagnostics of specific equipment is needed.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
            log_file = f"/home/user/IITB/LFi/LFs/Level/csv/EQUIPMENTLEVEL_LF3_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
            with open(log_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def EQUIPMENTLEVEL_LF4(x):

    result = ClassLabels.EQUIPMENT if extractor.apply_rule(
        'If conducting safety checks or inspections of specific equipment is essential.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
            log_file = f"/home/user/IITB/LFi/LFs/Level/csv/EQUIPMENTLEVEL_LF4_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
            with open(log_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def EQUIPMENTLEVEL_LF5(x):

    result = ClassLabels.EQUIPMENT if extractor.apply_rule(
        'If establishing or modifying usage protocols for specific equipment is required.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
            log_file = f"/home/user/IITB/LFi/LFs/Level/csv/EQUIPMENTLEVEL_LF5_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
            with open(log_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def EQUIPMENTLEVEL_LF6(x):

    result = ClassLabels.EQUIPMENT if extractor.apply_rule(
        'If managing spare parts or replacement components for specific equipment is necessary.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
            log_file = f"/home/user/IITB/LFi/LFs/Level/csv/EQUIPMENTLEVEL_LF6_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
            with open(log_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def EQUIPMENTLEVEL_LF7(x):

    result = ClassLabels.EQUIPMENT if extractor.apply_rule(
        'If performing emergency repairs or troubleshooting specific equipment is needed.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
            log_file = f"/home/user/IITB/LFi/LFs/Level/csv/EQUIPMENTLEVEL_LF7_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
            with open(log_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def EQUIPMENTLEVEL_LF8(x):

    result = ClassLabels.EQUIPMENT if extractor.apply_rule(
        'If upgrading or modifying specific equipment is required.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
            log_file = f"/home/user/IITB/LFi/LFs/Level/csv/EQUIPMENTLEVEL_LF8_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
            with open(log_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def EQUIPMENTLEVEL_LF9(x):

    result = ClassLabels.EQUIPMENT if extractor.apply_rule(
        'If training personnel on the use and maintenance of specific equipment is necessary.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
            log_file = f"/home/user/IITB/LFi/LFs/Level/csv/EQUIPMENTLEVEL_LF9_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
            with open(log_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def EQUIPMENTLEVEL_LF10(x):

    result = ClassLabels.EQUIPMENT if extractor.apply_rule(
        'If monitoring the performance and efficiency of specific equipment is essential.', x) == True else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
            log_file = f"/home/user/IITB/LFi/LFs/Level/csv/EQUIPMENTLEVEL_LF10_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"
            with open(log_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now(), x, result])

    return result

EQUIPMENTLEVEL_LFS = [
    EQUIPMENTLEVEL_LF1, EQUIPMENTLEVEL_LF2, EQUIPMENTLEVEL_LF3, EQUIPMENTLEVEL_LF4, EQUIPMENTLEVEL_LF5, EQUIPMENTLEVEL_LF6, EQUIPMENTLEVEL_LF7, EQUIPMENTLEVEL_LF8, EQUIPMENTLEVEL_LF9, EQUIPMENTLEVEL_LF10
]