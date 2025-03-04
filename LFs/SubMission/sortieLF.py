# 1. Carrier-based power projection mission

# 2. Maritime operational zone navigation

# 3. Maritime domain awareness objective

# 4. Anti-ship/maritime sensor configuration

# 5. Fleet defensive/offensive positioning support

# 6. Extended maritime operational range profile

# 7. Carrier air wing coordinated tactics

# 8. Maritime engagement protocol compliance

# 9. Maritime interdiction/combat capability

# 10. Maritime extreme environment operational readiness

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
@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Sortie_LF1(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Sortie_LF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Fleetsupport
        if extractor.apply_rule(
            "If mission involves aircraft deployment for specific tactical purpose.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Sortie_LF2(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Sortie_LF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Fleetsupport
        if extractor.apply_rule(
            "If flight path is pre-planned and strategically defined.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Sortie_LF3(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Sortie_LF3_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Fleetsupport
        if extractor.apply_rule(
            "If objective requires specific aerial operational profile.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Sortie_LF4(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Sortie_LF4_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Fleetsupport
        if extractor.apply_rule("If aircraft carries specialized mission equipment.", x)
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Sortie_LF5(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Sortie_LF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Fleetsupport
        if extractor.apply_rule(
            "If flight supports strategic reconnaissance or support goals.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Sortie_LF6(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Sortie_LF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Fleetsupport
        if extractor.apply_rule(
            "If mission requires specific fuel, range, and payload parameters.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Sortie_LF7(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Sortie_LF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Fleetsupport
        if extractor.apply_rule(
            "If operation involves single aircraft or coordinated squadron movement.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Sortie_LF8(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Sortie_LF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Fleetsupport
        if extractor.apply_rule(
            "If mission follows precise operational flight protocols.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Sortie_LF9(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Sortie_LF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Fleetsupport
        if extractor.apply_rule(
            "If flight supports combat, surveillance, or logistical objectives.", x
        )
        == True
        else ABSTAIN
    )
    if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])

    return result


@labeling_function(pre=[convert_to_lower], label=ClassLabels.Fleetsupport)
def Sortie_LF10(x):
    log_file = f"/home/user/IITB/LFi/LFs/SubMission/csv/Sortie_LF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"

    result = (
        ClassLabels.Fleetsupport
        if extractor.apply_rule(
            "If operation requires specific pilot skills and aircraft capabilities.", x
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
Sortie_LFS = [
    Sortie_LF1,
    Sortie_LF2,
    Sortie_LF3,
    Sortie_LF4,
    Sortie_LF5,
    Sortie_LF6,
    Sortie_LF7,
    Sortie_LF8,
    Sortie_LF9,
    Sortie_LF10,
]
