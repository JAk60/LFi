['If the ship must have sufficient spare parts for maintenance.',
'If the spares must be available for emergency repairs.',
'If the spare parts must be compatible with ship systems.',
'If the spares must be managed for efficiency.',
'If the ship must have emergency spare parts.',
'If the spares must be secure against damage.',
'If the spare parts must be sufficient for high-intensity operations.',
'If the spares must be coordinated with mission timelines.',
'If the spares must be managed for cost-effectiveness.',
'If the spare parts must be of high quality to ensure system performance.']
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

@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPARES_AVAILABILITY)
def SPARES_AVAILABILITYLF1(x):
    log_file = f"./csv/SPARES_AVAILABILITYLF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPARES_AVAILABILITY if extractor.apply_rule(
        'If the ship must have sufficient spare parts for maintenance.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPARES_AVAILABILITY)
def SPARES_AVAILABILITYLF2(x):
    log_file = f"./csv/SPARES_AVAILABILITYLF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPARES_AVAILABILITY if extractor.apply_rule(
        'If the spares must be available for emergency repairs.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPARES_AVAILABILITY)
def SPARES_AVAILABILITYLF3(x):
    log_file = f"./csv/SPARES_AVAILABILITYLF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPARES_AVAILABILITY if extractor.apply_rule(
        'If the spare parts must be compatible with ship systems.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPARES_AVAILABILITY)
def SPARES_AVAILABILITYLF4(x):
    log_file = f"./csv/SPARES_AVAILABILITYLF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPARES_AVAILABILITY if extractor.apply_rule(
        'If the spares must be managed for efficiency.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPARES_AVAILABILITY)
def SPARES_AVAILABILITYLF5(x):
    log_file = f"./csv/SPARES_AVAILABILITYLF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPARES_AVAILABILITY if extractor.apply_rule(
        'If the ship must have emergency spare parts.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPARES_AVAILABILITY)
def SPARES_AVAILABILITYLF6(x):
    log_file = f"./csv/SPARES_AVAILABILITYLF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPARES_AVAILABILITY if extractor.apply_rule(
        'If the spares must be secure against damage.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPARES_AVAILABILITY)
def SPARES_AVAILABILITYLF7(x):
    log_file = f"./csv/SPARES_AVAILABILITYLF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPARES_AVAILABILITY if extractor.apply_rule(
        'If the spare parts must be sufficient for high-intensity operations.', x) == True else ABSTAIN      
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPARES_AVAILABILITY)
def SPARES_AVAILABILITYLF8(x):
    log_file = f"./csv/SPARES_AVAILABILITYLF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPARES_AVAILABILITY if extractor.apply_rule(
        'If the spares must be coordinated with mission timelines.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPARES_AVAILABILITY)
def SPARES_AVAILABILITYLF9(x):
    log_file = f"./csv/SPARES_AVAILABILITYLF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPARES_AVAILABILITY if extractor.apply_rule(
        'If the spares must be managed for cost-effectiveness.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPARES_AVAILABILITY)
def SPARES_AVAILABILITYLF10(x):
    log_file = f"./csv/SPARES_AVAILABILITYLF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPARES_AVAILABILITY if extractor.apply_rule(
        'If the spare parts must be of high quality to ensure system performance.', x) == True else ABSTAIN  
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result

SPARES_AVAILABILITYLFS = [
    SPARES_AVAILABILITYLF1, SPARES_AVAILABILITYLF2, SPARES_AVAILABILITYLF3, SPARES_AVAILABILITYLF4, SPARES_AVAILABILITYLF5, SPARES_AVAILABILITYLF6, SPARES_AVAILABILITYLF7, SPARES_AVAILABILITYLF8, SPARES_AVAILABILITYLF9, SPARES_AVAILABILITYLF10
]