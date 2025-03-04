# 1. If operation involves structured military training scenario.

# 2. If personnel practice simulated mission protocols.

# 3. If objective is skill development and readiness assessment.

# 4. If scenario tests tactical response capabilities.

# 5. If environment mimics potential operational conditions.

# 6. If equipment and resources are used for training purposes.

# 7. If mission goal is to evaluate unit performance.

# 8. If engagement follows predefined training guidelines.

# 9. If potential risks are controlled and monitored.

# 10. If military preparedness is the primary focus.

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
    Combat = 0
    Exercise = 1
    Fleetsupport = 2
    Sortie = 3
    Humanitarian = 4


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


# Combat Labeling Functions
@labeling_function(pre=[convert_to_lower], label=ClassLabels.Exercise)
def Exercise_LF1(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Exercise_LF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Exercise
        if extractor.apply_rule(
            "If operation involves structured military training scenario.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Exercise)
def Exercise_LF2(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Exercise_LF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Exercise
        if extractor.apply_rule("If personnel practice simulated mission protocols.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Exercise)
def Exercise_LF3(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Exercise_LF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Exercise
        if extractor.apply_rule(
            "If objective is skill development and readiness assessment.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Exercise)
def Exercise_LF4(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Exercise_LF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Exercise
        if extractor.apply_rule("If scenario tests tactical response capabilities.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Exercise)
def Exercise_LF5(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Exercise_LF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Exercise
        if extractor.apply_rule(
            "If environment mimics potential operational conditions.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Exercise)
def Exercise_LF6(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Exercise_LF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Exercise
        if extractor.apply_rule(
            "If equipment and resources are used for training purposes.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Exercise)
def Exercise_LF7(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Exercise_LF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Exercise
        if extractor.apply_rule("If mission goal is to evaluate unit performance.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Exercise)
def Exercise_LF8(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Exercise_LF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Exercise
        if extractor.apply_rule(
            "If engagement follows predefined training guidelines.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Exercise)
def Exercise_LF9(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Exercise_LF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Exercise
        if extractor.apply_rule("If potential risks are controlled and monitored.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Exercise)
def Exercise_LF10(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Exercise_LF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Exercise
        if extractor.apply_rule("If military preparedness is the primary focus.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


# Create LFSet and add all labeling functions
Exercise_LFS = [
    Exercise_LF1,
    Exercise_LF2,
    Exercise_LF3,
    Exercise_LF4,
    Exercise_LF5,
    Exercise_LF6,
    Exercise_LF7,
    Exercise_LF8,
    Exercise_LF9,
    Exercise_LF10,
]
