import os
from pathlib import Path

from data_access.handlers.__class_feather_handler import Feather
from data_access.handlers.__class_pickle_handler import Pickle
from data_access.handlers.__class_yaml_handler import Yaml
from data_access.handlers.__class_toml_handler import Toml
from data_access.handlers.__class_json_handler import Json
from data_access.handlers.__class_txt_handler import Txt


class UniversalHandler:

    file_handler_pointer = {
        '': Txt,
        '.txt': Txt,
        '.yaml': Yaml,
        '.toml': Toml,
        '.json': Json,
        '.pickle': Pickle,
        '.pkl': Pickle,
        '.feather': Feather,
        '.fthr': Feather
    }

    def __init__(self, link, work_dir=None):
        self.link = Path(link)
        self.link_folder = self.link.parent
        self.work_dir = Path(work_dir) if work_dir else None
        self.file_type = self.file_type_recognition()
        self.handler_class = self.get_handler()
        self.handler = self.handler_class(self.link, self.link_folder, work_dir=work_dir)

    def read_data(self):
        return self.handler.get()

    def write_data(self, data):
        if not self.link_folder.exists():
            os.makedirs(self.link_folder)
        self.handler.put(data)

    def get_handler(self):
        # If handler class is not recognized, assuming it is the class Txt
        return self.file_handler_pointer.get(self.file_type, Txt)

    def file_type_recognition(self):
        return self.link.suffix

