import pytest
# to run use the -m stands for mark
# you can mark (tag) the test by using @pytest.mark.<tagname>


@pytest.mark.smoke  # To group methods
@pytest.mark.skip   # to skip the test
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because the string do not match"   # The second argument will be the error message


@pytest.mark.smoke
def test_creditProgram():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"





