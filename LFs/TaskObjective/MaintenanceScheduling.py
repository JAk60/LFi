# 1. If the operation involves direct scheduling of maintenance tasks.

# 2. If the use of maintenance scheduling tools is authorized for the mission.

# 3. If the target equipment requires immediate maintenance scheduling.

# 4. If the situation demands urgent maintenance scheduling to prevent failures.

# 5. If the equipment is within the maintenance window and requires scheduling.

# 6. If the tactical plan includes coordinated maintenance scheduling efforts.

# 7. If the objective can only be achieved through proper maintenance scheduling.

# 8. If the rules of engagement specify the use of maintenance scheduling methods.

# 9. If the equipment is equipped with sensors requiring maintenance scheduling.

# 10. If the mission requires continuous maintenance scheduling to ensure operational readiness.


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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MaintenanceScheduling)
def MaintenanceSchedulingLF1(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/MaintenanceSchedulingLF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.MaintenanceScheduling
        if extractor.apply_rule(
            "If the operation involves direct scheduling of maintenance tasks.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MaintenanceScheduling)
def MaintenanceSchedulingLF2(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/MaintenanceSchedulingLF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.MaintenanceScheduling
        if extractor.apply_rule(
            "If the use of maintenance scheduling tools is authorized for the mission.",
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MaintenanceScheduling)
def MaintenanceSchedulingLF3(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/MaintenanceSchedulingLF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.MaintenanceScheduling
        if extractor.apply_rule(
            "If the target equipment requires immediate maintenance scheduling.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MaintenanceScheduling)
def MaintenanceSchedulingLF4(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/MaintenanceSchedulingLF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.MaintenanceScheduling
        if extractor.apply_rule(
            "If the situation demands urgent maintenance scheduling to prevent failures.",
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MaintenanceScheduling)
def MaintenanceSchedulingLF5(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/MaintenanceSchedulingLF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.MaintenanceScheduling
        if extractor.apply_rule(
            "If the equipment is within the maintenance window and requires scheduling.",
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MaintenanceScheduling)
def MaintenanceSchedulingLF6(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/MaintenanceSchedulingLF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.MaintenanceScheduling
        if extractor.apply_rule(
            "If the tactical plan includes coordinated maintenance scheduling efforts.",
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MaintenanceScheduling)
def MaintenanceSchedulingLF7(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/MaintenanceSchedulingLF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.MaintenanceScheduling
        if extractor.apply_rule(
            "If the objective can only be achieved through proper maintenance scheduling.",
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MaintenanceScheduling)
def MaintenanceSchedulingLF8(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/MaintenanceSchedulingLF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.MaintenanceScheduling
        if extractor.apply_rule(
            "If the rules of engagement specify the use of maintenance scheduling methods.",
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MaintenanceScheduling)
def MaintenanceSchedulingLF9(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/MaintenanceSchedulingLF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.MaintenanceScheduling
        if extractor.apply_rule(
            "If the equipment is equipped with sensors requiring maintenance scheduling.",
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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.MaintenanceScheduling)
def MaintenanceSchedulingLF10(x):
    log_file = f"/home/user/IITB/LFi/LFs/Task Objective/csv/MaintenanceSchedulingLF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.MaintenanceScheduling
        if extractor.apply_rule(
            " If the mission requires continuous maintenance scheduling to ensure operational readiness.",
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


# Create LFSet and add all labeling functions
MaintenanceSchedulingLFS = [
    MaintenanceSchedulingLF1,
    MaintenanceSchedulingLF2,
    MaintenanceSchedulingLF3,
    MaintenanceSchedulingLF4,
    MaintenanceSchedulingLF5,
    MaintenanceSchedulingLF6,
    MaintenanceSchedulingLF7,
    MaintenanceSchedulingLF8,
    MaintenanceSchedulingLF9,
    MaintenanceSchedulingLF10,
]
