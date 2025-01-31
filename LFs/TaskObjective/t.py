import enum
from datetime import datetime

class ClassLabels(enum.Enum):
    Gunfiring = 0
    InterrogationInterception = 1
    MaintenanceScheduling = 2
    MissileFiring = 3
    SearchAndRescue = 4

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
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result
"""
    return function_template

# Example: Printing functions for a specific label and a list of rules
rules = [
'If the operation involves direct search and rescue efforts.',
'If the use of search and rescue teams is authorized for the mission.',
'If the target is to be located and rescued immediately.',
'If the situation demands urgent search and rescue response.',
'If the individuals are within the search area and require rescue.',
'If the tactical plan includes coordinated search and rescue efforts.',
'If the objective can only be achieved through effective search and rescue.',
'If the rules of engagement specify the use of search and rescue methods.',
'If the area is equipped with beacons or signals for search and rescue.',
' If the mission requires continuous search and rescue to ensure safety.',
]

label = ClassLabels.SearchAndRescue

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

print(f"""{label}LFS = [
    {label}LF1, {label}LF2, {label}LF3, {label}LF4, {label}LF5, {label}LF6, {label}LF7, {label}LF8, {label}LF9, {label}LF10
]""")
