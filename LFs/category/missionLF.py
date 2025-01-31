import numpy as np
import re
import enum
import csv
import logging
from datetime import datetime
import sys


sys.path.append('../../')

from spear.labeling import labeling_function, ABSTAIN, preprocessor, LFSet

from helper.con_scorer import word_similarity
from helper.mistral import SentenceExtractor

extractor = SentenceExtractor()

class ClassLabels(enum.Enum):
    Maintenance = 0
    Mission = 1

THRESHOLD = 0.6

# Keywords for classification
trigWord1 = {"fleet", "task force", "maritime operations", "deployment", "patrol", "exercise", "amphibious assault", "maritime security", "maneuvers", "fleet admiral", "base", "aviation", "seaborne operation", "vessel", "blockade", "warfare", "strategy", "surveillance", "convoy", "anti-submarine warfare", "combat", "mission objectives", "reconnaissance", "domain awareness", "presence", "drills", "escort", "fleet maneuvers", "operations center", "interception","mission","enemy","war", "mission,","mission's"}

trigWord2 = {"Repair", "Overhaul", "Refit", "Inspection", "Service", "Check-up", "Refurbishment", "Restoration", "Tune-up", "Fix", "Upgrade", "Restoration", "Refurbishment", "Inspection", "Overhaul", "Retrofit", "Revamp", "Refurbish", "Tune", "Lubrication", "Cleaning", "Calibration", "Testing", "Adjustment", "Replacement", "Painting", "Welding", "Greasing", "Polishing", "Troubleshooting","maintenance","annual","repair","restoration"}

@preprocessor()
def convert_to_lower(x):
    return x.lower().strip()

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mission)
def LF1(x):
    log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    
    result = ClassLabels.Mission if len(set(x.split()) & trigWord1) > 0 else ABSTAIN
        if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])
    
    return result
@labeling_function(cont_scorer=word_similarity, resources=dict(keywords=trigWord1), pre=[convert_to_lower], label=ClassLabels.Mission)
def CLF1(c, **kwargs):
    log_file = f"/home/user/IITB/LFi/LFs/category/csv/CLF1_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result=ClassLabels.Mission if kwargs["continuous_score"] >= THRESHOLD else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), c, result])
    
    return result

@labeling_function(cont_scorer=word_similarity, resources=dict(keywords=trigWord2), pre=[convert_to_lower], label=ClassLabels.Maintenance)
def CLF2(c, **kwargs):
    log_file = f"/home/user/IITB/LFi/LFs/category/csv/CLF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    result=ClassLabels.Maintenance if kwargs["continuous_score"] >= THRESHOLD else ABSTAIN
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), c, result])
    
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Maintenance)
def LF2(x):
    log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF2_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    
    result = ClassLabels.Maintenance if len(set(x.split()) & trigWord2) > 0 else ABSTAIN
        if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])
    
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mission)
def LF5(x):
    log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF5_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    
    pattern = r'/b([2-9][0-9]|[1-9][0-9]{2,}) nm/b' 
    result = ClassLabels.Mission if re.search(pattern, x) else ABSTAIN
        if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])
    
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mission)
def LF6(x):
    log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF6_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    
    pattern = r'/b([4-9]|[1-9][0-9]{2,}) ac/b' 
    result = ClassLabels.Mission if re.search(pattern, x) else ABSTAIN
        if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])
    
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mission)
def LF7(x):
    log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF7_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    
    pattern = r'[1-9]{3,} steering pumps' 
    result = ClassLabels.Mission if re.search(pattern, x) else ABSTAIN
        if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])
    
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mission)    
def LF8(x):
    log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF8_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    
    pattern = r'stabiliser' 
    result = ClassLabels.Mission if re.search(pattern, x) else ABSTAIN
        if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])
    
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mission)  
def LF9(x):
    log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF9_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    
    pattern = r'/b([0-9]|1[0-9]|2[0-9]) kw/b|power generation units on hot standby' 
    result = ClassLabels.Mission if re.search(pattern, x) else ABSTAIN
        if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])
    
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mission)   
def LF10(x):
    log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF10_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    
    rpm_pattern = r'/b(1[5-9][0-9]|[2-9][0-9]{2,})/s*rpm/b'
    knots_pattern = r'/b(1[89]|[2-9][0-9]|[1-9][0-9]{2,})/s*knots/b'
    pattern = f'({rpm_pattern})|({knots_pattern})'
    
    result = ClassLabels.Mission if re.search(pattern, x) else ABSTAIN
        if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])
    
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Maintenance)  
def LF11(x):
    log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF11_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    
    pattern = r'/b([0-9]|[1-4][0-9])% (das|diesel alternator)/b'
    result = ClassLabels.Maintenance if re.search(pattern, x) else ABSTAIN
        if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])
    
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Maintenance)  
def LF12(x):
    log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF12_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    
    pattern = r'Fire pumps on the ship are not in the ready state|Fire pumps available  0|fire pumps are chocked'
    result = ClassLabels.Maintenance if re.search(pattern, x) else ABSTAIN
        if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])
    
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Maintenance)  
def LF13(x):
    log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF13_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    
    pattern = r'/b helicopters onboard (1[5-9][0-9]|[2-9][1-9]{1,}) |helicopters are available for next 2 days|helo' 
    result = ClassLabels.Maintenance if re.search(pattern, x) else ABSTAIN
        if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])
    
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Maintenance)  
def LF14(x):
    log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF14_logs_{datetime.now().strftime('%Y%m%d')}.csv"
    
    pattern = r'radar is not working | sonar is unavailable | sonar system needs to be changed| satelite communication' 
    result = ClassLabels.Maintenance if re.search(pattern, x) else ABSTAIN
        if LOGGING_ENABLED and result != ABSTAIN:
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), x, result])
    
    return result

@labeling_function(pre=[convert_to_lower], label=ClassLabels.Mission)
def LF15(x):
    log_file = f"/home/user/IITB/LFi/LFs/category/csv/LF15_logs_{datetime.now().strftime('%Y%m%d')}.csv"
   
    d = extractor._extract_distance(x)
    result = ClassLabels.Mission if float(d) > 20 else ABSTAIN
   
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), x, d, result])
   
    return result

LFS = [
    LF1,
    LF2,
    CLF1,
    CLF2,
    LF5,
    LF6,
    LF7,
    LF8,
    LF9,
    LF10,
    LF11,
    LF12,
    LF13,
    LF14,
    LF15
]


