# 1. If the mission aims to achieve objectives while minimizing exposure to danger or harm.
# 2. If all operational actions are designed to reduce the likelihood of unexpected or adverse events.
# 3. If preventive measures are prioritized to avoid failures, accidents, or losses.
# 4. If mission plans emphasize the safety of personnel and equipment at every stage.
# 5. If risk assessments are conducted continuously to adapt the mission plan as necessary.
# 6. If safety protocols and contingency plans are integral to the mission's execution.
# 7. If the mission seeks to avoid high-risk areas or actions that could escalate potential threats.
# 8. If critical decisions are based on minimizing potential impacts of negative outcomes.
# 9. If the mission avoids unnecessary exposure to hostile or volatile environments.
# 10. If backup systems and procedures are in place to handle risks and reduce exposure to failure.


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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_RISK)
def MinimumRisk_LF1(x):
    result = (
        ClassLabels.MINIMUM_RISK
        if extractor.apply_rule(
            "If the mission aims to achieve objectives while minimizing exposure to danger or harm.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumRisk_LF1_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_RISK)
def MinimumRisk_LF2(x):
    result = (
        ClassLabels.MINIMUM_RISK
        if extractor.apply_rule(
            "If all operational actions are designed to reduce the likelihood of unexpected or adverse events.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumRisk_LF2_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_RISK)
def MinimumRisk_LF3(x):
    result = (
        ClassLabels.MINIMUM_RISK
        if extractor.apply_rule(
            "If preventive measures are prioritized to avoid failures, accidents, or losses.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumRisk_LF3_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_RISK)
def MinimumRisk_LF4(x):
    result = (
        ClassLabels.MINIMUM_RISK
        if extractor.apply_rule(
            "If mission plans emphasize the safety of personnel and equipment at every stage.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumRisk_LF4_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_RISK)
def MinimumRisk_LF5(x):
    result = (
        ClassLabels.MINIMUM_RISK
        if extractor.apply_rule(
            "If risk assessments are conducted continuously to adapt the mission plan as necessary.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumRisk_LF5_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_RISK)
def MinimumRisk_LF6(x):
    result = (
        ClassLabels.MINIMUM_RISK
        if extractor.apply_rule(
            'If safety protocols and contingency plans are integral to the mission"s execution.',
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumRisk_LF6_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_RISK)
def MinimumRisk_LF7(x):
    result = (
        ClassLabels.MINIMUM_RISK
        if extractor.apply_rule(
            "If the mission seeks to avoid high-risk areas or actions that could escalate potential threats.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumRisk_LF7_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_RISK)
def MinimumRisk_LF8(x):
    result = (
        ClassLabels.MINIMUM_RISK
        if extractor.apply_rule(
            "If critical decisions are based on minimizing potential impacts of negative outcomes.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumRisk_LF8_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_RISK)
def MinimumRisk_LF9(x):
    result = (
        ClassLabels.MINIMUM_RISK
        if extractor.apply_rule(
            "If the mission avoids unnecessary exposure to hostile or volatile environments.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumRisk_LF9_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_RISK)
def MinimumRisk_LF10(x):
    result = (
        ClassLabels.MINIMUM_RISK
        if extractor.apply_rule(
            "If backup systems and procedures are in place to handle risks and reduce exposure to failure.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumRisk_LF10_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


MinimumRisk_LFS = [
    MinimumRisk_LF1,
    MinimumRisk_LF2,
    MinimumRisk_LF3,
    MinimumRisk_LF4,
    MinimumRisk_LF5,
    MinimumRisk_LF6,
    MinimumRisk_LF7,
    MinimumRisk_LF8,
    MinimumRisk_LF9,
    MinimumRisk_LF10,
]
