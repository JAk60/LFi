import csv
import enum
import sys
from datetime import datetime

from helper.mistral import SentenceExtractor
from LFs import LOGGING_ENABLED
from spear.labeling import ABSTAIN, labeling_function, preprocessor

sys.path.append("../../")


extractor = SentenceExtractor()


class ClassLabels(enum.Enum):
    FLEET = 0
    SHIP = 1
    EQUIPMENT = 2


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
    "combat",
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def SHIPLEVEL_LF1(x):
    result = (
        ClassLabels.SHIP
        if extractor.apply_rule(
            "If tactical operations or immediate mission execution is required.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/Level/csv/SHIPLEVEL_LF1_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def SHIPLEVEL_LF2(x):
    result = (
        ClassLabels.SHIP
        if extractor.apply_rule(
            "If the management of the crew, including assignments and rotations, is necessary.",
            x,
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/Level/csv/SHIPLEVEL_LF2_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def SHIPLEVEL_LF3(x):
    result = (
        ClassLabels.SHIP
        if extractor.apply_rule(
            "If responding to an immediate threat or emergency affecting the ship is essential.",
            x,
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/Level/csv/SHIPLEVEL_LF3_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def SHIPLEVEL_LF4(x):
    result = (
        ClassLabels.SHIP
        if extractor.apply_rule(
            "If the maintenance and repair of ship-specific equipment is needed.", x
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/Level/csv/SHIPLEVEL_LF4_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def SHIPLEVEL_LF5(x):
    result = (
        ClassLabels.SHIP
        if extractor.apply_rule(
            "If setting the course or navigating the ship is required.", x
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/Level/csv/SHIPLEVEL_LF5_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def SHIPLEVEL_LF6(x):
    result = (
        ClassLabels.SHIP
        if extractor.apply_rule(
            "If communication protocols and procedures specific to the ship must be followed.",
            x,
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/Level/csv/SHIPLEVEL_LF6_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def SHIPLEVEL_LF7(x):
    result = (
        ClassLabels.SHIP
        if extractor.apply_rule(
            "If the management of supplies and inventory specific to the ship is necessary.",
            x,
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/Level/csv/SHIPLEVEL_LF7_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def SHIPLEVEL_LF8(x):
    result = (
        ClassLabels.SHIP
        if extractor.apply_rule(
            "If safety protocols and emergency procedures specific to the ship must be enforced.",
            x,
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/Level/csv/SHIPLEVEL_LF8_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def SHIPLEVEL_LF9(x):
    result = (
        ClassLabels.SHIP
        if extractor.apply_rule(
            "If conducting training exercises or drills specific to the ship is required.",
            x,
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/Level/csv/SHIPLEVEL_LF9_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SHIP)
def SHIPLEVEL_LF10(x):
    result = (
        ClassLabels.SHIP
        if extractor.apply_rule(
            "If adapting to environmental conditions or weather affecting the ship is necessary.",
            x,
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/Level/csv/SHIPLEVEL_LF10_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


SHIPLEVEL_LFS = [
    SHIPLEVEL_LF1,
    SHIPLEVEL_LF2,
    SHIPLEVEL_LF3,
    SHIPLEVEL_LF4,
    SHIPLEVEL_LF5,
    SHIPLEVEL_LF6,
    SHIPLEVEL_LF7,
    SHIPLEVEL_LF8,
    SHIPLEVEL_LF9,
    SHIPLEVEL_LF10,
]
