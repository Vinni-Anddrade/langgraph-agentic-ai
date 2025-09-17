import yaml
from box import ConfigBox


def read_yaml(path: str) -> ConfigBox:
    with open(path, "r") as yaml_file:
        output_file = yaml.safe_load(yaml_file)

    return ConfigBox(output_file)
