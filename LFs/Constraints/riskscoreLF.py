[
    "If the mission risk must be assessed for crew safety.",
    "If the risk score must be low for non-combat operations.",
    "If the risk must be managed for mission success.",
    "If the risk score must be evaluated for emergency response.",
    "If the risk must be minimized for humanitarian aid missions.",
    "If the risk score must be assessed for joint exercises.",
    "If the risk must be managed for search and rescue operations.",
    "If the risk score must be evaluated for anti-piracy missions.",
    "If the risk must be minimized for maritime security patrols.",
    "If the risk score must be assessed for disaster relief operations.",
]

import csv
import enum
import sys
from datetime import datetime

sys.path.append("../../")

from helper.mistral import SentenceExtractor
from LFs import LOGGING_ENABLED
from spear.labeling import ABSTAIN, labeling_function, preprocessor

extractor = SentenceExtractor()


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
trigWord1 = {
    "fleet",
    "task force",
    "maritime operations",
    "deployment",
    "patrol",
    "exercise",
    "amphibious assault",
    "maritime security",
    "maneuvers",
    "fleet admiral",
    "base",
    "aviation",
    "seaborne operation",
    "vessel",
    "blockade",
    "warfare",
    "strategy",
    "surveillance",
    "convoy",
    "anti-submarine warfare",
    "Gunfiring",
    "mission objectives",
    "reconnaissance",
    "domain awareness",
    "presence",
    "drills",
    "escort",
    "fleet maneuvers",
    "operations center",
    "interception",
    "mission",
    "enemy",
    "war",
    "mission,",
    "mission's",
}

trigWord2 = {
    "Repair",
    "Overhaul",
    "Refit",
    "Inspection",
    "Service",
    "Check-up",
    "Refurbishment",
    "Restoration",
    "Tune-up",
    "Fix",
    "Upgrade",
    "Retrofit",
    "Revamp",
    "Refurbish",
    "Tune",
    "Lubrication",
    "Cleaning",
    "Calibration",
    "Testing",
    "Adjustment",
    "Replacement",
    "Painting",
    "Welding",
    "Greasing",
    "Polishing",
    "Troubleshooting",
    "maintenance",
    "annual",
    "repair",
    "restoration",
}


@preprocessor()
def convert_to_lower(x):
    return x.lower().strip()


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RISK_SCORE)
def RISK_SCORELF1(x):
    result = (
        ClassLabels.RISK_SCORE
        if extractor.apply_rule(
            "If the mission risk must be assessed for crew safety.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RISK_SCORELF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RISK_SCORE)
def RISK_SCORELF2(x):
    result = (
        ClassLabels.RISK_SCORE
        if extractor.apply_rule(
            "If the risk score must be low for non-combat operations.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RISK_SCORELF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RISK_SCORE)
def RISK_SCORELF3(x):
    result = (
        ClassLabels.RISK_SCORE
        if extractor.apply_rule("If the risk must be managed for mission success.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RISK_SCORELF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RISK_SCORE)
def RISK_SCORELF4(x):
    result = (
        ClassLabels.RISK_SCORE
        if extractor.apply_rule(
            "If the risk score must be evaluated for emergency response.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RISK_SCORELF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RISK_SCORE)
def RISK_SCORELF5(x):
    result = (
        ClassLabels.RISK_SCORE
        if extractor.apply_rule(
            "If the risk must be minimized for humanitarian aid missions.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RISK_SCORELF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RISK_SCORE)
def RISK_SCORELF6(x):
    result = (
        ClassLabels.RISK_SCORE
        if extractor.apply_rule(
            "If the risk score must be assessed for joint exercises.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RISK_SCORELF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RISK_SCORE)
def RISK_SCORELF7(x):
    result = (
        ClassLabels.RISK_SCORE
        if extractor.apply_rule(
            "If the risk must be managed for search and rescue operations.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RISK_SCORELF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RISK_SCORE)
def RISK_SCORELF8(x):
    result = (
        ClassLabels.RISK_SCORE
        if extractor.apply_rule(
            "If the risk score must be evaluated for anti-piracy missions.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RISK_SCORELF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RISK_SCORE)
def RISK_SCORELF9(x):
    result = (
        ClassLabels.RISK_SCORE
        if extractor.apply_rule(
            "If the risk must be minimized for maritime security patrols.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RISK_SCORELF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RISK_SCORE)
def RISK_SCORELF10(x):
    result = (
        ClassLabels.RISK_SCORE
        if extractor.apply_rule(
            "If the risk score must be assessed for disaster relief operations.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RISK_SCORELF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


RISK_SCORELFS = [
    RISK_SCORELF1,
    RISK_SCORELF2,
    RISK_SCORELF3,
    RISK_SCORELF4,
    RISK_SCORELF5,
    RISK_SCORELF6,
    RISK_SCORELF7,
    RISK_SCORELF8,
    RISK_SCORELF9,
    RISK_SCORELF10,
]
