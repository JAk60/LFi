# 1. If the operation involves direct gunfire exchange.

# 2. If the use of firearms is authorized for the mission.

# 3. If the target is to be eliminated through gunfire.

# 4. If the situation demands immediate gunfire response.

# 5. If the enemy is within gunfire range and poses a threat.

# 6. If the tactical plan includes coordinated gunfire.

# 7. If the objective can only be achieved through gunfire.

# 8. If the rules of engagement specify the use of gunfire.

# 9. If the hostile forces are equipped with firearms.

# 10. If the mission requires suppressive gunfire to advance.
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
    Gunfiring = 0
    InterrogationInterception = 1
    MaintenanceScheduling = 2
    Miscellaneous = 3
    MissileFiring = 4
    SearchAndRescue = 5


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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Gunfiring)
def GunfiringLF1(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/GunfiringLF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Gunfiring
        if extractor.apply_rule("If the operation involves direct gunfire exchange.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Gunfiring)
def GunfiringLF2(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/GunfiringLF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Gunfiring
        if extractor.apply_rule(
            "If the use of firearms is authorized for the mission.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Gunfiring)
def GunfiringLF3(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/GunfiringLF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Gunfiring
        if extractor.apply_rule("If the target is to be eliminated through gunfire.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Gunfiring)
def GunfiringLF4(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/GunfiringLF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Gunfiring
        if extractor.apply_rule(
            "If the situation demands immediate gunfire response.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Gunfiring)
def GunfiringLF5(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/GunfiringLF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Gunfiring
        if extractor.apply_rule(
            "If the enemy is within gunfire range and poses a threat.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Gunfiring)
def GunfiringLF6(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/GunfiringLF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Gunfiring
        if extractor.apply_rule("If the tactical plan includes coordinated gunfire.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Gunfiring)
def GunfiringLF7(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/GunfiringLF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Gunfiring
        if extractor.apply_rule(
            "If the objective can only be achieved through gunfire.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Gunfiring)
def GunfiringLF8(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/GunfiringLF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Gunfiring
        if extractor.apply_rule(
            "If the rules of engagement specify the use of gunfire.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Gunfiring)
def GunfiringLF9(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/GunfiringLF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Gunfiring
        if extractor.apply_rule("If the hostile forces are equipped with firearms.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Gunfiring)
def GunfiringLF10(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/GunfiringLF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Gunfiring
        if extractor.apply_rule(
            "If the mission requires suppressive gunfire to advance.", x
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
GunfiringLFS = [
    GunfiringLF1,
    GunfiringLF2,
    GunfiringLF3,
    GunfiringLF4,
    GunfiringLF5,
    GunfiringLF6,
    GunfiringLF7,
    GunfiringLF8,
    GunfiringLF9,
    GunfiringLF10,
]
