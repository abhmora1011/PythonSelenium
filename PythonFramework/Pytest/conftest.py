# This can be inherited automatically to all test in the folder

import pytest


@pytest.fixture(scope="class")   # BeforeTest
def setup():
    print("I will executed first")
    yield   # keyword used to invoke AfterTest
    print("Close Session")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Abraham", "Ora", "abraham.morial.ora@gmil.com"]


@pytest.fixture(params=[("Chrome", "Abraham"), ("Firefox", "Gale"), ("IE", "Rhys")])
def crossBrowser(request):  # request param is required to fetch the parameter values
    return request.param

