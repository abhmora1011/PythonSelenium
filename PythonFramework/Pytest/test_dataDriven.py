# Fixtures is like BeforeTest and AfterTest
# BeforeTest is invoked before yield keyword and AfterTest after the keyword
import pytest


@pytest.mark.usefixtures("dataLoad")
class TestDataDriven:

    def test_editProfile(self, dataLoad):   # When returning something it is required to call the fixture to the method
        print(dataLoad[0])
        print(dataLoad[2])





