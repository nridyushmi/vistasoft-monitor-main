from selenium.webdriver.chrome.options import Options
from config import Config
import pytest
from selenium import webdriver

# Add base directory path to PYTHONPATH
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

cfg = Config()
env = cfg.VSM_BASE_URL

@pytest.fixture
def config():
    return cfg

@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-extensions')
    options.add_argument("--ignore-ssl-errors=yes")
    options.add_argument("--ignore-certificate-errors")
    if cfg.HEADLESS_TEST:
        options.headless = True
    driver = webdriver.Chrome(executable_path=cfg.CHROME_DRIVER, options=options)
    #desired_capabilities = DesiredCapabilities.CHROME.copy()
    #desired_capabilities['acceptInsecureCerts'] = True
    #driver = webdriver.Chrome(executable_path='./driver/chromedriver_98', desired_capabilities=desired_capabilities)
    driver.get(env)
    driver.implicitly_wait(150)
    request.cls.driver = driver
    yield
    driver.quit()


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

@pytest.fixture(scope="session")
def user():
    u = User(cfg.USER, cfg.PASSWORD)
    yield u