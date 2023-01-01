import pytest
from unittest import mock
from models.sample_reader import DefaultPathChecker
from support.expecteds import (EXPECTED_SAMPLE_PATH,
                               CORRECT_SAMPLE_STRUCTURE,
                               EXPECTED_IMAGES_PATH,
                               VALID_IMAGE_NAMES)


@pytest.fixture
def sample_path_checker():
    return DefaultPathChecker()


@mock.patch(target="os.listdir",
            side_effect=[
                CORRECT_SAMPLE_STRUCTURE,
                VALID_IMAGE_NAMES,
                CORRECT_SAMPLE_STRUCTURE])
def test_CheckSamplePath_PathHasCorrectStructure(mock_listdir, sample_path_checker):

    assert sample_path_checker.isValid(path="..\\data\\raw_samples\\Acetone")

    mock_listdir.assert_has_calls([
        mock.call.listdir(EXPECTED_SAMPLE_PATH),
        mock.call.listdir(EXPECTED_IMAGES_PATH),
        mock.call.listdir(EXPECTED_SAMPLE_PATH),
    ])
