
# 1. If the mission requires continuous operation without extended breaks or interruptions.  
# 2. If the success of the mission is contingent upon maintaining high system uptime.  
# 3. If quick recovery or repair times are essential for sustaining mission operations.  
# 4. If there are critical time windows where downtime must be minimized to avoid mission failure.  
# 5. If personnel or equipment must be on standby for immediate redeployment to reduce idle time.  
# 6. If operational schedules emphasize rapid turnarounds and swift restarts after delays.  
# 7. If mission tasks must be completed with minimal time spent on maintenance or troubleshooting.  
# 8. If any downtime is proactively planned for and minimized during off-peak periods.  
# 9. If alternate systems or redundancies are in place to ensure continuous operation during failures.  
# 10. If mission objectives prioritize maintaining momentum and reducing delays at all stages.  

from helper.mistral import SentenceExtractor
from helper.con_scorer import word_similarity
from spear.labeling import labeling_function, ABSTAIN, preprocessor, LFSet
from pickle import TRUE
import numpy as np
import re
import enum
import csv
import logging
from datetime import datetime
import sys


sys.path.append('../../')


extractor = SentenceExtractor()


class ClassLabels:
    MINIMUM_TIME = 0
    MAXIMUM_AVAILABILITY = 1
    MAXIMUM_CONFORMANCE = 2
    MAXIMUM_RELIABILITY = 3
    MINIMUM_COST = 4
    MINIMUM_DOWNTIME = 5
    MINIMUM_RISK = 6


THRESHOLD = 0.6

# Keywords for classification
trigWord1 = {"fleet", "task force", "maritime operations", "deployment", "patrol", "exercise", "amphibious assault", "maritime security", "maneuvers", "fleet admiral", "base", "aviation", "seaborne operation", "vessel", "blockade", "warfare", "strategy",
             "surveillance", "convoy", "anti-submarine warfare", "combat", "mission objectives", "reconnaissance", "domain awareness", "presence", "drills", "escort", "fleet maneuvers", "operations center", "interception", "mission", "enemy", "war", "mission,", "mission's"}

trigWord2 = {"Repair", "Overhaul", "Refit", "Inspection", "Service", "Check-up", "Refurbishment", "Restoration", "Tune-up", "Fix", "Upgrade", "Restoration", "Refurbishment", "Inspection", "Overhaul", "Retrofit", "Revamp",
             "Refurbish", "Tune", "Lubrication", "Cleaning", "Calibration", "Testing", "Adjustment", "Replacement", "Painting", "Welding", "Greasing", "Polishing", "Troubleshooting", "maintenance", "annual", "repair", "restoration"}


@preprocessor()
def convert_to_lower(x):
    return x.lower().strip()

@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_DOWNTIME)
def MINIMUM_DOWNTIME_LF1(x):
    log_file = f"./csv/MINIMUM_DOWNTIME_LF1_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MINIMUM_DOWNTIME if extractor.apply_rule(
        'If the mission requires continuous operation without extended breaks or interruptions.', x) == True else ClassLabels.ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_DOWNTIME)
def MINIMUM_DOWNTIME_LF2(x):
    log_file = f"./csv/MINIMUM_DOWNTIME_LF2_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MINIMUM_DOWNTIME if extractor.apply_rule(
        'If the success of the mission is contingent upon maintaining high system uptime.', x) == True else ClassLabels.ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_DOWNTIME)
def MINIMUM_DOWNTIME_LF3(x):
    log_file = f"./csv/MINIMUM_DOWNTIME_LF3_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MINIMUM_DOWNTIME if extractor.apply_rule(
        'If quick recovery or repair times are essential for sustaining mission operations.', x) == True else ClassLabels.ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_DOWNTIME)
def MINIMUM_DOWNTIME_LF4(x):
    log_file = f"./csv/MINIMUM_DOWNTIME_LF4_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MINIMUM_DOWNTIME if extractor.apply_rule(
        'If there are critical time windows where downtime must be minimized to avoid mission failure.', x) == True else ClassLabels.ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_DOWNTIME)
def MINIMUM_DOWNTIME_LF5(x):
    log_file = f"./csv/MINIMUM_DOWNTIME_LF5_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MINIMUM_DOWNTIME if extractor.apply_rule(
        'If personnel or equipment must be on standby for immediate redeployment to reduce idle time.', x) == True else ClassLabels.ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_DOWNTIME)
def MINIMUM_DOWNTIME_LF6(x):
    log_file = f"./csv/MINIMUM_DOWNTIME_LF6_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MINIMUM_DOWNTIME if extractor.apply_rule(
        'If operational schedules emphasize rapid turnarounds and swift restarts after delays.', x) == True else ClassLabels.ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_DOWNTIME)
def MINIMUM_DOWNTIME_LF7(x):
    log_file = f"./csv/MINIMUM_DOWNTIME_LF7_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MINIMUM_DOWNTIME if extractor.apply_rule(
        'If mission tasks must be completed with minimal time spent on maintenance or troubleshooting.', x) == True else ClassLabels.ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_DOWNTIME)
def MINIMUM_DOWNTIME_LF8(x):
    log_file = f"./csv/MINIMUM_DOWNTIME_LF8_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MINIMUM_DOWNTIME if extractor.apply_rule(
        'If any downtime is proactively planned for and minimized during off-peak periods.', x) == True else ClassLabels.ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_DOWNTIME)
def MINIMUM_DOWNTIME_LF9(x):
    log_file = f"./csv/MINIMUM_DOWNTIME_LF9_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MINIMUM_DOWNTIME if extractor.apply_rule(
        'If alternate systems or redundancies are in place to ensure continuous operation during failures.', x) == True else ClassLabels.ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_DOWNTIME)
def MINIMUM_DOWNTIME_LF10(x):
    log_file = f"./csv/MINIMUM_DOWNTIME_LF10_logs_" + datetime.now().strftime('%Y%m%d') + ".csv"

    result = ClassLabels.MINIMUM_DOWNTIME if extractor.apply_rule(
        'If mission objectives prioritize maintaining momentum and reducing delays at all stages.', x) == True else ClassLabels.ABSTAIN

    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, result])

    return result

MINIMUM_DOWNTIMELFS = [
    MINIMUM_DOWNTIME_LF1, MINIMUM_DOWNTIME_LF2, MINIMUM_DOWNTIME_LF3, MINIMUM_DOWNTIME_LF4, MINIMUM_DOWNTIME_LF5, MINIMUM_DOWNTIME_LF6, MINIMUM_DOWNTIME_LF7, MINIMUM_DOWNTIME_LF8, MINIMUM_DOWNTIME_LF9, MINIMUM_DOWNTIME_LF10
]