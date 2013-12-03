import subprocess
import os

def test_test_names_are_not_corrupted_by_patching():
    result = subprocess.check_output([os.environ["PYTEST_EXECUTABLE"], "-v", os.path.join(os.path.dirname(__file__), "test_example.py")]).split(os.linesep)
    assert result[0] == "============================= test session starts ============================="
    assert result[2] == "collecting ... collected 3 items"
    assert result[3] == ""
    assert result[4].endswith("test_one PASSED")
    assert result[5].endswith("test_two PASSED")
    assert result[6].endswith("test_three PASSED")
    assert result[7] == ""
    assert result[8].startswith("========================== 3 passed in")
    assert result[8].endswith(" seconds ===========================")
