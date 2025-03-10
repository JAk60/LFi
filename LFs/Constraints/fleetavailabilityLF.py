[
    "If the fleet must be ready for immediate deployment.",
    "If the ships must be available for emergency response.",
    "If the fleet must be prepared for sudden combat operations.",
    "If the ships must be available for humanitarian aid missions.",
    "If the fleet must be ready for joint exercises with allied nations.",
    "If the ships must be available for search and rescue operations.",
    "If the fleet must be prepared for anti-piracy missions.",
    "If the ships must be available for maritime security patrols.",
    "If the fleet must be ready for disaster relief operations.",
    "If the ships must be available for escort duties.",
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET_AVAILABILITY)
def FLEET_AVAILABILITYLF1(x):
    result = (
        ClassLabels.FLEET_AVAILABILITY
        if extractor.apply_rule(
            "If the fleet must be ready for immediate deployment.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/FLEET_AVAILABILITYLF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET_AVAILABILITY)
def FLEET_AVAILABILITYLF2(x):
    result = (
        ClassLabels.FLEET_AVAILABILITY
        if extractor.apply_rule(
            "If the ships must be available for emergency response.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/FLEET_AVAILABILITYLF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET_AVAILABILITY)
def FLEET_AVAILABILITYLF3(x):
    result = (
        ClassLabels.FLEET_AVAILABILITY
        if extractor.apply_rule(
            "If the fleet must be prepared for sudden combat operations.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/FLEET_AVAILABILITYLF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET_AVAILABILITY)
def FLEET_AVAILABILITYLF4(x):
    result = (
        ClassLabels.FLEET_AVAILABILITY
        if extractor.apply_rule(
            "If the ships must be available for humanitarian aid missions.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/FLEET_AVAILABILITYLF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET_AVAILABILITY)
def FLEET_AVAILABILITYLF5(x):
    result = (
        ClassLabels.FLEET_AVAILABILITY
        if extractor.apply_rule(
            "If the fleet must be ready for joint exercises with allied nations.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/FLEET_AVAILABILITYLF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET_AVAILABILITY)
def FLEET_AVAILABILITYLF6(x):
    result = (
        ClassLabels.FLEET_AVAILABILITY
        if extractor.apply_rule(
            "If the ships must be available for search and rescue operations.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/FLEET_AVAILABILITYLF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET_AVAILABILITY)
def FLEET_AVAILABILITYLF7(x):
    result = (
        ClassLabels.FLEET_AVAILABILITY
        if extractor.apply_rule(
            "If the fleet must be prepared for anti-piracy missions.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/FLEET_AVAILABILITYLF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET_AVAILABILITY)
def FLEET_AVAILABILITYLF8(x):
    result = (
        ClassLabels.FLEET_AVAILABILITY
        if extractor.apply_rule(
            "If the ships must be available for maritime security patrols.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/FLEET_AVAILABILITYLF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET_AVAILABILITY)
def FLEET_AVAILABILITYLF9(x):
    result = (
        ClassLabels.FLEET_AVAILABILITY
        if extractor.apply_rule(
            "If the fleet must be ready for disaster relief operations.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/FLEET_AVAILABILITYLF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.FLEET_AVAILABILITY)
def FLEET_AVAILABILITYLF10(x):
    result = (
        ClassLabels.FLEET_AVAILABILITY
        if extractor.apply_rule("If the ships must be available for escort duties.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/FLEET_AVAILABILITYLF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


FLEET_AVAILABILITYLFS = [
    FLEET_AVAILABILITYLF1,
    FLEET_AVAILABILITYLF2,
    FLEET_AVAILABILITYLF3,
    FLEET_AVAILABILITYLF4,
    FLEET_AVAILABILITYLF5,
    FLEET_AVAILABILITYLF6,
    FLEET_AVAILABILITYLF7,
    FLEET_AVAILABILITYLF8,
    FLEET_AVAILABILITYLF9,
    FLEET_AVAILABILITYLF10,
]
