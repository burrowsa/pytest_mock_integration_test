import subprocess
import os

def test_test_names_are_not_corrupted_by_patching():
    py_test = os.path.join(os.environ["VIRTUAL_ENV"], "scripts", "py.test")
    result = subprocess.check_output([py_test, "-v", "test_example.py"]).split(os.linesep)
    assert result[0] == "============================= test session starts ============================="
    assert result[2] == "collecting ... collected 3 items"
    assert result[3] == ""
    assert result[4] == r"test_example.py <- C:\Users\Andrew\projects\python_workspace\pytest_mock_integration_test\test\test_example.py:11: test_one PASSED"
    assert result[5] == r"test_example.py <- C:\Users\Andrew\projects\python_workspace\pytest_mock_integration_test\test\test_example.py:15: test_two PASSED"
    assert result[6] == r"test_example.py <- C:\Users\Andrew\projects\python_workspace\pytest_mock_integration_test\test\test_example.py:19: test_three PASSED"
    assert result[7] == ""
    assert result[8].startswith("========================== 3 passed in")
    assert result[8].endswith(" seconds ===========================")
