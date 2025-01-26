['If the ship must have sufficient fuel for long-range missions.',
'If the fuel consumption must be optimized for efficiency.',
'If the ship must have access to refueling points.',
'If the fuel reserves must be managed for extended operations.',
'If the ship must have emergency fuel supplies.',
'If the fuel type must be compatible with mission requirements.',
'If the fuel consumption must be monitored for cost-effectiveness.',
'If the ship must have fuel-efficient engines.',
'If the fuel storage must be secure against leaks.',
'If the fuel must be of high quality to ensure engine performance.']

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

@labeling_function(pre=[convert_to_lower], label=ClassLabels.FUEL)
def FUELLF1(x):
    log_file = f"./csv/FUELLF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.FUEL if extractor.apply_rule(
        'If the ship must have sufficient fuel for long-range missions.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FUEL)
def FUELLF2(x):
    log_file = f"./csv/FUELLF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.FUEL if extractor.apply_rule(
        'If the fuel consumption must be optimized for efficiency.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FUEL)
def FUELLF3(x):
    log_file = f"./csv/FUELLF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.FUEL if extractor.apply_rule(
        'If the ship must have access to refueling points.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FUEL)
def FUELLF4(x):
    log_file = f"./csv/FUELLF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.FUEL if extractor.apply_rule(
        'If the fuel reserves must be managed for extended operations.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FUEL)
def FUELLF5(x):
    log_file = f"./csv/FUELLF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.FUEL if extractor.apply_rule(
        'If the ship must have emergency fuel supplies.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FUEL)
def FUELLF6(x):
    log_file = f"./csv/FUELLF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.FUEL if extractor.apply_rule(
        'If the fuel type must be compatible with mission requirements.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FUEL)
def FUELLF7(x):
    log_file = f"./csv/FUELLF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.FUEL if extractor.apply_rule(
        'If the fuel consumption must be monitored for cost-effectiveness.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FUEL)
def FUELLF8(x):
    log_file = f"./csv/FUELLF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.FUEL if extractor.apply_rule(
        'If the ship must have fuel-efficient engines.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FUEL)
def FUELLF9(x):
    log_file = f"./csv/FUELLF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.FUEL if extractor.apply_rule(
        'If the fuel storage must be secure against leaks.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FUEL)
def FUELLF10(x):
    log_file = f"./csv/FUELLF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.FUEL if extractor.apply_rule(
        'If the fuel must be of high quality to ensure engine performance.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

FUELLFS = [
    FUELLF1, FUELLF2, FUELLF3, FUELLF4, FUELLF5, FUELLF6, FUELLF7, FUELLF8, FUELLF9, FUELLF10
]