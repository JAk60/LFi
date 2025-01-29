
# 1. If the operation involves direct search and rescue efforts.

# 2. If the use of search and rescue teams is authorized for the mission.

# 3. If the target is to be located and rescued immediately.

# 4. If the situation demands urgent search and rescue response.

# 5. If the individuals are within the search area and require rescue.

# 6. If the tactical plan includes coordinated search and rescue efforts.

# 7. If the objective can only be achieved through effective search and rescue.

# 8. If the rules of engagement specify the use of search and rescue methods.

# 9. If the area is equipped with beacons or signals for search and rescue.

# 10. If the mission requires continuous search and rescue to ensure safety.


# 1. If the operation involves direct missile firing.

# 2. If the use of missiles is authorized for the mission.

# 3. If the target is to be neutralized through missile firing.

# 4. If the situation demands immediate missile firing response.

# 5. If the enemy is within missile firing range and poses a threat.

# 6. If the tactical plan includes coordinated missile firing.

# 7. If the objective can only be achieved through missile firing.

# 8. If the rules of engagement specify the use of missile firing.

# 9. If the hostile forces are equipped with missile defense systems.

# 10. If the mission requires suppressive missile firing to advance.





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
    return x.lower().strip()


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SearchAndRescue)
def SearchAndRescueLF1(x):
    log_file = f"D:/IITB/LF/LFs/Task Objective/csv/SearchAndRescueLF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SearchAndRescue if extractor.apply_rule(
        'If the operation involves direct search and rescue efforts.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SearchAndRescue)
def SearchAndRescueLF2(x):
    log_file = f"D:/IITB/LF/LFs/Task Objective/csv/SearchAndRescueLF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SearchAndRescue if extractor.apply_rule(
        'If the use of search and rescue teams is authorized for the mission.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SearchAndRescue)
def SearchAndRescueLF3(x):
    log_file = f"D:/IITB/LF/LFs/Task Objective/csv/SearchAndRescueLF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SearchAndRescue if extractor.apply_rule(
        'If the target is to be located and rescued immediately.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SearchAndRescue)
def SearchAndRescueLF4(x):
    log_file = f"D:/IITB/LF/LFs/Task Objective/csv/SearchAndRescueLF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SearchAndRescue if extractor.apply_rule(
        'If the situation demands urgent search and rescue response.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SearchAndRescue)
def SearchAndRescueLF5(x):
    log_file = f"D:/IITB/LF/LFs/Task Objective/csv/SearchAndRescueLF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SearchAndRescue if extractor.apply_rule(
        'If the individuals are within the search area and require rescue.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SearchAndRescue)
def SearchAndRescueLF6(x):
    log_file = f"D:/IITB/LF/LFs/Task Objective/csv/SearchAndRescueLF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SearchAndRescue if extractor.apply_rule(
        'If the tactical plan includes coordinated search and rescue efforts.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SearchAndRescue)
def SearchAndRescueLF7(x):
    log_file = f"D:/IITB/LF/LFs/Task Objective/csv/SearchAndRescueLF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SearchAndRescue if extractor.apply_rule(
        'If the objective can only be achieved through effective search and rescue.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SearchAndRescue)
def SearchAndRescueLF8(x):
    log_file = f"D:/IITB/LF/LFs/Task Objective/csv/SearchAndRescueLF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SearchAndRescue if extractor.apply_rule(
        'If the rules of engagement specify the use of search and rescue methods.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SearchAndRescue)
def SearchAndRescueLF9(x):
    log_file = f"D:/IITB/LF/LFs/Task Objective/csv/SearchAndRescueLF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SearchAndRescue if extractor.apply_rule(
        'If the area is equipped with beacons or signals for search and rescue.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SearchAndRescue)
def SearchAndRescueLF10(x):
    log_file = f"D:/IITB/LF/LFs/Task Objective/csv/SearchAndRescueLF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = ClassLabels.SearchAndRescue if extractor.apply_rule(
        ' If the mission requires continuous search and rescue to ensure safety.', x) == True else ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


# Create LFSet and add all labeling functions
SearchAndRescueLFS = [
    SearchAndRescueLF1, SearchAndRescueLF2, SearchAndRescueLF3, SearchAndRescueLF4, SearchAndRescueLF5, SearchAndRescueLF6, SearchAndRescueLF7, SearchAndRescueLF8, SearchAndRescueLF9, SearchAndRescueLF10
]
