# 1. If the mission requires immediate accomplishment of critical objectives.
# 2. If delays risk compromising the success or relevance of the operation.
# 3. If the timeline directly impacts strategic or tactical advantages.
# 4. If time-sensitive intelligence drives mission planning and execution.
# 5. If the operation involves synchronized actions with strict time constraints.
# 6. If swift execution is necessary to prevent enemy countermeasures.
# 7. If the mission is a rapid response to an emergent threat or opportunity.
# 8. If operational goals emphasize speed over resource conservation.
# 9. If objectives are designed to minimize enemy recovery time.
# 10. If the success of the mission depends on achieving surprise through speed.


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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_TIME)
def MinimumTime_LF1(x):
    result = (
        ClassLabels.MINIMUM_TIME
        if extractor.apply_rule(
            "If the mission requires immediate accomplishment of critical objectives.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumTime_LF1_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_TIME)
def MinimumTime_LF2(x):
    result = (
        ClassLabels.MINIMUM_TIME
        if extractor.apply_rule(
            "If delays risk compromising the success or relevance of the operation.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumTime_LF2_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_TIME)
def MinimumTime_LF3(x):
    result = (
        ClassLabels.MINIMUM_TIME
        if extractor.apply_rule(
            "If the timeline directly impacts strategic or tactical advantages.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumTime_LF3_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_TIME)
def MinimumTime_LF4(x):
    result = (
        ClassLabels.MINIMUM_TIME
        if extractor.apply_rule(
            "If time-sensitive intelligence drives mission planning and execution.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumTime_LF4_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_TIME)
def MinimumTime_LF5(x):
    result = (
        ClassLabels.MINIMUM_TIME
        if extractor.apply_rule(
            "If the operation involves synchronized actions with strict time constraints.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumTime_LF5_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_TIME)
def MinimumTime_LF6(x):
    result = (
        ClassLabels.MINIMUM_TIME
        if extractor.apply_rule(
            "If swift execution is necessary to prevent enemy countermeasures.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumTime_LF6_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_TIME)
def MinimumTime_LF7(x):
    result = (
        ClassLabels.MINIMUM_TIME
        if extractor.apply_rule(
            "If the mission is a rapid response to an emergent threat or opportunity.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumTime_LF7_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_TIME)
def MinimumTime_LF8(x):
    result = (
        ClassLabels.MINIMUM_TIME
        if extractor.apply_rule(
            "If operational goals emphasize speed over resource conservation.", x
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumTime_LF8_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_TIME)
def MinimumTime_LF9(x):
    result = (
        ClassLabels.MINIMUM_TIME
        if extractor.apply_rule(
            "If objectives are designed to minimize enemy recovery time.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumTime_LF9_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MINIMUM_TIME)
def MinimumTime_LF10(x):
    result = (
        ClassLabels.MINIMUM_TIME
        if extractor.apply_rule(
            "If the success of the mission depends on achieving surprise through speed.",
            x,
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "/home/user/IITB/LFi/LFs/ObjectiveFunction/csv/MinimumTime_LF10_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


MinimumTime_LFS = [
    MinimumTime_LF1,
    MinimumTime_LF2,
    MinimumTime_LF3,
    MinimumTime_LF4,
    MinimumTime_LF5,
    MinimumTime_LF6,
    MinimumTime_LF7,
    MinimumTime_LF8,
    MinimumTime_LF9,
    MinimumTime_LF10,
]
