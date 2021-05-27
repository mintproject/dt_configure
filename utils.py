import yaml
from yaml import Loader
from pathlib import Path

def get_spec(config_yaml_path: Path) -> dict:
    spec = yaml.load(config_yaml_path.open(), Loader=Loader)
    return spec

def write_to_yaml(config_yaml_path: Path, spec):
    """
    This function makes sure that the comments get saved when writing new data to the yaml file
    @param config_yaml_path: path
    @param spec: data for yaml
    """
    with open(config_yaml_path, 'w') as f:
        yaml.dump(spec, f, sort_keys=False)
