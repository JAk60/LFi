
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
    EQUIPMENT=0
    SHIP=1
    WORKSHOP=2


THRESHOLD = 0.6

# Keywords for classification
trigWord1 = {"fleet", "task force", "maritime operations", "deployment", "patrol", "exercise", "amphibious assault", "maritime security", "maneuvers", "fleet admiral", "base", "aviation", "seaborne operation", "vessel", "blockade", "warfare", "strategy",
             "surveillance", "convoy", "anti-submarine warfare", "combat", "mission objectives", "reconnaissance", "domain awareness", "presence", "drills", "escort", "fleet maneuvers", "operations center", "interception", "mission", "enemy", "war", "mission,", "mission's"}

trigWord2 = {"Repair", "Overhaul", "Refit", "Inspection", "Service", "Check-up", "Refurbishment", "Restoration", "Tune-up", "Fix", "Upgrade", "Restoration", "Refurbishment", "Inspection", "Overhaul", "Retrofit", "Revamp",
             "Refurbish", "Tune", "Lubrication", "Cleaning", "Calibration", "Testing", "Adjustment", "Replacement", "Painting", "Welding", "Greasing", "Polishing", "Troubleshooting", "maintenance", "annual", "repair", "restoration"}


@preprocessor()
def convert_to_lower(x):
    return x.lower().strip()
@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def ENTITY_SHIP_LF1(x):
    log_file = f"D:/IITB/LF/LFs/Entity/csv/ENTITY_SHIP_LF1_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.SHIP if extractor.apply_rule(
        'If the operation involves navigating the Ship through hazardous waters.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def ENTITY_SHIP_LF2(x):
    log_file = f"D:/IITB/LF/LFs/Entity/csv/ENTITY_SHIP_LF2_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.SHIP if extractor.apply_rule(
        'If the Ship needs to be prepared for extended deployments.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def ENTITY_SHIP_LF3(x):
    log_file = f"D:/IITB/LF/LFs/Entity/csv/ENTITY_SHIP_LF3_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.SHIP if extractor.apply_rule(
        'If the Ship requires maintenance to ensure seaworthiness.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def ENTITY_SHIP_LF4(x):
    log_file = f"D:/IITB/LF/LFs/Entity/csv/ENTITY_SHIP_LF4_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.SHIP if extractor.apply_rule(
        'If the Ship must be equipped with advanced communication systems.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def ENTITY_SHIP_LF5(x):
    log_file = f"D:/IITB/LF/LFs/Entity/csv/ENTITY_SHIP_LF5_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.SHIP if extractor.apply_rule(
        'If the Ship needs to be stocked with essential supplies for the mission.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def ENTITY_SHIP_LF6(x):
    log_file = f"D:/IITB/LF/LFs/Entity/csv/ENTITY_SHIP_LF6_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.SHIP if extractor.apply_rule(
        'If the Ship must be manned with trained personnel for specific operations.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def ENTITY_SHIP_LF7(x):
    log_file = f"D:/IITB/LF/LFs/Entity/csv/ENTITY_SHIP_LF7_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.SHIP if extractor.apply_rule(
        'If the Ship requires upgrades to its defensive capabilities.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def ENTITY_SHIP_LF8(x):
    log_file = f"D:/IITB/LF/LFs/Entity/csv/ENTITY_SHIP_LF8_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.SHIP if extractor.apply_rule(
        'If the Ship needs to be inspected for structural integrity.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def ENTITY_SHIP_LF9(x):
    log_file = f"D:/IITB/LF/LFs/Entity/csv/ENTITY_SHIP_LF9_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.SHIP if extractor.apply_rule(
        'If the Ship must be coordinated with other vessels for joint operations.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def ENTITY_SHIP_LF10(x):
    log_file = f"D:/IITB/LF/LFs/Entity/csv/ENTITY_SHIP_LF10_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.SHIP if extractor.apply_rule(
        'If the Ship needs to be positioned strategically for mission success.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

ENTITY_SHIP_LFS = [
    ENTITY_SHIP_LF1, ENTITY_SHIP_LF2, ENTITY_SHIP_LF3, ENTITY_SHIP_LF4, ENTITY_SHIP_LF5, ENTITY_SHIP_LF6, ENTITY_SHIP_LF7, ENTITY_SHIP_LF8, ENTITY_SHIP_LF9, ENTITY_SHIP_LF10
]