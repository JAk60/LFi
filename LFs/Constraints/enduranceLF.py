['If the ship must sustain operations for extended periods without resupply.',
'If the crew must endure long durations at sea.',
'If the ship must have sufficient fuel reserves for prolonged missions.',
'If the ship must be capable of continuous surveillance for weeks.',
'If the ship must endure harsh weather conditions.',
'If the crew must maintain high alertness for extended periods.',
'If the ship must have reliable power generation for long missions.',
'If the ship must endure prolonged exposure to enemy threats.',
'If the ship must have sufficient provisions for extended voyages.',
'If the ship must endure continuous operational tempo.',]

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

@labeling_function(pre=[convert_to_lower], label=ClassLabels.ENDURANCE)
def ENDURANCELF1(x):
    log_file = f"./csv/ENDURANCELF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ENDURANCE if extractor.apply_rule(
        'If the ship must sustain operations for extended periods without resupply.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.ENDURANCE)
def ENDURANCELF2(x):
    log_file = f"./csv/ENDURANCELF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ENDURANCE if extractor.apply_rule(
        'If the crew must endure long durations at sea.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.ENDURANCE)
def ENDURANCELF3(x):
    log_file = f"./csv/ENDURANCELF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ENDURANCE if extractor.apply_rule(
        'If the ship must have sufficient fuel reserves for prolonged missions.', x) == True else ABSTAIN    

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.ENDURANCE)
def ENDURANCELF4(x):
    log_file = f"./csv/ENDURANCELF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ENDURANCE if extractor.apply_rule(
        'If the ship must be capable of continuous surveillance for weeks.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.ENDURANCE)
def ENDURANCELF5(x):
    log_file = f"./csv/ENDURANCELF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ENDURANCE if extractor.apply_rule(
        'If the ship must endure harsh weather conditions.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.ENDURANCE)
def ENDURANCELF6(x):
    log_file = f"./csv/ENDURANCELF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ENDURANCE if extractor.apply_rule(
        'If the crew must maintain high alertness for extended periods.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.ENDURANCE)
def ENDURANCELF7(x):
    log_file = f"./csv/ENDURANCELF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ENDURANCE if extractor.apply_rule(
        'If the ship must have reliable power generation for long missions.', x) == True else ABSTAIN        

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.ENDURANCE)
def ENDURANCELF8(x):
    log_file = f"./csv/ENDURANCELF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ENDURANCE if extractor.apply_rule(
        'If the ship must endure prolonged exposure to enemy threats.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.ENDURANCE)
def ENDURANCELF9(x):
    log_file = f"./csv/ENDURANCELF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ENDURANCE if extractor.apply_rule(
        'If the ship must have sufficient provisions for extended voyages.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.ENDURANCE)
def ENDURANCELF10(x):
    log_file = f"./csv/ENDURANCELF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.ENDURANCE if extractor.apply_rule(
        'If the ship must endure continuous operational tempo.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

ENDURANCELFS = [
    ENDURANCELF1, ENDURANCELF2, ENDURANCELF3, ENDURANCELF4, ENDURANCELF5, ENDURANCELF6, ENDURANCELF7, ENDURANCELF8, ENDURANCELF9, ENDURANCELF10
]