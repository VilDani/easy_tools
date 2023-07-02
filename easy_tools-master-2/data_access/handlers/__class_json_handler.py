import json
from data_access.handlers.__class_abstract_handler import AbstractHandler


class Json(AbstractHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self):
        with open(self.link) as json_file:
            data = json.load(json_file)
        return data

    def put(self, data: dict = None):
        data = data if data else {}
        with open(self.link, 'w') as json_file:
            json.dump(data, json_file, ensure_ascii=True, indent=4)
        return data
