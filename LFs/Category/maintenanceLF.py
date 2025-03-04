import csv
import enum
import re
import sys
from datetime import datetime

sys.path.append("../../")

from helper.mistral import SentenceExtractor
from helper.pcon_scorer import word_similarity
from LFs import LOGGING_ENABLED
from spear.labeling import ABSTAIN, labeling_function, preprocessor

extractor = SentenceExtractor()


class ClassLabels(enum.Enum):
    Maintenance = 0
    Mission = 1


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


@labeling_function(
    cont_scorer=word_similarity,
    resources=dict(keywords=trigWord2),
    pre=[convert_to_lower],
    label=ClassLabels.Maintenance,
)
def CLF2(c, **kwargs):
    result = (
        ClassLabels.Maintenance if kwargs["continuous_score"] >= THRESHOLD else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/category/csv/CLF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), c, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Maintenance)
def LF2(x):
    result = ClassLabels.Maintenance if len(set(x.split()) & trigWord2) > 0 else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Maintenance)
def LF11(x):
    pattern = r"/b([0-9]|[1-4][0-9])% (das|diesel alternator)/b"
    result = ClassLabels.Maintenance if re.search(pattern, x) else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF11_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Maintenance)
def LF12(x):
    pattern = r"Fire pumps on the ship are not in the ready state|Fire pumps available  0|fire pumps are chocked"
    result = ClassLabels.Maintenance if re.search(pattern, x) else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF12_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Maintenance)
def LF13(x):
    pattern = r"/b helicopters onboard (1[5-9][0-9]|[2-9][1-9]{1,}) |helicopters are available for next 2 days|helo"
    result = ClassLabels.Maintenance if re.search(pattern, x) else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF13_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Maintenance)
def LF14(x):
    pattern = r"radar is not working | sonar is unavailable | sonar system needs to be changed| satelite communication"
    result = ClassLabels.Maintenance if re.search(pattern, x) else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF14_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


MaintenanceLFS = [
    LF2,
    CLF2,
    LF11,
    LF12,
    LF13,
    LF14,
]
