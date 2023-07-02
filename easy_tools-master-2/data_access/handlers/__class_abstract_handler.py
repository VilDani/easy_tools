from abc import ABC, abstractmethod
from pathlib import Path


class AbstractHandler(ABC):
    def __init__(self, link, link_folder, work_dir=None):
        self.link = link
        self.link_folder = link_folder
        self.work_dir = Path(work_dir) if work_dir else None

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def put(self, data):
        pass

