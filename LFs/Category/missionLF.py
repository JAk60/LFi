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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mission)
def LF1(x):
    result = ClassLabels.Mission if len(set(x.split()) & trigWord1) > 0 else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(
    cont_scorer=word_similarity,
    resources=dict(keywords=trigWord1),
    pre=[convert_to_lower],
    label=ClassLabels.Mission,
)
def CLF1(c, **kwargs):
    result = ClassLabels.Mission if kwargs["continuous_score"] >= THRESHOLD else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/category/csv/CLF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), c, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mission)
def LF5(x):
    pattern = r"/b([2-9][0-9]|[1-9][0-9]{2,}) nm/b"
    result = ClassLabels.Mission if re.search(pattern, x) else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mission)
def LF6(x):
    pattern = r"/b([4-9]|[1-9][0-9]{2,}) ac/b"
    result = ClassLabels.Mission if re.search(pattern, x) else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mission)
def LF7(x):
    pattern = r"[1-9]{3,} steering pumps"
    result = ClassLabels.Mission if re.search(pattern, x) else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mission)
def LF8(x):
    pattern = r"stabiliser"
    result = ClassLabels.Mission if re.search(pattern, x) else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mission)
def LF9(x):
    pattern = r"/b([0-9]|1[0-9]|2[0-9]) kw/b|power generation units on hot standby"
    result = ClassLabels.Mission if re.search(pattern, x) else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mission)
def LF10(x):
    rpm_pattern = r"/b(1[5-9][0-9]|[2-9][0-9]{2,})/s*rpm/b"
    knots_pattern = r"/b(1[89]|[2-9][0-9]|[1-9][0-9]{2,})/s*knots/b"
    pattern = f"({rpm_pattern})|({knots_pattern})"

    result = ClassLabels.Mission if re.search(pattern, x) else ABSTAIN
    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mission)
def LF15(x):
    d = extractor._extract_distance(x)
    result = ClassLabels.Mission if float(d) > 20 else ABSTAIN

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF15_logs_{datetime.now().strftime('%Y%m%d')}.csv"
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


MissionLFS = [LF1, CLF1, LF5, LF6, LF7, LF8, LF9, LF10, LF15]
