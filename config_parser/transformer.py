import yaml

def transform_to_yaml(data):
    return yaml.dump(data, default_flow_style=False)
