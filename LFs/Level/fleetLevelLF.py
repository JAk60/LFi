
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

@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET)
def FLEETLEVEL_LF1(x):
    log_file = f"D:/IITB/LF/LFs/Level/csv/FLEETLEVEL_LF1_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.FLEET if extractor.apply_rule(
        'If the mission requires long-term strategic planning or overall mission objectives.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET)
def FLEETLEVEL_LF2(x):
    log_file = f"D:/IITB/LF/LFs/Level/csv/FLEETLEVEL_LF2_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.FLEET if extractor.apply_rule(
        'If resources must be allocated across multiple ships or units.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET)
def FLEETLEVEL_LF3(x):
    log_file = f"D:/IITB/LF/LFs/Level/csv/FLEETLEVEL_LF3_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.FLEET if extractor.apply_rule(
        'If coordination between multiple ships or units is essential.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET)
def FLEETLEVEL_LF4(x):
    log_file = f"D:/IITB/LF/LFs/Level/csv/FLEETLEVEL_LF4_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.FLEET if extractor.apply_rule(
        'If high-level intelligence or threat assessments affect the entire fleet.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET)
def FLEETLEVEL_LF5(x):
    log_file = f"D:/IITB/LF/LFs/Level/csv/FLEETLEVEL_LF5_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.FLEET if extractor.apply_rule(
        'If major policy changes or new directives impact the entire fleet.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET)
def FLEETLEVEL_LF6(x):
    log_file = f"D:/IITB/LF/LFs/Level/csv/FLEETLEVEL_LF6_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.FLEET if extractor.apply_rule(
        'If managing a crisis affects multiple ships or the entire fleet.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET)
def FLEETLEVEL_LF7(x):
    log_file = f"D:/IITB/LF/LFs/Level/csv/FLEETLEVEL_LF7_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.FLEET if extractor.apply_rule(
        'If planning and executing large-scale operations or missions is necessary.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET)
def FLEETLEVEL_LF8(x):
    log_file = f"D:/IITB/LF/LFs/Level/csv/FLEETLEVEL_LF8_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.FLEET if extractor.apply_rule(
        'If coordination with other agencies or external entities is required.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET)
def FLEETLEVEL_LF9(x):
    log_file = f"D:/IITB/LF/LFs/Level/csv/FLEETLEVEL_LF9_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.FLEET if extractor.apply_rule(
        'If the approval of budgets or financial allocations for the entire fleet is needed.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET)
def FLEETLEVEL_LF10(x):
    log_file = f"D:/IITB/LF/LFs/Level/csv/FLEETLEVEL_LF10_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.FLEET if extractor.apply_rule(
        'If the deployment or reassignment of personnel across multiple ships or units is necessary.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

FLEETLEVEL_LFS = [
    FLEETLEVEL_LF1, FLEETLEVEL_LF2, FLEETLEVEL_LF3, FLEETLEVEL_LF4, FLEETLEVEL_LF5, FLEETLEVEL_LF6, FLEETLEVEL_LF7, FLEETLEVEL_LF8, FLEETLEVEL_LF9, FLEETLEVEL_LF10
]