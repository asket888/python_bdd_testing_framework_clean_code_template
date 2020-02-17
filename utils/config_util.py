from json import load

from selenium import webdriver
from selenium.webdriver import chrome, firefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def get_driver(browser: str) -> webdriver:
    """
    Creates webdriver object depended from given browser parameter
    :param browser: which driver should be created
    """
    driver = None
    if browser.upper() == "CH":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser.upper() == "CH_HL":
        options = chrome.options.Options()
        options.add_argument("--window-size=1600x900")
        options.headless = True
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(), chrome_options=options
        )
    elif browser.upper() == "FF":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser.upper() == "FF_HL":
        options = firefox.options.Options()
        options.add_argument("--window-size=1600x900")
        options.headless = True
        driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install(), firefox_options=options
        )
    elif browser.upper() == "SF":
        driver = webdriver.Safari()
    else:
        raise TypeError(
            f"Unexpected browser '{browser.upper()}'."
            f"Check your behave.ini file for available variables"
        )
    return driver


def get_env(env: str) -> dict:
    """
    Returns url and login parameters of chosen environment
    :param env: which environment parameters should be returned
    """
    env_parameters = None
    if env.upper() == "LOCALHOST":
        env_parameters = _read_config("LOCALHOST")

    elif env.upper() == "STAGE_US":
        env_parameters = _read_config("STAGE_US")
    elif env.upper() == "STAGE_RU":
        env_parameters = _read_config("STAGE_RU")
    elif env.upper() == "STAGE_PL":
        env_parameters = _read_config("STAGE_PL")

    elif env.upper() == "PROD_US":
        env_parameters = _read_config("PROD_US")
    elif env.upper() == "PROD_RU":
        env_parameters = _read_config("PROD_RU")
    elif env.upper() == "PROD_PL":
        env_parameters = _read_config("PROD_PL")

    else:
        raise TypeError(
            f"Unexpected env '{env.upper()}'."
            f"Check your behave.ini file for available variables"
        )

    return env_parameters


def _read_config(env: str) -> dict:
    """
    Reads config file to get environment parameters
    :param env: which environment parameters should be returned
    """
    with open("config.json") as json_file:
        as_dict = load(json_file)[env]
        return as_dict
