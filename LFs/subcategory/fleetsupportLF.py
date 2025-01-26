# 1. If mission supports maritime operational readiness.

# 2. If operation involves ship maintenance and logistics.

# 3. If objective maintains fleet combat effectiveness.

# 4. If mission requires maritime supply and replenishment.

# 5. If operation supports inter-vessel communication protocols.

# 6. If mission involves strategic naval positioning.

# 7. If objective ensures fleet equipment reliability.

# 8. If operation provides technical support to naval units.

# 9. If mission involves coordination of naval resources.

# 10. If operation supports fleet deployment strategies.

from pickle import TRUE
import numpy as np
import re
import enum
import csv
import logging
from datetime import datetime
import sys

sys.path.append('../../')

from LFs.subcategory import fleetsupportLF
from spear.labeling import labeling_function, ABSTAIN, preprocessor, LFSet

from helper.con_scorer import word_similarity
from helper.mistral import SentenceExtractor

extractor = SentenceExtractor()

class ClassLabels(enum.Enum):
    Combat = 0
    Exercise = 1
    Fleetsupport = 2
    Sortie = 3
    Humanitarian = 4

THRESHOLD = 0.6

# Keywords for classification
trigWord1 = {"fleet", "task force", "maritime operations", "deployment", "patrol", "exercise", "amphibious assault", "maritime security", "maneuvers", "fleet admiral", "base", "aviation", "seaborne operation", "vessel", "blockade", "warfare", "strategy", "surveillance", "convoy", "anti-submarine warfare", "combat", "mission objectives", "reconnaissance", "domain awareness", "presence", "drills", "escort", "fleet maneuvers", "operations center", "interception","mission","enemy","war", "mission,","mission's"}

trigWord2 = {"Repair", "Overhaul", "Refit", "Inspection", "Service", "Check-up", "Refurbishment", "Restoration", "Tune-up", "Fix", "Upgrade", "Restoration", "Refurbishment", "Inspection", "Overhaul", "Retrofit", "Revamp", "Refurbish", "Tune", "Lubrication", "Cleaning", "Calibration", "Testing", "Adjustment", "Replacement", "Painting", "Welding", "Greasing", "Polishing", "Troubleshooting","maintenance","annual","repair","restoration"}

@preprocessor()
def convert_to_lower(x):
    return x.lower().strip()

# Combat Labeling Functions
@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Fleetsupport_LF1(x):
    log_file = f"./csv/Fleetsupport_LF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Fleetsupport if extractor.apply_rule(
        'If mission supports maritime operational readiness.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Fleetsupport_LF2(x):
    log_file = f"./csv/Fleetsupport_LF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Fleetsupport if extractor.apply_rule(
        'If operation involves ship maintenance and logistics.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Fleetsupport_LF3(x):
    log_file = f"./csv/Fleetsupport_LF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Fleetsupport if extractor.apply_rule(
        'If objective maintains fleet combat effectiveness.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Fleetsupport_LF4(x):
    log_file = f"./csv/Fleetsupport_LF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Fleetsupport if extractor.apply_rule(
        'If mission requires maritime supply and replenishment.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Fleetsupport_LF5(x):
    log_file = f"./csv/Fleetsupport_LF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Fleetsupport if extractor.apply_rule(
        'If operation supports inter-vessel communication protocols.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Fleetsupport_LF6(x):
    log_file = f"./csv/Fleetsupport_LF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Fleetsupport if extractor.apply_rule(
        'If mission involves strategic naval positioning.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Fleetsupport_LF7(x):
    log_file = f"./csv/Fleetsupport_LF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Fleetsupport if extractor.apply_rule(
        'If objective ensures fleet equipment reliability.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Fleetsupport_LF8(x):
    log_file = f"./csv/Fleetsupport_LF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Fleetsupport if extractor.apply_rule(
        'If operation provides technical support to naval units.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Fleetsupport_LF9(x):
    log_file = f"./csv/Fleetsupport_LF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Fleetsupport if extractor.apply_rule(
        'If mission involves coordination of naval resources.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Fleetsupport_LF10(x):
    log_file = f"./csv/Fleetsupport_LF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.Fleetsupport if extractor.apply_rule(
        'If operation supports fleet deployment strategies.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result
# Create LFSet and add all labeling functions
Fleetsupport_LFS = [
    Fleetsupport_LF1, Fleetsupport_LF2, Fleetsupport_LF3, Fleetsupport_LF4, Fleetsupport_LF5, Fleetsupport_LF6, Fleetsupport_LF7, Fleetsupport_LF8, Fleetsupport_LF9, Fleetsupport_LF10
]