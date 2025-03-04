[
    'If the ship"s systems must be reliable for mission success.',
    "If the equipment must be dependable for continuous operations.",
    "If the ship must have redundant systems for reliability.",
    "If the maintenance must be regular for system reliability.",
    "If the ship must have reliable communication systems.",
    "If the equipment must be tested for reliability.",
    "If the ship must have reliable navigation systems.",
    "If the maintenance must be timely for system reliability.",
    "If the ship must have reliable power generation.",
    "If the equipment must be durable for long-term use.",
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RELIABILITY)
def RELIABILITYLF1(x):
    result = (
        ClassLabels.RELIABILITY
        if extractor.apply_rule(
            'If the ship"s systems must be reliable for mission success.', x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RELIABILITYLF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RELIABILITY)
def RELIABILITYLF2(x):
    result = (
        ClassLabels.RELIABILITY
        if extractor.apply_rule(
            "If the equipment must be dependable for continuous operations.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RELIABILITYLF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RELIABILITY)
def RELIABILITYLF3(x):
    result = (
        ClassLabels.RELIABILITY
        if extractor.apply_rule(
            "If the ship must have redundant systems for reliability.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RELIABILITYLF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RELIABILITY)
def RELIABILITYLF4(x):
    result = (
        ClassLabels.RELIABILITY
        if extractor.apply_rule(
            "If the maintenance must be regular for system reliability.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RELIABILITYLF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RELIABILITY)
def RELIABILITYLF5(x):
    result = (
        ClassLabels.RELIABILITY
        if extractor.apply_rule(
            "If the ship must have reliable communication systems.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RELIABILITYLF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RELIABILITY)
def RELIABILITYLF6(x):
    result = (
        ClassLabels.RELIABILITY
        if extractor.apply_rule("If the equipment must be tested for reliability.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RELIABILITYLF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RELIABILITY)
def RELIABILITYLF7(x):
    result = (
        ClassLabels.RELIABILITY
        if extractor.apply_rule("If the ship must have reliable navigation systems.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RELIABILITYLF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RELIABILITY)
def RELIABILITYLF8(x):
    result = (
        ClassLabels.RELIABILITY
        if extractor.apply_rule(
            "If the maintenance must be timely for system reliability.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RELIABILITYLF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RELIABILITY)
def RELIABILITYLF9(x):
    result = (
        ClassLabels.RELIABILITY
        if extractor.apply_rule("If the ship must have reliable power generation.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RELIABILITYLF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.RELIABILITY)
def RELIABILITYLF10(x):
    result = (
        ClassLabels.RELIABILITY
        if extractor.apply_rule(
            "If the equipment must be durable for long-term use.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/RELIABILITYLF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


RELIABILITYLFS = [
    RELIABILITYLF1,
    RELIABILITYLF2,
    RELIABILITYLF3,
    RELIABILITYLF4,
    RELIABILITYLF5,
    RELIABILITYLF6,
    RELIABILITYLF7,
    RELIABILITYLF8,
    RELIABILITYLF9,
    RELIABILITYLF10,
]
