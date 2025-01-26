['If the ship must have advanced radar systems for surveillance.',
'If the ship must be equipped with anti-submarine warfare capabilities.',
'If the ship must have long-range missile systems.',
'If the ship must have advanced communication systems for secure transmissions.',
'If the ship must be capable of conducting amphibious operations.',
'If the ship must have electronic warfare capabilities.',
'If the ship must be equipped with unmanned aerial vehicles (UAVs).',
'If the ship must have medical facilities for emergency care.',
'If the ship must be capable of conducting search and rescue operations.',
'If the ship must have advanced sonar systems for underwater detection.']
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

@labeling_function(pre=[convert_to_lower], label=ClassLabels.CAPABILITY)
def CAPABILITYLF1(x):
    log_file = f"./csv/CAPABILITYLF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CAPABILITY if extractor.apply_rule(
        'If the ship must have advanced radar systems for surveillance.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.CAPABILITY)
def CAPABILITYLF2(x):
    log_file = f"./csv/CAPABILITYLF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CAPABILITY if extractor.apply_rule(
        'If the ship must be equipped with anti-submarine warfare capabilities.', x) == True else ABSTAIN    

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.CAPABILITY)
def CAPABILITYLF3(x):
    log_file = f"./csv/CAPABILITYLF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CAPABILITY if extractor.apply_rule(
        'If the ship must have long-range missile systems.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.CAPABILITY)
def CAPABILITYLF4(x):
    log_file = f"./csv/CAPABILITYLF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CAPABILITY if extractor.apply_rule(
        'If the ship must have advanced communication systems for secure transmissions.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.CAPABILITY)
def CAPABILITYLF5(x):
    log_file = f"./csv/CAPABILITYLF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CAPABILITY if extractor.apply_rule(
        'If the ship must be capable of conducting amphibious operations.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.CAPABILITY)
def CAPABILITYLF6(x):
    log_file = f"./csv/CAPABILITYLF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CAPABILITY if extractor.apply_rule(
        'If the ship must have electronic warfare capabilities.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.CAPABILITY)
def CAPABILITYLF7(x):
    log_file = f"./csv/CAPABILITYLF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CAPABILITY if extractor.apply_rule(
        'If the ship must be equipped with unmanned aerial vehicles (UAVs).', x) == True else ABSTAIN        

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.CAPABILITY)
def CAPABILITYLF8(x):
    log_file = f"./csv/CAPABILITYLF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CAPABILITY if extractor.apply_rule(
        'If the ship must have medical facilities for emergency care.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.CAPABILITY)
def CAPABILITYLF9(x):
    log_file = f"./csv/CAPABILITYLF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CAPABILITY if extractor.apply_rule(
        'If the ship must be capable of conducting search and rescue operations.', x) == True else ABSTAIN   

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.CAPABILITY)
def CAPABILITYLF10(x):
    log_file = f"./csv/CAPABILITYLF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.CAPABILITY if extractor.apply_rule(
        'If the ship must have advanced sonar systems for underwater detection.', x) == True else ABSTAIN    

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

CAPABILITYLFS = [
    CAPABILITYLF1, CAPABILITYLF2, CAPABILITYLF3, CAPABILITYLF4, CAPABILITYLF5, CAPABILITYLF6, CAPABILITYLF7, CAPABILITYLF8, CAPABILITYLF9, CAPABILITYLF10
]