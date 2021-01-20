from selenium import webdriver
import pytest

@pytest.fixture()
def setup(bwsr):
    if bwsr=='chrome':
        driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
        print("Launching Chrome browser.....")
    elif bwsr=='firefox':
        print("Launching Firefox browser.....")
        driver = webdriver.Firefox(executable_path="./drivers/geckodriver.exe")

    else:
        print("Launching Edge browser.....")
        driver = webdriver.Edge(executable_path="./drivers/msedgedriver.exe")
    return driver


def pytest_addoption(parser): # This will get the value from CLI/Hooks
    parser.addoption("--browser")

@pytest.fixture()
def bwsr(request): #This will return the Browser value to setup method
    return request.config.getoption("--browser")

############### Pytest HTML Report #############

#It is hook for adding Enviroment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Manjunatha'

 # It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


