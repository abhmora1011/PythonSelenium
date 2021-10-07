# Fixtures is like BeforeTest and AfterTest
# BeforeTest is invoked before yield keyword and AfterTest after the keyword
import pytest
from PythonFramework.Pytest.BaseClass import BaseClass

@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):   # When returning something it is required to call the fixture to the method
        log = self.getLogger
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        #print(dataLoad[0])
        #print(dataLoad[2])





