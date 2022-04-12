import os
import json

project_root = os.path.dirname(__file__)
with open(os.path.join(project_root, '../../reinvent_chemistry/configs/config.json'), 'r') as f:
    config = json.load(f)

MAIN_TEST_PATH = config["MAIN_TEST_PATH"]

REACTION_DEFINITIONS_PATH = config["TEST_RESOURCES"]["REACTION_DEFINITIONS_PATH"]
AIZYNTH_PREDICTION_URL = config["AIZYNTH"]["AIZYNTH_PREDICTION_URL"]
AIZYNTH_BUILDING_BLOCKS_URL = config["AIZYNTH"]["AIZYNTH_BUILDING_BLOCKS_URL"]
AIZYNTH_TOKEN = config["AIZYNTH"]["AIZYNTH_TOKEN"]
