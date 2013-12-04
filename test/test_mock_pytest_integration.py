import subprocess
import os


def check_output(*args, **kwargs):
    if hasattr(subprocess, "check_output"):
        return subprocess.check_output(*args, **kwargs)

    process = subprocess.Popen(*args, stdout=subprocess.PIPE, **kwargs)
    output, unused_err = process.communicate()
    retcode = process.wait()
    if retcode:
        raise subprocess.CalledProcessError(retcode, args[0])
    return output


def test_test_names_are_not_corrupted_by_patching():
    result = check_output([os.environ["PYTEST_EXECUTABLE"], "-v", "test/test_example.py"])
    lines = result.splitlines()
    assert lines[4].endswith(b"test_one PASSED")
    assert lines[5].endswith(b"test_two PASSED")
    assert lines[6].endswith(b"test_three PASSED")
