import pandas as pd
from data_access.handlers.__class_abstract_handler import AbstractHandler


class Feather(AbstractHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self):
        return pd.read_feather(self.link)

    def put(self, data_frame: pd.DataFrame = pd.DataFrame()):
        # Deleting all indexes - feather format doesn't support them
        return data_frame.reset_index().to_feather(self.link)
    