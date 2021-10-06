# Any pytest file should start with test_ in the file name or end it by _test
# pytest method names should start with test
# Any code should wrap in method only
# method name should have sense
# -k <regex> stands for method names execution, -s logs in out put, -v stands for more info metadata
# you can run specific file with py.test <filename>
# fixture is used for setup
# by using conftest.py file it will be possible to inherit the setup to all test file
# datadriven and parameriterizartion can be done thru return statement in list format
# when you define fixture scope to class only, it will run once before class is initiated and at the end
import pytest


def test_firstProgram(setup):
    print("Hello")


@pytest.mark.xfail  # Skip the reporting
def test_secondProgram():
    print("World!")


def test_crossBrowser(crossBrowser):    # This will run 3 times
    print(crossBrowser[1])