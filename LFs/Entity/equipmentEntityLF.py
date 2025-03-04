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
    EQUIPMENT = 0
    SHIP = 1
    WORKSHOP = 2


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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def ENTITY_EQUIPMENT_LF1(x):
    log_file = (
        "/home/user/IITB/LFi/LFs/Entity/csv/ENTITY_EQUIPMENT_LF1_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.EQUIPMENT
        if extractor.apply_rule(
            "If the operation involves maintaining the functionality of critical Equipment.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def ENTITY_EQUIPMENT_LF2(x):
    log_file = (
        "/home/user/IITB/LFi/LFs/Entity/csv/ENTITY_EQUIPMENT_LF2_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.EQUIPMENT
        if extractor.apply_rule(
            "If the Equipment needs to be inspected for wear and tear.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def ENTITY_EQUIPMENT_LF3(x):
    log_file = (
        "/home/user/IITB/LFi/LFs/Entity/csv/ENTITY_EQUIPMENT_LF3_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.EQUIPMENT
        if extractor.apply_rule(
            "If the Equipment requires calibration for accurate performance.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def ENTITY_EQUIPMENT_LF4(x):
    log_file = (
        "/home/user/IITB/LFi/LFs/Entity/csv/ENTITY_EQUIPMENT_LF4_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.EQUIPMENT
        if extractor.apply_rule(
            "If the Equipment must be upgraded to meet new operational standards.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def ENTITY_EQUIPMENT_LF5(x):
    log_file = (
        "/home/user/IITB/LFi/LFs/Entity/csv/ENTITY_EQUIPMENT_LF5_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.EQUIPMENT
        if extractor.apply_rule(
            "If the Equipment needs to be repaired to ensure operational readiness.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def ENTITY_EQUIPMENT_LF6(x):
    log_file = (
        "/home/user/IITB/LFi/LFs/Entity/csv/ENTITY_EQUIPMENT_LF6_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.EQUIPMENT
        if extractor.apply_rule(
            "If the Equipment must be tested for compliance with safety regulations.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def ENTITY_EQUIPMENT_LF7(x):
    log_file = (
        "/home/user/IITB/LFi/LFs/Entity/csv/ENTITY_EQUIPMENT_LF7_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.EQUIPMENT
        if extractor.apply_rule(
            "If the Equipment needs to be integrated with other systems for enhanced functionality.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def ENTITY_EQUIPMENT_LF8(x):
    log_file = (
        "/home/user/IITB/LFi/LFs/Entity/csv/ENTITY_EQUIPMENT_LF8_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.EQUIPMENT
        if extractor.apply_rule(
            "If the Equipment requires regular maintenance to prevent failures.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def ENTITY_EQUIPMENT_LF9(x):
    log_file = (
        "/home/user/IITB/LFi/LFs/Entity/csv/ENTITY_EQUIPMENT_LF9_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.EQUIPMENT
        if extractor.apply_rule(
            "If the Equipment must be monitored for performance metrics.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.EQUIPMENT)
def ENTITY_EQUIPMENT_LF10(x):
    log_file = (
        "/home/user/IITB/LFi/LFs/Entity/csv/ENTITY_EQUIPMENT_LF10_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.EQUIPMENT
        if extractor.apply_rule(
            "If the Equipment needs to be secured against potential threats.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


ENTITY_EQUIPMENT_LFS = [
    ENTITY_EQUIPMENT_LF1,
    ENTITY_EQUIPMENT_LF2,
    ENTITY_EQUIPMENT_LF3,
    ENTITY_EQUIPMENT_LF4,
    ENTITY_EQUIPMENT_LF5,
    ENTITY_EQUIPMENT_LF6,
    ENTITY_EQUIPMENT_LF7,
    ENTITY_EQUIPMENT_LF8,
    ENTITY_EQUIPMENT_LF9,
    ENTITY_EQUIPMENT_LF10,
]
