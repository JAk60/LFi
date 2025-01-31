['If the cargo distribution must be evenly balanced to maintain stability.',
'If the load on different decks must be balanced to avoid listing.',
'If the weight distribution affects the ship"s maneuverability.',
'If the load must be balanced to ensure optimal fuel efficiency.',
'If the cargo must be distributed to avoid overloading specific areas.',
'If the load balance is critical for high-speed operations.',
'If the weight distribution affects the ship"s draft and clearance.',
'If the load must be balanced to ensure safety during rough seas.',
'If the cargo distribution must be adjusted for different mission profiles.',
'If the load balance is essential for the stability during combat maneuvers.']

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

@labeling_function(pre=[convert_to_lower], label=ClassLabels.BALANCING_LOADS)
def BALANCING_LOADSLF1(x):
    log_file = f"./csv/BALANCING_LOADSLF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.BALANCING_LOADS if extractor.apply_rule(
        'If the cargo distribution must be evenly balanced to maintain stability.', x) == True else ABSTAIN  
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.BALANCING_LOADS)
def BALANCING_LOADSLF2(x):
    log_file = f"./csv/BALANCING_LOADSLF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.BALANCING_LOADS if extractor.apply_rule(
        'If the load on different decks must be balanced to avoid listing.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.BALANCING_LOADS)
def BALANCING_LOADSLF3(x):
    log_file = f"./csv/BALANCING_LOADSLF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.BALANCING_LOADS if extractor.apply_rule(
        'If the weight distribution affects the ship"s maneuverability.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.BALANCING_LOADS)
def BALANCING_LOADSLF4(x):
    log_file = f"./csv/BALANCING_LOADSLF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.BALANCING_LOADS if extractor.apply_rule(
        'If the load must be balanced to ensure optimal fuel efficiency.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.BALANCING_LOADS)
def BALANCING_LOADSLF5(x):
    log_file = f"./csv/BALANCING_LOADSLF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.BALANCING_LOADS if extractor.apply_rule(
        'If the cargo must be distributed to avoid overloading specific areas.', x) == True else ABSTAIN     
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.BALANCING_LOADS)
def BALANCING_LOADSLF6(x):
    log_file = f"./csv/BALANCING_LOADSLF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.BALANCING_LOADS if extractor.apply_rule(
        'If the load balance is critical for high-speed operations.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.BALANCING_LOADS)
def BALANCING_LOADSLF7(x):
    log_file = f"./csv/BALANCING_LOADSLF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.BALANCING_LOADS if extractor.apply_rule(
        'If the weight distribution affects the ship"s draft and clearance.', x) == True else ABSTAIN        
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.BALANCING_LOADS)
def BALANCING_LOADSLF8(x):
    log_file = f"./csv/BALANCING_LOADSLF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.BALANCING_LOADS if extractor.apply_rule(
        'If the load must be balanced to ensure safety during rough seas.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.BALANCING_LOADS)
def BALANCING_LOADSLF9(x):
    log_file = f"./csv/BALANCING_LOADSLF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.BALANCING_LOADS if extractor.apply_rule(
        'If the cargo distribution must be adjusted for different mission profiles.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.BALANCING_LOADS)
def BALANCING_LOADSLF10(x):
    log_file = f"./csv/BALANCING_LOADSLF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.BALANCING_LOADS if extractor.apply_rule(
        'If the load balance is essential for the stability during combat maneuvers.', x) == True else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result

BALANCING_LOADSLFS = [
    BALANCING_LOADSLF1, BALANCING_LOADSLF2, BALANCING_LOADSLF3, BALANCING_LOADSLF4, BALANCING_LOADSLF5, BALANCING_LOADSLF6, BALANCING_LOADSLF7, BALANCING_LOADSLF8, BALANCING_LOADSLF9, BALANCING_LOADSLF10    
]