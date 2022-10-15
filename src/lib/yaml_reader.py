import os
from yaml import *
import io

def get_root_dir():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_config_path():
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    return f"{ROOT_DIR}\config.yaml"

def read_config():
    config_path = get_config_path()
    
    with open(config_path, "r") as stream:
        return safe_load(stream)

def get_cavebot_waypoint(file):
    path = get_root_dir() + f"\cavebot\{file}.yaml"

    with open(path) as stream:
        return load(stream.read(), Loader)

def save_file(filename, file_data):
    yaml_path = get_root_dir() + f"\cavebot\{filename}.yaml"

    with io.open(yaml_path, "w", encoding="utf8") as outfile:
        dump(file_data, outfile, default_flow_style=False, allow_unicode=True)
        print(f"File {yaml_path} saved.")
