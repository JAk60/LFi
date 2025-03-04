[
    "If the ship must have onboard workshops for repairs.",
    "If the workshops must be available for emergency maintenance.",
    "If the workshop must be equipped for various repair tasks.",
    "If the workshops must be managed for efficiency.",
    "If the ship must have emergency workshop capabilities.",
    "If the workshops must be secure against damage.",
    "If the workshop must be sufficient for high-intensity operations.",
    "If the workshops must be coordinated with mission timelines.",
    "If the workshops must be managed for cost-effectiveness.",
    "If the workshop must be of high quality to ensure system performance.",
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP_AVAILABILITY)
def WORKSHOP_AVAILABILITYLF1(x):
    result = (
        ClassLabels.WORKSHOP_AVAILABILITY
        if extractor.apply_rule(
            "If the ship must have onboard workshops for repairs.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/WORKSHOP_AVAILABILITYLF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP_AVAILABILITY)
def WORKSHOP_AVAILABILITYLF2(x):
    result = (
        ClassLabels.WORKSHOP_AVAILABILITY
        if extractor.apply_rule(
            "If the workshops must be available for emergency maintenance.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/WORKSHOP_AVAILABILITYLF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP_AVAILABILITY)
def WORKSHOP_AVAILABILITYLF3(x):
    result = (
        ClassLabels.WORKSHOP_AVAILABILITY
        if extractor.apply_rule(
            "If the workshop must be equipped for various repair tasks.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/WORKSHOP_AVAILABILITYLF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP_AVAILABILITY)
def WORKSHOP_AVAILABILITYLF4(x):
    result = (
        ClassLabels.WORKSHOP_AVAILABILITY
        if extractor.apply_rule("If the workshops must be managed for efficiency.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/WORKSHOP_AVAILABILITYLF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP_AVAILABILITY)
def WORKSHOP_AVAILABILITYLF5(x):
    result = (
        ClassLabels.WORKSHOP_AVAILABILITY
        if extractor.apply_rule(
            "If the ship must have emergency workshop capabilities.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/WORKSHOP_AVAILABILITYLF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP_AVAILABILITY)
def WORKSHOP_AVAILABILITYLF6(x):
    result = (
        ClassLabels.WORKSHOP_AVAILABILITY
        if extractor.apply_rule("If the workshops must be secure against damage.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/WORKSHOP_AVAILABILITYLF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP_AVAILABILITY)
def WORKSHOP_AVAILABILITYLF7(x):
    result = (
        ClassLabels.WORKSHOP_AVAILABILITY
        if extractor.apply_rule(
            "If the workshop must be sufficient for high-intensity operations.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/WORKSHOP_AVAILABILITYLF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP_AVAILABILITY)
def WORKSHOP_AVAILABILITYLF8(x):
    result = (
        ClassLabels.WORKSHOP_AVAILABILITY
        if extractor.apply_rule(
            "If the workshops must be coordinated with mission timelines.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/WORKSHOP_AVAILABILITYLF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP_AVAILABILITY)
def WORKSHOP_AVAILABILITYLF9(x):
    result = (
        ClassLabels.WORKSHOP_AVAILABILITY
        if extractor.apply_rule(
            "If the workshops must be managed for cost-effectiveness.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/WORKSHOP_AVAILABILITYLF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP_AVAILABILITY)
def WORKSHOP_AVAILABILITYLF10(x):
    result = (
        ClassLabels.WORKSHOP_AVAILABILITY
        if extractor.apply_rule(
            "If the workshop must be of high quality to ensure system performance.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"./csv/WORKSHOP_AVAILABILITYLF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


WORKSHOP_AVAILABILITYLFS = [
    WORKSHOP_AVAILABILITYLF1,
    WORKSHOP_AVAILABILITYLF2,
    WORKSHOP_AVAILABILITYLF3,
    WORKSHOP_AVAILABILITYLF4,
    WORKSHOP_AVAILABILITYLF5,
    WORKSHOP_AVAILABILITYLF6,
    WORKSHOP_AVAILABILITYLF7,
    WORKSHOP_AVAILABILITYLF8,
    WORKSHOP_AVAILABILITYLF9,
    WORKSHOP_AVAILABILITYLF10,
]
