[
    "If only destroyers can be sent to combat of high criticality.",
    "If aircraft carriers must be deployed for air superiority.",
    "If submarines must be used for stealth operations.",
    "If frigates must be deployed for anti-submarine warfare.",
    "If amphibious assault ships must be used for beach landings.",
    "If mine countermeasure vessels must be deployed for mine clearance.",
    "If patrol boats must be used for coastal surveillance.",
    "If hospital ships must be deployed for medical support.",
    "If replenishment ships must be used for logistic support.",
    "If corvettes must be deployed for littoral combat.",
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP_CLASS)
def SHIP_CLASSLF1(x):
    result = (
        ClassLabels.SHIP_CLASS
        if extractor.apply_rule(
            "If only destroyers can be sent to combat of high criticality.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/SHIP_CLASSLF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP_CLASS)
def SHIP_CLASSLF2(x):
    result = (
        ClassLabels.SHIP_CLASS
        if extractor.apply_rule(
            "If aircraft carriers must be deployed for air superiority.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/SHIP_CLASSLF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP_CLASS)
def SHIP_CLASSLF3(x):
    result = (
        ClassLabels.SHIP_CLASS
        if extractor.apply_rule("If submarines must be used for stealth operations.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/SHIP_CLASSLF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP_CLASS)
def SHIP_CLASSLF4(x):
    result = (
        ClassLabels.SHIP_CLASS
        if extractor.apply_rule(
            "If frigates must be deployed for anti-submarine warfare.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/SHIP_CLASSLF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP_CLASS)
def SHIP_CLASSLF5(x):
    result = (
        ClassLabels.SHIP_CLASS
        if extractor.apply_rule(
            "If amphibious assault ships must be used for beach landings.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/SHIP_CLASSLF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP_CLASS)
def SHIP_CLASSLF6(x):
    result = (
        ClassLabels.SHIP_CLASS
        if extractor.apply_rule(
            "If mine countermeasure vessels must be deployed for mine clearance.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/SHIP_CLASSLF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP_CLASS)
def SHIP_CLASSLF7(x):
    result = (
        ClassLabels.SHIP_CLASS
        if extractor.apply_rule(
            "If patrol boats must be used for coastal surveillance.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/SHIP_CLASSLF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP_CLASS)
def SHIP_CLASSLF8(x):
    result = (
        ClassLabels.SHIP_CLASS
        if extractor.apply_rule(
            "If hospital ships must be deployed for medical support.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/SHIP_CLASSLF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP_CLASS)
def SHIP_CLASSLF9(x):
    result = (
        ClassLabels.SHIP_CLASS
        if extractor.apply_rule(
            "If replenishment ships must be used for logistic support.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/SHIP_CLASSLF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP_CLASS)
def SHIP_CLASSLF10(x):
    result = (
        ClassLabels.SHIP_CLASS
        if extractor.apply_rule("If corvettes must be deployed for littoral combat.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/SHIP_CLASSLF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


SHIP_CLASSLFS = [
    SHIP_CLASSLF1,
    SHIP_CLASSLF2,
    SHIP_CLASSLF3,
    SHIP_CLASSLF4,
    SHIP_CLASSLF5,
    SHIP_CLASSLF6,
    SHIP_CLASSLF7,
    SHIP_CLASSLF8,
    SHIP_CLASSLF9,
    SHIP_CLASSLF10,
]
