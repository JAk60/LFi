['If the crew must work extended hours for mission success.'
,'If the working hours must be managed for crew health.'
,'If the crew must be available for emergency response.'
,'If the working hours must be coordinated with mission timelines.'
,'If the crew must be prepared for high-intensity operations.'
,'If the working hours must be optimized for efficiency.'
,'If the crew must be available for search and rescue operations.'
,'If the working hours must be managed for cost-effectiveness.'
,'If the crew must be ready for disaster relief operations.'
,'If the working hours must be compatible with crew capabilities.']
import os
import numpy as np
import re
import enum
import csv
import logging
from datetime import datetime
import sys

sys.path.append('../../')

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

@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKING_HOURS)
def WORKING_HOURSLF1(x):
    log_file = f"./csv/WORKING_HOURSLF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.WORKING_HOURS if extractor.apply_rule(
        'If the crew must work extended hours for mission success.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKING_HOURS)
def WORKING_HOURSLF2(x):
    log_file = f"./csv/WORKING_HOURSLF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.WORKING_HOURS if extractor.apply_rule(
        'If the working hours must be managed for crew health.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKING_HOURS)
def WORKING_HOURSLF3(x):
    log_file = f"./csv/WORKING_HOURSLF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.WORKING_HOURS if extractor.apply_rule(
        'If the crew must be available for emergency response.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKING_HOURS)
def WORKING_HOURSLF4(x):
    log_file = f"./csv/WORKING_HOURSLF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.WORKING_HOURS if extractor.apply_rule(
        'If the working hours must be coordinated with mission timelines.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKING_HOURS)
def WORKING_HOURSLF5(x):
    log_file = f"./csv/WORKING_HOURSLF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.WORKING_HOURS if extractor.apply_rule(
        'If the crew must be prepared for high-intensity operations.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKING_HOURS)
def WORKING_HOURSLF6(x):
    log_file = f"./csv/WORKING_HOURSLF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.WORKING_HOURS if extractor.apply_rule(
        'If the working hours must be optimized for efficiency.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKING_HOURS)
def WORKING_HOURSLF7(x):
    log_file = f"./csv/WORKING_HOURSLF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.WORKING_HOURS if extractor.apply_rule(
        'If the crew must be available for search and rescue operations.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKING_HOURS)
def WORKING_HOURSLF8(x):
    log_file = f"./csv/WORKING_HOURSLF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.WORKING_HOURS if extractor.apply_rule(
        'If the working hours must be managed for cost-effectiveness.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKING_HOURS)
def WORKING_HOURSLF9(x):
    log_file = f"./csv/WORKING_HOURSLF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.WORKING_HOURS if extractor.apply_rule(
        'If the crew must be ready for disaster relief operations.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKING_HOURS)
def WORKING_HOURSLF10(x):
    log_file = f"./csv/WORKING_HOURSLF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.WORKING_HOURS if extractor.apply_rule(
        'If the working hours must be compatible with crew capabilities.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

WORKING_HOURSLFS = [
    WORKING_HOURSLF1, WORKING_HOURSLF2, WORKING_HOURSLF3, WORKING_HOURSLF4, WORKING_HOURSLF5, WORKING_HOURSLF6, WORKING_HOURSLF7, WORKING_HOURSLF8, WORKING_HOURSLF9, WORKING_HOURSLF10
]
