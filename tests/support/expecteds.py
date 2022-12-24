import os

EXPECTED_SAMPLE_PATH = "..\\data\\raw_samples\\Acetone"
EXPECTED_SAMPLE_NAME = "Acetone"
EXPECTED_SAMPLE_LIST = ["Acetone",
                        "Ammonia",
                        "Benzene",
                        "Ethanol",
                        "Methanol",
                        "Toluene"]

EXPECTED_IMAGES_PATH = os.path.join(EXPECTED_SAMPLE_PATH, "images")

CORRECT_SAMPLE_STRUCTURE = ["images",
                            "serialdata.csv"]

VALID_IMAGE_NAMES = ["1.jpg",
                     "2.jpg",
                     "3.jpg"]
