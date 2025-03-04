from typing import Dict, List, Any, Union
from importlib import import_module
from pydantic import BaseModel, field_validator
import sys
import traceback

# Add necessary paths
sys.path.append('../../')
sys.path.append('../')
sys.path.append('../codes/')

from spearInf import pred_all_task

class Scenario(BaseModel):
    scenario: str
    version: Union[str, int]

    @field_validator('scenario')
    @classmethod
    def validate_scenario(cls, v):
        if not v or len(v) < 10:
            raise ValueError('Scenario must be a meaningful text')
        return v

    @field_validator('version')
    @classmethod
    def validate_version(cls, v):
        try:
            version = int(v)
            if version < 1 or version > 10:
                raise ValueError('Version must be between 1 and 10')
            return version
        except ValueError:
            raise ValueError('Version must be a valid integer')

MODULE_MAPPING = {
    "Category": "Category.CategoryLFS",
    "SubMission": "SubMission.SubcategoryLFS",
    "Criticality": "Criticality.CriticalityLFS",
    "Level": "Level.LevelLFS",
    "Action": "Action.ActionLFS",
    "Entity": "Entity.EntityLFS",
    "TaskObjective": "TaskObjective.TaskObjectiveLFS",
    "Constraints": "Constraints.ConstraintsLFS",
    "ObjectiveFunction": "ObjectiveFunction.ObjectiveFuncLFS",
}

class LabelingFunctionApplier:
    def __init__(self, lf_set_name: str, lflist: List[Any]):
        from spear.labeling.lf_set.core import LFSet
        from spear.labeling.apply import LFApplier

        self.rules = LFSet(lf_set_name)
        self.rules.add_lf_list(lflist)
        self.applier = LFApplier(lf_set=self.rules)
    
    def apply_lfs(self, data_points: List[str]):
        """Applies labeling functions and returns raw votes."""
        L, S = self.applier.apply(data_points)
        return L, S
    
    def voting_based_confidence(self, votes):
        """
        Applies a majority vote mechanism for Labeling Functions' outputs and
        calculates confidence for each labeling function, considering only `1` and ignoring `None`/`0` votes.
        """
        total_len = len(votes)
        valid_votes = [v for v in votes if v is not None]
        print(f"Valid Votes (after filtering None): {valid_votes}")
        
        # Convert values close to zero to 1, but leave exact zeros unchanged
        valid_votes = [1 if abs(v) >= 1e-5 else v for v in valid_votes]
        print(f"Valid Votes (after conversion): {valid_votes}")

        # Count the occurrences of 1 and 0
        count_1 = valid_votes.count(1)
        
        # Calculate the confidence as the percentage of 1 votes
        confidence = count_1 / total_len if valid_votes else 0

        return confidence

    def get_final_predictions(self, data_points):
        """Wrapper to apply labeling functions and use the voting mechanism"""
        L, S = self.apply_lfs(data_points)
        lf_confidences = self.voting_based_confidence(L[0])
        return lf_confidences

def load_lf_dictionary():
    return {
        'Category': ['MaintenanceLFS', 'MissionLFS'], 
        'SubMission': ['Combat_LFS', 'Exercise_LFS', 'Fleetsupport_LFS', 'Humanitarian_LFS', 'Sortie_LFS'], 
        'Criticality': ['High_Critical_LFS', 'Low_Critical_LFS', 'Mid_Critical_LFS'],
        'Level': ['FLEETLEVEL_LFS', 'SHIPLEVEL_LFS', 'EQUIPMENTLEVEL_LFS'],
        'Action': ['SELECT_K_OUT_OF_N_ACTION_LFS', 'IDENTIFY_ACTION_LFS', 'EVALUATE_ACTION_LFS'],
        'Entity': ['ENTITY_SHIP_LFS', 'ENTITY_WORKSHOP_LFS', 'ENTITY_EQUIPMENT_LFS'],
        'TaskObjective': ['GunfiringLFS', 'InterrogationInterceptionLFS', 'MaintenanceSchedulingLFS', 'MissileFiringLFS', 'SearchAndRescueLFS'], 
        'Constraints': ['ACTIVITY_SEQUENCESLFS', 'BALANCING_LOADSLFS', 'CAPABILITYLFS', 'CONFORMANCELFS',
                      'ENDURANCELFS', 'FLEET_AVAILABILITYLFS', 'FUELLFS', 'LOGISTIC_TIMELFS', 'MANPOWER_AVAILABILITYLFS',
                      'RATIONLFS', 'RELIABILITYLFS', 'RISK_SCORELFS', 'SHIP_CLASSLFS', 'SPARES_AVAILABILITYLFS',
                      'SPEEDLFS', 'WORKING_HOURSLFS', 'WORKSHOP_AVAILABILITYLFS'], 
        'ObjectiveFunction': ['MAXIMUM_AVAILABILITYLFS', 'MAXIMUM_CONFORMANCELFS', 'MAXIMUM_RELIABILITY_LFS', 
                            'MINIMUM_COST_LFS', 'MINIMUM_DOWNTIMELFS', 'MinimumRisk_LFS', 'MinimumTime_LFS']
    }

def process_predictions(scenario: str, predclass_output: List[Dict], lf_dict: Dict[str, List[str]]) -> Dict[str, Any]:
    if not isinstance(predclass_output, list):
        raise ValueError(f"Expected list of dictionaries, got {type(predclass_output)}")
    
    task_names = MODULE_MAPPING.keys()
    
    # Initialize the output structure
    results = {
        "predclass_output": {},
        "LFapplier_output": {}
    }

    for task, sublabels in zip(task_names, predclass_output):
        # Store predclass output directly
        results["predclass_output"][task] = sublabels
        results["LFapplier_output"][task] = {}
        
        task_module_path = MODULE_MAPPING.get(task)
        if not task_module_path:
            continue

        task_module = import_module(f"LFs.{task_module_path}")
        
        # Process each sublabel for LF voting
        for sublabel in sublabels.keys():
            matching_lfs = []
            for lf in lf_dict.get(task, []):
                if sublabel in lf and hasattr(task_module, lf):
                    lf_list = getattr(task_module, lf)
                    # Check if it's already a list
                    if isinstance(lf_list, list):
                        matching_lfs.extend(lf_list)
                    else:
                        matching_lfs.append(lf_list)
            
            if matching_lfs:
                try:
                    lf_applier = LabelingFunctionApplier(f"{task}_{sublabel}_LFs", matching_lfs)
                    data_points = [scenario]
                    lf_confidences = lf_applier.get_final_predictions(data_points)
                    
                    # Get the confidence for this sublabel from voting
                    if lf_confidences is not None:  # Check if there is a valid confidence value
                        sublabel_key = round(float(sublabel), 2) if sublabel.replace(".", "", 1).isdigit() else sublabel
                        print(f"Checking {sublabel_key} in lf_confidences")  # Debugging the confidence value  
                        # Update result with the confidence data
                        results["LFapplier_output"][task][sublabel] = lf_confidences
                    else:
                        print(f"No valid confidence found for {task} -> {sublabel}")
                        results["LFapplier_output"][task][sublabel] = 0.0
                except Exception as e:
                    print(f"Error processing {task}_{sublabel}: {str(e)}")
                    results["LFapplier_output"][task][sublabel] = 0.0
            else:
                results["LFapplier_output"][task][sublabel] = 0.0
    
    return results

def predict_scenario_logic(request_scenario: str, request_version: Union[str, int]):
    try:
        # Get model predictions
        predclass_output, pred_prob_all = pred_all_task(
            scenario=request_scenario, 
            version=request_version
        )
        
        # Load LF dictionary
        lf_dict = load_lf_dictionary()
        
        # Process predictions with new structure
        results = process_predictions(request_scenario, pred_prob_all, lf_dict)
        return results
    
    except Exception as e:
        print(traceback.format_exc())
        raise Exception(f"Unexpected error in prediction service: {str(e)}")
