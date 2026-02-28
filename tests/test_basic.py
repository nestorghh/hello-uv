from hello_uv.nn import relu, Linear

def test_relu():
    assert relu(-1) == 0
    assert relu(2) == 2

def test_linear_repr():
    assert "Linear(" in repr(Linear(2, 3))
