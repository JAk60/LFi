[
'If the mission requires synchronized operations across multiple theaters.',
'If the sequence of activities must be strictly adhered to for mission success.',
'If coordination between different naval units is critical.',
'If the timing of actions is crucial for tactical advantage.',
'If the sequence of logistical support must be maintained.',
'If the order of operations affects the outcome of the mission.',
'If the activities must be performed in a specific order to avoid detection.',
'If the sequence of reconnaissance and surveillance is predefined.',
'If the activities must be synchronized with allied forces.',
'If the sequence of activities is dependent on real-time intelligence.'
]

from spear.labeling import labeling_function, ABSTAIN, preprocessor, LFSet
import os
import numpy as np
import re
import enum
import csv
import logging
from datetime import datetime
import sys

sys.path.append('../../')


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

@labeling_function(pre=[convert_to_lower], label=ClassLabels.ACTIVITY_SEQUENCES)
def ACTIVITY_SEQUENCESLF1(x):
    log_file = f"./csv/ACTIVITY_SEQUENCESLF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ACTIVITY_SEQUENCES if extractor.apply_rule(
        'If the mission requires synchronized operations across multiple theaters.', x) == True else ABSTAIN 

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.ACTIVITY_SEQUENCES)
def ACTIVITY_SEQUENCESLF2(x):
    log_file = f"./csv/ACTIVITY_SEQUENCESLF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ACTIVITY_SEQUENCES if extractor.apply_rule(
        'If the sequence of activities must be strictly adhered to for mission success.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.ACTIVITY_SEQUENCES)
def ACTIVITY_SEQUENCESLF3(x):
    log_file = f"./csv/ACTIVITY_SEQUENCESLF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ACTIVITY_SEQUENCES if extractor.apply_rule(
        'If coordination between different naval units is critical.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.ACTIVITY_SEQUENCES)
def ACTIVITY_SEQUENCESLF4(x):
    log_file = f"./csv/ACTIVITY_SEQUENCESLF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ACTIVITY_SEQUENCES if extractor.apply_rule(
        'If the timing of actions is crucial for tactical advantage.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.ACTIVITY_SEQUENCES)
def ACTIVITY_SEQUENCESLF5(x):
    log_file = f"./csv/ACTIVITY_SEQUENCESLF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ACTIVITY_SEQUENCES if extractor.apply_rule(
        'If the sequence of logistical support must be maintained.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.ACTIVITY_SEQUENCES)
def ACTIVITY_SEQUENCESLF6(x):
    log_file = f"./csv/ACTIVITY_SEQUENCESLF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ACTIVITY_SEQUENCES if extractor.apply_rule(
        'If the order of operations affects the outcome of the mission.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.ACTIVITY_SEQUENCES)
def ACTIVITY_SEQUENCESLF7(x):
    log_file = f"./csv/ACTIVITY_SEQUENCESLF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ACTIVITY_SEQUENCES if extractor.apply_rule(
        'If the activities must be performed in a specific order to avoid detection.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.ACTIVITY_SEQUENCES)
def ACTIVITY_SEQUENCESLF8(x):
    log_file = f"./csv/ACTIVITY_SEQUENCESLF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ACTIVITY_SEQUENCES if extractor.apply_rule(
        'If the sequence of reconnaissance and surveillance is predefined.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.ACTIVITY_SEQUENCES)
def ACTIVITY_SEQUENCESLF9(x):
    log_file = f"./csv/ACTIVITY_SEQUENCESLF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ACTIVITY_SEQUENCES if extractor.apply_rule(
        'If the activities must be synchronized with allied forces.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.ACTIVITY_SEQUENCES)
def ACTIVITY_SEQUENCESLF10(x):
    log_file = f"./csv/ACTIVITY_SEQUENCESLF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ACTIVITY_SEQUENCES if extractor.apply_rule(
        'If the sequence of activities is dependent on real-time intelligence.', x) == True else ABSTAIN     

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

ACTIVITY_SEQUENCESLFS = [
    ACTIVITY_SEQUENCESLF1, ACTIVITY_SEQUENCESLF2, ACTIVITY_SEQUENCESLF3, ACTIVITY_SEQUENCESLF4, ACTIVITY_SEQUENCESLF5, ACTIVITY_SEQUENCESLF6, ACTIVITY_SEQUENCESLF7, ACTIVITY_SEQUENCESLF8, ACTIVITY_SEQUENCESLF9, ACTIVITY_SEQUENCESLF10
]