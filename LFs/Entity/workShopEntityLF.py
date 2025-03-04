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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP)
def ENTITY_WORKSHOP_LF1(x):
    log_file = (
        "./home/user/IITB/LFi/LFs/Entity/csv/ENTITY_WORKSHOP_LF1_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.WORKSHOP
        if extractor.apply_rule(
            "If the operation involves setting up the Workshop for specialized tasks.",
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP)
def ENTITY_WORKSHOP_LF2(x):
    log_file = (
        "./home/user/IITB/LFi/LFs/Entity/csv/ENTITY_WORKSHOP_LF2_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.WORKSHOP
        if extractor.apply_rule(
            "If the Workshop needs to be equipped with necessary tools and machinery.",
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP)
def ENTITY_WORKSHOP_LF3(x):
    log_file = (
        "./home/user/IITB/LFi/LFs/Entity/csv/ENTITY_WORKSHOP_LF3_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.WORKSHOP
        if extractor.apply_rule(
            "If the Workshop requires maintenance to ensure operational efficiency.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP)
def ENTITY_WORKSHOP_LF4(x):
    log_file = (
        "./home/user/IITB/LFi/LFs/Entity/csv/ENTITY_WORKSHOP_LF4_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.WORKSHOP
        if extractor.apply_rule(
            "If the Workshop must be staffed with skilled technicians for specific jobs.",
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP)
def ENTITY_WORKSHOP_LF5(x):
    log_file = (
        "./home/user/IITB/LFi/LFs/Entity/csv/ENTITY_WORKSHOP_LF5_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.WORKSHOP
        if extractor.apply_rule(
            "If the Workshop needs to be organized for optimal workflow.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP)
def ENTITY_WORKSHOP_LF6(x):
    log_file = (
        "./home/user/IITB/LFi/LFs/Entity/csv/ENTITY_WORKSHOP_LF6_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.WORKSHOP
        if extractor.apply_rule(
            "If the Workshop must be inspected for safety compliance.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP)
def ENTITY_WORKSHOP_LF7(x):
    log_file = (
        "./home/user/IITB/LFi/LFs/Entity/csv/ENTITY_WORKSHOP_LF7_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.WORKSHOP
        if extractor.apply_rule(
            "If the Workshop requires upgrades to its equipment for enhanced productivity.",
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP)
def ENTITY_WORKSHOP_LF8(x):
    log_file = (
        "./home/user/IITB/LFi/LFs/Entity/csv/ENTITY_WORKSHOP_LF8_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.WORKSHOP
        if extractor.apply_rule(
            "If the Workshop needs to be stocked with essential materials for projects.",
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP)
def ENTITY_WORKSHOP_LF9(x):
    log_file = (
        "./home/user/IITB/LFi/LFs/Entity/csv/ENTITY_WORKSHOP_LF9_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.WORKSHOP
        if extractor.apply_rule(
            "If the Workshop must be coordinated with other departments for integrated operations.",
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.WORKSHOP)
def ENTITY_WORKSHOP_LF10(x):
    log_file = (
        "./home/user/IITB/LFi/LFs/Entity/csv/ENTITY_WORKSHOP_LF10_logs_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )

    result = (
        ClassLabels.WORKSHOP
        if extractor.apply_rule(
            "If the Workshop needs to be secured against unauthorized access.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


ENTITY_WORKSHOP_LFS = [
    ENTITY_WORKSHOP_LF1,
    ENTITY_WORKSHOP_LF2,
    ENTITY_WORKSHOP_LF3,
    ENTITY_WORKSHOP_LF4,
    ENTITY_WORKSHOP_LF5,
    ENTITY_WORKSHOP_LF6,
    ENTITY_WORKSHOP_LF7,
    ENTITY_WORKSHOP_LF8,
    ENTITY_WORKSHOP_LF9,
    ENTITY_WORKSHOP_LF10,
]
