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
    EVALUTE = 0
    IDENTIFY = 1
    SELECT_K_OUT_OF_N = 2


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


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SELECT_K_OUT_OF_N)
def SELECT_K_OUT_OF_NACTION_LF1(x):
    result = (
        ClassLabels.SELECT_K_OUT_OF_N
        if extractor.apply_rule(
            "If the mission requires selecting the top k performing units out of N.", x
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "./csv/SELECT_K_OUT_OF_NACTION_LF1_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SELECT_K_OUT_OF_N)
def SELECT_K_OUT_OF_NACTION_LF2(x):
    result = (
        ClassLabels.SELECT_K_OUT_OF_N
        if extractor.apply_rule(
            "If k critical tasks must be prioritized out of N possible tasks.", x
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "./csv/SELECT_K_OUT_OF_NACTION_LF2_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SELECT_K_OUT_OF_N)
def SELECT_K_OUT_OF_NACTION_LF3(x):
    result = (
        ClassLabels.SELECT_K_OUT_OF_N
        if extractor.apply_rule(
            "If k key personnel must be chosen out of N candidates.", x
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "./csv/SELECT_K_OUT_OF_NACTION_LF3_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SELECT_K_OUT_OF_N)
def SELECT_K_OUT_OF_NACTION_LF4(x):
    result = (
        ClassLabels.SELECT_K_OUT_OF_N
        if extractor.apply_rule(
            "If k essential resources must be allocated out of N available resources.",
            x,
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "./csv/SELECT_K_OUT_OF_NACTION_LF4_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SELECT_K_OUT_OF_N)
def SELECT_K_OUT_OF_NACTION_LF5(x):
    result = (
        ClassLabels.SELECT_K_OUT_OF_N
        if extractor.apply_rule(
            "If k strategic locations must be selected out of N potential sites.", x
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "./csv/SELECT_K_OUT_OF_NACTION_LF5_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SELECT_K_OUT_OF_N)
def SELECT_K_OUT_OF_NACTION_LF6(x):
    result = (
        ClassLabels.SELECT_K_OUT_OF_N
        if extractor.apply_rule(
            "If k high-priority targets must be identified out of N targets.", x
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "./csv/SELECT_K_OUT_OF_NACTION_LF6_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SELECT_K_OUT_OF_N)
def SELECT_K_OUT_OF_NACTION_LF7(x):
    result = (
        ClassLabels.SELECT_K_OUT_OF_N
        if extractor.apply_rule(
            "If k optimal routes must be chosen out of N possible routes.", x
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "./csv/SELECT_K_OUT_OF_NACTION_LF7_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SELECT_K_OUT_OF_N)
def SELECT_K_OUT_OF_NACTION_LF8(x):
    result = (
        ClassLabels.SELECT_K_OUT_OF_N
        if extractor.apply_rule(
            "If k critical systems must be selected for upgrade out of N systems.", x
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "./csv/SELECT_K_OUT_OF_NACTION_LF8_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SELECT_K_OUT_OF_N)
def SELECT_K_OUT_OF_NACTION_LF9(x):
    result = (
        ClassLabels.SELECT_K_OUT_OF_N
        if extractor.apply_rule(
            "If k key suppliers must be chosen out of N potential suppliers.", x
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "./csv/SELECT_K_OUT_OF_NACTION_LF9_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.SELECT_K_OUT_OF_N)
def SELECT_K_OUT_OF_NACTION_LF10(x):
    result = (
        ClassLabels.SELECT_K_OUT_OF_N
        if extractor.apply_rule(
            "If k high-risk areas must be identified out of N areas for surveillance.",
            x,
        )
        == True
        else ABSTAIN
    )

    if LOGGING_ENABLED and result != ABSTAIN:
        log_file = (
            "./csv/SELECT_K_OUT_OF_NACTION_LF10_logs_"
            + datetime.now().strftime("%Y%m%d")
            + ".csv"
        )
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


SELECT_K_OUT_OF_N_ACTION_LFS = [
    SELECT_K_OUT_OF_NACTION_LF1,
    SELECT_K_OUT_OF_NACTION_LF2,
    SELECT_K_OUT_OF_NACTION_LF3,
    SELECT_K_OUT_OF_NACTION_LF4,
    SELECT_K_OUT_OF_NACTION_LF5,
    SELECT_K_OUT_OF_NACTION_LF6,
    SELECT_K_OUT_OF_NACTION_LF7,
    SELECT_K_OUT_OF_NACTION_LF8,
    SELECT_K_OUT_OF_NACTION_LF9,
    SELECT_K_OUT_OF_NACTION_LF10,
]
