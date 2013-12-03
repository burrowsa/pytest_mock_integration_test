from mock import patch, sentinel, Mock


class M(object):
    pass

obj = M()
obj.value = sentinel.foo


@patch("os.path")
def test_one(mock_os_path):
    assert isinstance(mock_os_path, Mock)

@patch.object(obj, "value", sentinel.bar)
def test_two():
    assert obj.value == sentinel.bar


def test_three():
    assert obj.value == sentinel.foo
