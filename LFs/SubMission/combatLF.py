# 1. If mission involves direct armed confrontation.

# 2. If weapons deployed are lethal and targeted.

# 3. If objective is to neutralize enemy combatants.

# 4. If strategic positioning requires military intervention.

# 5. If personnel are armed and in hostile territory.

# 6. If tactical engagement necessitates combat force.

# 7. If mission goal is to disrupt enemy capabilities.

# 8. If rules of engagement permit offensive strikes.

# 9. If potential for armed conflict is high.

# 10. If military power projection requires direct action.

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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Combat)
def Combat_LF1(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Combat_LF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Combat
        if extractor.apply_rule("If mission involves direct armed confrontation.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Combat)
def Combat_LF2(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Combat_LF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Combat
        if extractor.apply_rule("If weapons deployed are lethal and targeted.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Combat)
def Combat_LF3(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Combat_LF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Combat
        if extractor.apply_rule("If objective is to neutralize enemy combatants.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Combat)
def Combat_LF4(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Combat_LF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Combat
        if extractor.apply_rule(
            "If strategic positioning requires military intervention.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Combat)
def Combat_LF5(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Combat_LF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Combat
        if extractor.apply_rule("If personnel are armed and in hostile territory.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Combat)
def Combat_LF6(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Combat_LF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Combat
        if extractor.apply_rule("If tactical engagement necessitates combat force.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Combat)
def Combat_LF7(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Combat_LF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Combat
        if extractor.apply_rule("If mission goal is to disrupt enemy capabilities.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Combat)
def Combat_LF8(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Combat_LF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Combat
        if extractor.apply_rule("If rules of engagement permit offensive strikes.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Combat)
def Combat_LF9(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Combat_LF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Combat
        if extractor.apply_rule("If potential for armed conflict is high.", x) == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Combat)
def Combat_LF10(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Combat_LF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Combat
        if extractor.apply_rule(
            "If military power projection requires direct action.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


# Create LFSet and add all labeling functions
Combat_LFS = [
    Combat_LF1,
    Combat_LF2,
    Combat_LF3,
    Combat_LF4,
    Combat_LF5,
    Combat_LF6,
    Combat_LF7,
    Combat_LF8,
    Combat_LF9,
    Combat_LF10,
]
