import os
import pandas as pd
import json
import sys
import warnings

sys.path.append("../../")
sys.path.append("../")
sys.path.append("../codes/")
import sys

# Get the absolute path of the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from helper.create_dir_files_path import (
    define_log_and_param_paths,
)  # Now it should work

from spear.jl import JL
from spear.utils import get_data
from task_utils import embedding

warnings.filterwarnings("ignore")


def pred_task(scenario, version=1, labels="Category", scenario_embedding=None):
    if scenario_embedding is None:
        scenario_embedding = embedding.scenarios_embedding(scenario)

    (log_path_1, params_path) = define_log_and_param_paths(version, labels, "JL")
    U_path_pkl = f"/home/user/IITB/LFi/LFs/{labels}/result/{labels}_pickle_U.pkl"
    path_json = f"/home/user/IITB/LFi/LFs/{labels}/result/{labels}.json"
    print(U_path_pkl)  # Print the exact path being used
    print(os.path.exists(U_path_pkl))  # Check if file exists
    # Load data
    data_U = get_data(path=U_path_pkl, check_shapes=True)
    n_lfs = data_U[1].shape[1]

    # JL Configuration settings
    feature_model = "nn"
    n_features = 768
    n_hidden = 512

    jl = JL(
        path_json=path_json,
        n_lfs=n_lfs,
        n_features=n_features,
        n_hidden=n_hidden,
        feature_model=feature_model,
    )

    jl.load_params(params_path)

    pred_prob = jl.predict_fm_proba(scenario_embedding)
    pred = jl.predict_fm(scenario_embedding)

    classes = json.load(open(path_json))
    pred_class = classes[str(pred[0])]

    pred_prob_dict = {classes[i]: pred_prob[0][int(i)] for i in classes}

    return pred_class, pred_prob_dict


def pred_all_task(scenario, version=1, scenario_embedding=None):
    if scenario_embedding is None:
        scenario_embedding = embedding.scenarios_embedding(scenario)

    pred_class_all = []
    pred_prob_all = []

    full_path = "/home/user/IITB/LFi/data/processed/version7/full.csv"
    df_full = pd.read_csv(full_path)
    # all_tasks = df_full.columns[1:]
    all_tasks = [
        "Category",
        "SubMission",
        "Criticality",
        "Level",
        "Action",
        "Entity",
        "TaskObjective",
        "Constraints",
        "ObjectiveFunction",
    ]

    for labels in all_tasks:
        pred_class, pred_prob = pred_task(
            scenario,
            version=version,
            labels=labels,
            scenario_embedding=scenario_embedding,
        )
        pred_class_all.append(pred_class)
        pred_prob_all.append(pred_prob)

    return pred_class_all, pred_prob_all


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--scenario', type=str, required=True,
    #                     help='Enter Scenario to extract the context')
    # parser.add_argument('--version', type=int, default=2,
    #                     help='Version number (default: 2)')

    # args = parser.parse_args()

    scenario = [
        "An unidentified missile has been detected on radar, approaching the fleet at high speed. Its trajectory indicates a possible direct impact. All defense systems must be activated immediately to intercept the threat."
    ]  # Your input text
    version = 7

    pred_class_all, pred_prob_all = pred_all_task(scenario, version=version)
    print(pred_class_all, pred_prob_all)
