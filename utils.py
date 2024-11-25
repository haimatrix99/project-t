import os

import yaml
from ultralytics import YOLO
from yaml.loader import SafeLoader

from constants import AUTH_PATH


def load_config():
    if os.path.exists(AUTH_PATH):
        with open(AUTH_PATH) as file:
            config = yaml.load(file, Loader=SafeLoader)
        return config
    else:
        raise ValueError("Auth config does not be exists for authentication!!!")


def load_model(model_path):
    """
    Loads a YOLO object detection model from the specified model_path.

    Parameters:
        model_path (str): The path to the YOLO model file.

    Returns:
        A YOLO object detection model.
    """
    model = YOLO(model_path)
    return model
