import subprocess
import os


def check_output(*args, **kwargs):
    if hasattr(subprocess, "check_output"):
        return subprocess.check_output(*args, **kwargs)

    process = subprocess.Popen(*args, stdout=subprocess.PIPE, **kwargs)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        raise subprocess.CalledProcessError(retcode, args[0])
    return output


def test_test_names_are_not_corrupted_by_patching():
    result = check_output(["py.test", "-v", "test/test_example.py"], shell=True)
    lines = result.split(os.linesep)
    assert lines[4].endswith("test_one PASSED")
    assert lines[5].endswith("test_two PASSED")
    assert lines[6].endswith("test_three PASSED")
