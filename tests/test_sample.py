import sample_app.sample as sample

def test_use_library():
    result = sample.use_library()
    assert result.foo == 42
    assert round(result.bar, 2) == 3.14
    assert result.baz is True
