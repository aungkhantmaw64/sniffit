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
from typing import Dict, Any
import os


class SamplePathChecker(ABC):

    @abstractmethod
    def isValid(self, path: str) -> bool:
        pass


class SampleReader(ABC):

    @abstractmethod
    def read(self, path) -> Dict[str, Any]:
        pass


class DefaultPathChecker(SamplePathChecker):

    def __hasCsvFile(self, path: str) -> bool:
        """This private helper method checks
        if the given path has a file with .csv format.

        Args:
            path (str): Sample path.

        Returns:
            bool: True if .csv file is found, False otherwise.
        """
        entries = os.listdir(path)
        for entry in entries:
            if entry[-4:] == ".csv":
                return True
        return False

    def __hasImageFolder(self, path: str) -> bool:
        """This private helper methods check
        if the given path has a folder name "images", that has at least an image file with .jpg format.

        Args:
            path (str): Sample path.

        Returns:
            bool: True if the image folder is found, False otherwise.
        """
        pathEntries = os.listdir(path)
        if "images" in pathEntries:
            imagesPath = os.path.join(path, "images")
            imageEntries = os.listdir(imagesPath)
            if len(imageEntries) > 0:
                for entry in imageEntries:
                    if entry[-4:] == ".jpg":
                        return True
        return False

    def isValid(self, path: str) -> bool:
        """This method checks if the given path is a valid sample directory according to HybridEnose's Rules.

        Args:
            path (str): Sample path

        Returns:
            bool: True if the sample directory is valid, False otherwise.
        """
        return (self.__hasImageFolder(path) and self.__hasCsvFile(path))
