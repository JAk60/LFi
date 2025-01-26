['If the crew must be available for immediate deployment.',
'If the personnel must be ready for emergency response.',
'If the crew must be prepared for sudden combat operations.',
'If the personnel must be available for humanitarian aid missions.',
'If the crew must be ready for joint exercises with allied nations.',
'If the personnel must be available for search and rescue operations.',
'If the crew must be prepared for anti-piracy missions.',
'If the personnel must be available for maritime security patrols.',
'If the crew must be ready for disaster relief operations.',
'If the personnel must be available for escort duties.']

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

@labeling_function(pre=[convert_to_lower], label=ClassLabels.MANPOWER_AVAILABILITY)
def MANPOWER_AVAILABILITYLF1(x):
    log_file = f"./csv/MANPOWER_AVAILABILITYLF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.MANPOWER_AVAILABILITY if extractor.apply_rule(
        'If the crew must be available for immediate deployment.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MANPOWER_AVAILABILITY)
def MANPOWER_AVAILABILITYLF2(x):
    log_file = f"./csv/MANPOWER_AVAILABILITYLF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.MANPOWER_AVAILABILITY if extractor.apply_rule(
        'If the personnel must be ready for emergency response.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MANPOWER_AVAILABILITY)
def MANPOWER_AVAILABILITYLF3(x):
    log_file = f"./csv/MANPOWER_AVAILABILITYLF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.MANPOWER_AVAILABILITY if extractor.apply_rule(
        'If the crew must be prepared for sudden combat operations.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MANPOWER_AVAILABILITY)
def MANPOWER_AVAILABILITYLF4(x):
    log_file = f"./csv/MANPOWER_AVAILABILITYLF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.MANPOWER_AVAILABILITY if extractor.apply_rule(
        'If the personnel must be available for humanitarian aid missions.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MANPOWER_AVAILABILITY)
def MANPOWER_AVAILABILITYLF5(x):
    log_file = f"./csv/MANPOWER_AVAILABILITYLF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.MANPOWER_AVAILABILITY if extractor.apply_rule(
        'If the crew must be ready for joint exercises with allied nations.', x) == True else ABSTAIN        

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MANPOWER_AVAILABILITY)
def MANPOWER_AVAILABILITYLF6(x):
    log_file = f"./csv/MANPOWER_AVAILABILITYLF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.MANPOWER_AVAILABILITY if extractor.apply_rule(
        'If the personnel must be available for search and rescue operations.', x) == True else ABSTAIN      

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MANPOWER_AVAILABILITY)
def MANPOWER_AVAILABILITYLF7(x):
    log_file = f"./csv/MANPOWER_AVAILABILITYLF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.MANPOWER_AVAILABILITY if extractor.apply_rule(
        'If the crew must be prepared for anti-piracy missions.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MANPOWER_AVAILABILITY)
def MANPOWER_AVAILABILITYLF8(x):
    log_file = f"./csv/MANPOWER_AVAILABILITYLF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.MANPOWER_AVAILABILITY if extractor.apply_rule(
        'If the personnel must be available for maritime security patrols.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MANPOWER_AVAILABILITY)
def MANPOWER_AVAILABILITYLF9(x):
    log_file = f"./csv/MANPOWER_AVAILABILITYLF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.MANPOWER_AVAILABILITY if extractor.apply_rule(
        'If the crew must be ready for disaster relief operations.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MANPOWER_AVAILABILITY)
def MANPOWER_AVAILABILITYLF10(x):
    log_file = f"./csv/MANPOWER_AVAILABILITYLF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.MANPOWER_AVAILABILITY if extractor.apply_rule(
        'If the personnel must be available for escort duties.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

MANPOWER_AVAILABILITYLFS = [
    MANPOWER_AVAILABILITYLF1, MANPOWER_AVAILABILITYLF2, MANPOWER_AVAILABILITYLF3, MANPOWER_AVAILABILITYLF4, MANPOWER_AVAILABILITYLF5, MANPOWER_AVAILABILITYLF6, MANPOWER_AVAILABILITYLF7, MANPOWER_AVAILABILITYLF8, MANPOWER_AVAILABILITYLF9, MANPOWER_AVAILABILITYLF10
]
