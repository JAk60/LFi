['If the ship must maintain high speed for rapid response.',
'If the speed must be optimized for fuel efficiency.',
'If the ship must have the capability for high-speed maneuvers.',
'If the speed must be managed for mission success.',
'If the ship must have emergency speed capabilities.',
'If the speed must be compatible with mission requirements.',
'If the ship must have reliable engines for high speed.',
'If the speed must be timely for emergency situations.',
'If the ship must have speed-efficient hull design.',
'If the speed must be managed for extended missions.']

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

@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPEED)
def SPEEDLF1(x):
    log_file = f"./csv/SPEEDLF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPEED if extractor.apply_rule(
        'If the ship must maintain high speed for rapid response.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPEED)
def SPEEDLF2(x):
    log_file = f"./csv/SPEEDLF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPEED if extractor.apply_rule(
        'If the speed must be optimized for fuel efficiency.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPEED)
def SPEEDLF3(x):
    log_file = f"./csv/SPEEDLF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPEED if extractor.apply_rule(
        'If the ship must have the capability for high-speed maneuvers.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPEED)
def SPEEDLF4(x):
    log_file = f"./csv/SPEEDLF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPEED if extractor.apply_rule(
        'If the speed must be managed for mission success.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPEED)
def SPEEDLF5(x):
    log_file = f"./csv/SPEEDLF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPEED if extractor.apply_rule(
        'If the ship must have emergency speed capabilities.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPEED)
def SPEEDLF6(x):
    log_file = f"./csv/SPEEDLF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPEED if extractor.apply_rule(
        'If the speed must be compatible with mission requirements.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPEED)
def SPEEDLF7(x):
    log_file = f"./csv/SPEEDLF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPEED if extractor.apply_rule(
        'If the ship must have reliable engines for high speed.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPEED)
def SPEEDLF8(x):
    log_file = f"./csv/SPEEDLF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPEED if extractor.apply_rule(
        'If the speed must be timely for emergency situations.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPEED)
def SPEEDLF9(x):
    log_file = f"./csv/SPEEDLF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPEED if extractor.apply_rule(
        'If the ship must have speed-efficient hull design.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SPEED)
def SPEEDLF10(x):
    log_file = f"./csv/SPEEDLF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SPEED if extractor.apply_rule(
        'If the speed must be managed for extended missions.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

SPEEDLFS = [
    SPEEDLF1, SPEEDLF2, SPEEDLF3, SPEEDLF4, SPEEDLF5, SPEEDLF6, SPEEDLF7, SPEEDLF8, SPEEDLF9, SPEEDLF10      
]