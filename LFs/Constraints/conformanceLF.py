['If the mission must comply with international maritime laws.'
'If the operations must adhere to environmental regulations.'
'If the ship must follow specific navigation routes.'
'If the crew must comply with safety protocols.'
'If the mission must conform to allied nations guidelines.'
'If the ship must adhere to communication blackout periods.'
'If the operations must comply with noise pollution limits.'
'If the ship must follow specific refueling procedures.'
'If the mission must conform to humanitarian aid standards.'
'If the ship must adhere to maintenance schedules.']
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
    ACTIVITY_SEQUENCES = 0
    BALANCING_LOADS = 1
    CAPABILITY = 2
    CONFORMANCE = 3
    ENDURANCE = 4
    FLEET_AVAILABILITY = 5
    FUEL = 6
    LOGISTIC_TIME = 7
    MANPOWER_AVAILABILITY = 8
    RATION = 9
    RELIABILITY = 10
    RISK_SCORE = 11
    SHIP_CLASS = 12
    SPARES_AVAILABILITY = 13
    SPEED = 14
    WORKING_HOURS = 15
    WORKSHOP_AVAILABILITY = 16


THRESHOLD = 0.6

# Keywords for classification
trigWord1 = {"fleet", "task force", "maritime operations", "deployment", "patrol", "exercise", "amphibious assault", "maritime security", "maneuvers", "fleet admiral", "base", "aviation", "seaborne operation", "vessel", "blockade", "warfare", "strategy", "surveillance", "convoy", "anti-submarine warfare", "Gunfiring", "mission objectives", "reconnaissance", "domain awareness", "presence", "drills", "escort", "fleet maneuvers", "operations center", "interception","mission","enemy","war", "mission,","mission's"}

trigWord2 = {"Repair", "Overhaul", "Refit", "Inspection", "Service", "Check-up", "Refurbishment", "Restoration", "Tune-up", "Fix", "Upgrade", "Restoration", "Refurbishment", "Inspection", "Overhaul", "Retrofit", "Revamp", "Refurbish", "Tune", "Lubrication", "Cleaning", "Calibration", "Testing", "Adjustment", "Replacement", "Painting", "Welding", "Greasing", "Polishing", "Troubleshooting","maintenance","annual","repair","restoration"}

@preprocessor()
def convert_to_lower(x):
    return x.lower().strip()

@labeling_function(pre=[convert_to_lower], label=ClassLabels.CONFORMANCE)
def CONFORMANCELF1(x):
    log_file = f"./csv/CONFORMANCELF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CONFORMANCE if extractor.apply_rule(
        'If the mission must comply with international maritime laws.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.CONFORMANCE)
def CONFORMANCELF2(x):
    log_file = f"./csv/CONFORMANCELF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CONFORMANCE if extractor.apply_rule(
        'If the operations must adhere to environmental regulations.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.CONFORMANCE)
def CONFORMANCELF3(x):
    log_file = f"./csv/CONFORMANCELF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CONFORMANCE if extractor.apply_rule(
        'If the ship must follow specific navigation routes.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.CONFORMANCE)
def CONFORMANCELF4(x):
    log_file = f"./csv/CONFORMANCELF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CONFORMANCE if extractor.apply_rule(
        'If the crew must comply with safety protocols.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.CONFORMANCE)
def CONFORMANCELF5(x):
    log_file = f"./csv/CONFORMANCELF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CONFORMANCE if extractor.apply_rule(
        'If the mission must conform to allied nations guidelines.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.CONFORMANCE)
def CONFORMANCELF6(x):
    log_file = f"./csv/CONFORMANCELF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CONFORMANCE if extractor.apply_rule(
        'If the ship must adhere to communication blackout periods.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.CONFORMANCE)
def CONFORMANCELF7(x):
    log_file = f"./csv/CONFORMANCELF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CONFORMANCE if extractor.apply_rule(
        'If the operations must comply with noise pollution limits.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.CONFORMANCE)
def CONFORMANCELF8(x):
    log_file = f"./csv/CONFORMANCELF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CONFORMANCE if extractor.apply_rule(
        'If the ship must follow specific refueling procedures.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.CONFORMANCE)
def CONFORMANCELF9(x):
    log_file = f"./csv/CONFORMANCELF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CONFORMANCE if extractor.apply_rule(
        'If the mission must conform to humanitarian aid standards.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.CONFORMANCE)
def CONFORMANCELF10(x):
    log_file = f"./csv/CONFORMANCELF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CONFORMANCE if extractor.apply_rule(
        'If the ship must adhere to maintenance schedules.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result

CONFORMANCELFS = [
    CONFORMANCELF1, CONFORMANCELF2, CONFORMANCELF3, CONFORMANCELF4, CONFORMANCELF5, CONFORMANCELF6, CONFORMANCELF7, CONFORMANCELF8, CONFORMANCELF9, CONFORMANCELF10
]