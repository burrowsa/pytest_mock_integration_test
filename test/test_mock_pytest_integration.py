import subprocess
import os

def test_test_names_are_not_corrupted_by_patching():
    result = subprocess.check_output([os.environ["PYTEST_EXECUTABLE"], "-v", os.path.join(os.path.dirname(__file__), "test_example.py")]).split(os.linesep)
    assert result[4].endswith("test_one PASSED")
    assert result[5].endswith("test_two PASSED")
    assert result[6].endswith("test_three PASSED")
