[
    "If the logistic support must be timely for mission success.",
    "If the resupply must be coordinated with mission timelines.",
    "If the logistic time must be minimized for rapid response.",
    "If the supply chain must be efficient for continuous operations.",
    "If the logistic support must be synchronized with combat operations.",
    "If the logistic time must be optimized for cost-effectiveness.",
    "If the resupply must be timely for humanitarian aid missions.",
    "If the logistic support must be coordinated with allied forces.",
    "If the logistic time must be managed for extended missions.",
    "If the resupply must be timely for emergency situations.",
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.LOGISTIC_TIME)
def LOGISTIC_TIMELF1(x):
    result = (
        ClassLabels.LOGISTIC_TIME
        if extractor.apply_rule(
            "If the logistic support must be timely for mission success.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/LOGISTIC_TIMELF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.LOGISTIC_TIME)
def LOGISTIC_TIMELF2(x):
    result = (
        ClassLabels.LOGISTIC_TIME
        if extractor.apply_rule(
            "If the resupply must be coordinated with mission timelines.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/LOGISTIC_TIMELF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.LOGISTIC_TIME)
def LOGISTIC_TIMELF3(x):
    result = (
        ClassLabels.LOGISTIC_TIME
        if extractor.apply_rule(
            "If the logistic time must be minimized for rapid response.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/LOGISTIC_TIMELF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.LOGISTIC_TIME)
def LOGISTIC_TIMELF4(x):
    result = (
        ClassLabels.LOGISTIC_TIME
        if extractor.apply_rule(
            "If the supply chain must be efficient for continuous operations.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/LOGISTIC_TIMELF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.LOGISTIC_TIME)
def LOGISTIC_TIMELF5(x):
    result = (
        ClassLabels.LOGISTIC_TIME
        if extractor.apply_rule(
            "If the logistic support must be synchronized with combat operations.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/LOGISTIC_TIMELF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.LOGISTIC_TIME)
def LOGISTIC_TIMELF6(x):
    result = (
        ClassLabels.LOGISTIC_TIME
        if extractor.apply_rule(
            "If the logistic time must be optimized for cost-effectiveness.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/LOGISTIC_TIMELF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.LOGISTIC_TIME)
def LOGISTIC_TIMELF7(x):
    result = (
        ClassLabels.LOGISTIC_TIME
        if extractor.apply_rule(
            "If the resupply must be timely for humanitarian aid missions.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/LOGISTIC_TIMELF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.LOGISTIC_TIME)
def LOGISTIC_TIMELF8(x):
    result = (
        ClassLabels.LOGISTIC_TIME
        if extractor.apply_rule(
            "If the logistic support must be coordinated with allied forces.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/LOGISTIC_TIMELF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.LOGISTIC_TIME)
def LOGISTIC_TIMELF9(x):
    result = (
        ClassLabels.LOGISTIC_TIME
        if extractor.apply_rule(
            "If the logistic time must be managed for extended missions.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/LOGISTIC_TIMELF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.LOGISTIC_TIME)
def LOGISTIC_TIMELF10(x):
    result = (
        ClassLabels.LOGISTIC_TIME
        if extractor.apply_rule(
            "If the resupply must be timely for emergency situations.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            f"./csv/LOGISTIC_TIMELF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


LOGISTIC_TIMELFS = [
    LOGISTIC_TIMELF1,
    LOGISTIC_TIMELF2,
    LOGISTIC_TIMELF3,
    LOGISTIC_TIMELF4,
    LOGISTIC_TIMELF5,
    LOGISTIC_TIMELF6,
    LOGISTIC_TIMELF7,
    LOGISTIC_TIMELF8,
    LOGISTIC_TIMELF9,
    LOGISTIC_TIMELF10,
]
