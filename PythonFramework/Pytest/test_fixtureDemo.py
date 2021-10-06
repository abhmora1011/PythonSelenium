# Fixtures is like BeforeTest and AfterTest
# BeforeTest is invoked before yield keyword and AfterTest after the keyword
import pytest


@pytest.mark.usefixtures("setup")
class TestFixture:   # Creating a class to optimize the call of the fixtures

    def test_fixtureDemo1(self):    # setup will tied up to this method since it is called or passed as a parameter
        print("I will execute steps in fixtureDemo1 method")

    def test_fixtureDemo(self):    # setup will tied up to this method since it is called or passed as a parameter
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo2(self):    # setup will tied up to this method since it is called or passed as a parameter
        print("I will execute steps in fixtureDemo2 method")



