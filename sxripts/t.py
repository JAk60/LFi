import enum
from datetime import datetime

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

def create_labeling_function(label, rule , i):
    """
    Generate and return the entire labeling function as a formatted string with the label and rule replaced.
    
    :param label: The classification label (e.g., ClassLabels.Gunfiring)
    :param rule: A single rule string to apply
    :return: String representation of the labeling function
    """
    function_template = f"""
@labeling_function(pre=[convert_to_lower], label={label})
def {label.name}LF{i}(x):
    log_file = f"./csv/{label.name}LF{i}_logs_{{datetime.now().strftime('%Y%m%d')}}.csv"

    result = {label} if extractor.apply_rule(
        '{rule}', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result
"""
    return function_template

# Example: Printing functions for a specific label and a list of rules
rules = ['If the ship must have onboard workshops for repairs.',
'If the workshops must be available for emergency maintenance.',
'If the workshop must be equipped for various repair tasks.',
'If the workshops must be managed for efficiency.',
'If the ship must have emergency workshop capabilities.',
'If the workshops must be secure against damage.',
'If the workshop must be sufficient for high-intensity operations.',
'If the workshops must be coordinated with mission timelines.',
'If the workshops must be managed for cost-effectiveness.',
'If the workshop must be of high quality to ensure system performance.']


label = ClassLabels.WORKSHOP_AVAILABILITY

# Generate and print the function for each rule
print("""import os
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
    Gunfiring = 0
    InterrogationInterception = 1
    MaintenanceScheduling = 2
    MissileFiring = 3
    SearchAndRescue = 4


THRESHOLD = 0.6

# Keywords for classification
trigWord1 = {"fleet", "task force", "maritime operations", "deployment", "patrol", "exercise", "amphibious assault", "maritime security", "maneuvers", "fleet admiral", "base", "aviation", "seaborne operation", "vessel", "blockade", "warfare", "strategy", "surveillance", "convoy", "anti-submarine warfare", "Gunfiring", "mission objectives", "reconnaissance", "domain awareness", "presence", "drills", "escort", "fleet maneuvers", "operations center", "interception","mission","enemy","war", "mission,","mission's"}

trigWord2 = {"Repair", "Overhaul", "Refit", "Inspection", "Service", "Check-up", "Refurbishment", "Restoration", "Tune-up", "Fix", "Upgrade", "Restoration", "Refurbishment", "Inspection", "Overhaul", "Retrofit", "Revamp", "Refurbish", "Tune", "Lubrication", "Cleaning", "Calibration", "Testing", "Adjustment", "Replacement", "Painting", "Welding", "Greasing", "Polishing", "Troubleshooting","maintenance","annual","repair","restoration"}

@preprocessor()
def convert_to_lower(x):
    return x.lower().strip()""")
for i, rule in enumerate(rules, 1):
    print(create_labeling_function(label, rule, i))

print(f"""{label.name}LFS = [
    {label.name}LF1, {label.name}LF2, {label.name}LF3, {label.name}LF4, {label.name}LF5, {label.name}LF6, {label.name}LF7, {label.name}LF8, {label.name}LF9, {label.name}LF10
]""")
