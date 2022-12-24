'''
Raw experimental samples are stored as follows:

    GasName
        |_images
        |   |_1.jpg
        |   |_2.jpg
        |   |_3.jpg
        |   |_etc.
        |_serialdata.csv
'''
from abc import ABC, abstractmethod
from typing import Dict
import os


class SamplePathChecker(ABC):

    @abstractmethod
    def isSample(self, path: str) -> bool:
        pass


class SampleReader(ABC):

    @abstractmethod
    def read(self, path) -> Dict:
        pass


class HybridEnosePathChecker(SamplePathChecker):

    def __hasCsvFile(self, path: str) -> bool:
        entries = os.listdir(path)
        for entry in entries:
            if entry[-4:] == ".csv":
                return True
        return False

    def __hasImageFolder(self, path: str) -> bool:
        pathEntries = os.listdir(path)
        if "images" in pathEntries:
            imagesPath = os.path.join(path, "images")
            imageEntries = os.listdir(imagesPath)
            if len(imageEntries) > 0:
                for entry in imageEntries:
                    if entry[-4:] == ".jpg":
                        return True
        return False

    def isSample(self, path: str) -> bool:
        return (self.__hasImageFolder(path) and self.__hasCsvFile(path))


class HybridEnoseSampleReader(SampleReader):

    def read(self, path: str) -> Dict:
        pass
