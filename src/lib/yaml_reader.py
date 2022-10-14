import os
import yaml
import io

def get_root_dir():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_config_path():
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    return f"{ROOT_DIR}\config.yaml"

def read_config():
    config_path = get_config_path()
    
    with open(config_path, "r") as stream:
        return yaml.safe_load(stream)

def update_config(yaml_path, file_data):
    with io.open(yaml_path, "w", encoding="utf8") as outfile:
        yaml.dump(file_data, outfile, default_flow_style=False, allow_unicode=True)
        print(f"File {yaml_path} saved.")
