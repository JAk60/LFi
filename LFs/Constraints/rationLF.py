['If the ship must have sufficient food supplies for extended missions.',
'If the rations must be balanced for crew health.',
'If the food supplies must be managed for efficiency.',
'If the ship must have emergency rations.',
'If the rations must be compatible with crew dietary requirements.',
'If the food supplies must be secure against spoilage.',
'If the rations must be sufficient for high-intensity operations.',
'If the food supplies must be coordinated with mission timelines.',
'If the rations must be managed for cost-effectiveness.',
'If the food supplies must be of high quality to ensure crew performance.']

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

@labeling_function(pre=[convert_to_lower], label=ClassLabels.RATION)
def RATIONLF1(x):
    log_file = f"./csv/RATIONLF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.RATION if extractor.apply_rule(
        'If the ship must have sufficient food supplies for extended missions.', x) == True else ABSTAIN     
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RATION)
def RATIONLF2(x):
    log_file = f"./csv/RATIONLF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.RATION if extractor.apply_rule(
        'If the rations must be balanced for crew health.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RATION)
def RATIONLF3(x):
    log_file = f"./csv/RATIONLF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.RATION if extractor.apply_rule(
        'If the food supplies must be managed for efficiency.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RATION)
def RATIONLF4(x):
    log_file = f"./csv/RATIONLF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.RATION if extractor.apply_rule(
        'If the ship must have emergency rations.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RATION)
def RATIONLF5(x):
    log_file = f"./csv/RATIONLF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.RATION if extractor.apply_rule(
        'If the rations must be compatible with crew dietary requirements.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RATION)
def RATIONLF6(x):
    log_file = f"./csv/RATIONLF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.RATION if extractor.apply_rule(
        'If the food supplies must be secure against spoilage.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RATION)
def RATIONLF7(x):
    log_file = f"./csv/RATIONLF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.RATION if extractor.apply_rule(
        'If the rations must be sufficient for high-intensity operations.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RATION)
def RATIONLF8(x):
    log_file = f"./csv/RATIONLF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.RATION if extractor.apply_rule(
        'If the food supplies must be coordinated with mission timelines.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RATION)
def RATIONLF9(x):
    log_file = f"./csv/RATIONLF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.RATION if extractor.apply_rule(
        'If the rations must be managed for cost-effectiveness.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RATION)
def RATIONLF10(x):
    log_file = f"./csv/RATIONLF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.RATION if extractor.apply_rule(
        'If the food supplies must be of high quality to ensure crew performance.', x) == True else ABSTAIN  
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result

RATIONLFS = [
    RATIONLF1, RATIONLF2, RATIONLF3, RATIONLF4, RATIONLF5, RATIONLF6, RATIONLF7, RATIONLF8, RATIONLF9, RATIONLF10
]
