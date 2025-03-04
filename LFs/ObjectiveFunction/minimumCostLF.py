# 1. If the mission aims to achieve objectives using the least amount of financial resources.
# 2. If resource allocation is focused on achieving efficiency without over-investing in non-essential elements.
# 3. If cost-effective solutions are prioritized in operational planning and execution.
# 4. If operational decisions emphasize reducing waste and maximizing resource utilization.
# 5. If the mission relies on minimal expenditure for equipment, personnel, and logistics.
# 6. If the budget is limited, requiring a careful balance between resource needs and mission success.
# 7. If cheaper alternatives are explored to meet operational requirements without compromising safety.
# 8. If external partnerships or collaborations are leveraged to reduce costs.
# 9. If the mission requires a lean operational structure with minimal overhead.
# 10. If cost reduction strategies are continuously assessed and adjusted throughout the mission's lifecycle.


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
    MINIMUM_TIME = 0
    MAXIMUM_AVAILABILITY = 1
    MAXIMUM_CONFORMANCE = 2
    MAXIMUM_RELIABILITY = 3
    MINIMUM_COST = 4
    MINIMUM_DOWNTIME = 5
    MINIMUM_RISK = 6


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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_COST)
def MINIMUM_COST_LF1(x):
    result = (
        ClassLabels.MINIMUM_COST
        if extractor.apply_rule(
            "If the mission aims to achieve objectives using the least amount of financial resources.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MINIMUM_COST_LF1_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_COST)
def MINIMUM_COST_LF2(x):
    result = (
        ClassLabels.MINIMUM_COST
        if extractor.apply_rule(
            "If resource allocation is focused on achieving efficiency without over-investing in non-essential elements.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MINIMUM_COST_LF2_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_COST)
def MINIMUM_COST_LF3(x):
    result = (
        ClassLabels.MINIMUM_COST
        if extractor.apply_rule(
            "If cost-effective solutions are prioritized in operational planning and execution.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MINIMUM_COST_LF3_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_COST)
def MINIMUM_COST_LF4(x):
    result = (
        ClassLabels.MINIMUM_COST
        if extractor.apply_rule(
            "If operational decisions emphasize reducing waste and maximizing resource utilization.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MINIMUM_COST_LF4_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_COST)
def MINIMUM_COST_LF5(x):
    result = (
        ClassLabels.MINIMUM_COST
        if extractor.apply_rule(
            "If the mission relies on minimal expenditure for equipment, personnel, and logistics.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MINIMUM_COST_LF5_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_COST)
def MINIMUM_COST_LF6(x):
    result = (
        ClassLabels.MINIMUM_COST
        if extractor.apply_rule(
            "If the budget is limited, requiring a careful balance between resource needs and mission success.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MINIMUM_COST_LF6_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_COST)
def MINIMUM_COST_LF7(x):
    result = (
        ClassLabels.MINIMUM_COST
        if extractor.apply_rule(
            "If cheaper alternatives are explored to meet operational requirements without compromising safety.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MINIMUM_COST_LF7_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_COST)
def MINIMUM_COST_LF8(x):
    result = (
        ClassLabels.MINIMUM_COST
        if extractor.apply_rule(
            "If external partnerships or collaborations are leveraged to reduce costs.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MINIMUM_COST_LF8_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_COST)
def MINIMUM_COST_LF9(x):
    result = (
        ClassLabels.MINIMUM_COST
        if extractor.apply_rule(
            "If the mission requires a lean operational structure with minimal overhead.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MINIMUM_COST_LF9_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_COST)
def MINIMUM_COST_LF10(x):
    result = (
        ClassLabels.MINIMUM_COST
        if extractor.apply_rule(
            'If cost reduction strategies are continuously assessed and adjusted throughout the mission"s lifecycle.',
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MINIMUM_COST_LF10_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


MINIMUM_COST_LFS = [
    MINIMUM_COST_LF1,
    MINIMUM_COST_LF2,
    MINIMUM_COST_LF3,
    MINIMUM_COST_LF4,
    MINIMUM_COST_LF5,
    MINIMUM_COST_LF6,
    MINIMUM_COST_LF7,
    MINIMUM_COST_LF8,
    MINIMUM_COST_LF9,
    MINIMUM_COST_LF10,
]
