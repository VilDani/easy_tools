import pickle
from data_access.handlers.__class_abstract_handler import AbstractHandler


class Pickle(AbstractHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self):
        pass

    def put(self, data=None):
        pass
