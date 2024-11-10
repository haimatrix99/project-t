import os
import yaml
from yaml.loader import SafeLoader

from constants import AUTH_PATH

def load_config():
    if os.path.exists(AUTH_PATH):
        with open(AUTH_PATH) as file:
            config = yaml.load(file, Loader=SafeLoader)
        return config 
    else:
        raise ValueError("Auth config does not be exists for authentication!!!")