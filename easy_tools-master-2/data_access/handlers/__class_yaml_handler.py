import yaml
from data_access.handlers.__class_abstract_handler import AbstractHandler


class Yaml(AbstractHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self):
        with open(self.link) as yaml_file:
            return yaml.load(yaml_file, Loader=yaml.loader.SafeLoader)

    def put(self, data: dict = None):
        data = data if data else {}
        with open(self.link, 'w') as yaml_file:
            result = yaml.dump(data, yaml_file)
        return result or data
