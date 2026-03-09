from abc import ABC, abstractmethod
from typing import Dict


class Person(ABC):

    @abstractmethod
    def get_details(self) -> str:
        pass

    @abstractmethod
    def to_dict(self) -> Dict:
        pass