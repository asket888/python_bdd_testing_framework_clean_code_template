from os import path
from typing import Tuple, List

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage:

    _IMPLICIT_TIMEOUT = 10
    _EXPLICIT_TIMEOUT = 30

    def __init__(self, driver: webdriver, env: dict):
        self.env = env
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(BasePage._IMPLICIT_TIMEOUT)
        self.explicitly_wait = WebDriverWait(driver, BasePage._EXPLICIT_TIMEOUT)

    # element wait methods
    def _is_element_visible(self, by_locator: Tuple[By, str]):
        """
        Wait till element will appear in DOM model
        :param by_locator: tuple parameter with type of locator and its value (e.g: (By.ID, "submit"))
        """
        self.explicitly_wait.until(
            expected_conditions.visibility_of_element_located(by_locator),
            message=f"'{by_locator}' element doesn't appear on the page"
        )

    def _is_element_not_visible(self, by_locator: Tuple[By, str]):
        """
        Wait till element will disappear from DOM model
        :param by_locator: tuple parameter with type of locator and its value (e.g: (By.ID, "submit"))
        """
        self.explicitly_wait.until(
            expected_conditions.invisibility_of_element_located(by_locator),
            message=f"'{by_locator}' element doesn't disappear from the page"
        )

    def _is_element_clickable(self, by_locator: Tuple[By, str]):
        """
        Wait till element will be clickable in DOM model
        :param by_locator: tuple parameter with type of locator and its value (e.g: (By.ID, "submit"))
        """
        self.explicitly_wait.until(
            expected_conditions.element_to_be_clickable(by_locator),
            message=f"'{by_locator}' element is not clickable on the page"
        )

    # element status methods
    def if_element_displayed(self, by_locator: Tuple[By, str]) -> bool:
        """
        Check if element is presented on the page
        :param by_locator: tuple parameter with type of locator and its value (e.g: (By.ID, "submit"))
        :returns boolean parameter True if element is displayed
        """
        self._is_element_visible(by_locator)
        return self.driver.find_element(*by_locator).is_displayed()

    def if_element_not_displayed(self, by_locator: Tuple[By, str]) -> bool:
        """
        Check if element is not presented on the page
        :param by_locator: tuple parameter with type of locator and its value (e.g: (By.ID, "submit"))
        :returns boolean parameter True if element is NOT displayed
        """
        self._is_element_not_visible(by_locator)
        return not self.driver.find_element(*by_locator).is_displayed()

    # elements set actions methods
    def click(self, by_locator: Tuple[By, str]):
        """
        Click an element
        :param by_locator: tuple parameter with type of locator and its value (e.g: (By.ID, "submit"))
        """
        self._is_element_clickable(by_locator)
        self.driver.find_element(*by_locator).click()

    def clear(self, by_locator: Tuple[By, str]):
        """
        Clear an element
        :param by_locator: tuple parameter with type of locator and its value (e.g: (By.ID, "submit"))
        """
        self._is_element_visible(by_locator)
        self.driver.find_element(*by_locator).clear()

    def fill(self, by_locator: Tuple[By, str], value: str):
        """
        Fill element by text
        :param by_locator: tuple parameter with type of locator and its value (e.g: (By.ID, "submit"))
        :param value: string to be typed
        """
        self._is_element_visible(by_locator)
        self.driver.find_element(*by_locator).clear()
        self.driver.find_element(*by_locator).send_keys(value)

    def select(self, by_locator: Tuple[By, str], value: str):
        """
        Select dropdown value using selenium selector
        :param by_locator: tuple parameter with type of locator and its value (e.g: (By.ID, "submit"))
        :param value: dropdown option to be selected
        """
        self._is_element_visible(by_locator)
        Select(self.driver.find_element(*by_locator)).select_by_visible_text(value)

    def select_from_dropdown(self, by_select_locator: Tuple[By, str], by_option_locator: Tuple[By, str]):
        """
        Select dropdown value using simple clicking logic (when selector doesn't work)
        :param by_select_locator: tuple parameter with type of select locator and its value (e.g: (By.ID, "submit"))
        :param by_option_locator: tuple parameter with type of option locator and its value (e.g: (By.ID, "submit"))
        """
        self._is_element_clickable(by_select_locator)
        self.driver.find_element(*by_select_locator).click()
        self._is_element_clickable(by_option_locator)
        self.driver.find_element(*by_option_locator).click()

    # elements get actions methods
    def get_text(self, by_locator: Tuple[By, str]) -> str:
        """
        Return text from element
        :param by_locator: tuple parameter with type of locator and its value (e.g: (By.ID, "submit"))
        :returns string with text from an element
        """
        self._is_element_visible(by_locator)
        return self.driver.find_element(*by_locator).text

    def get_all_elements(self, by_locator: Tuple[By, str]) -> List[object]:
        """
        Return all elements with the same locator as a list
        :param by_locator: tuple parameter with type of locator and its value (e.g: (By.ID, "submit"))
        :returns list with all elements matched to locator
        """
        self._is_element_visible(by_locator)
        return self.driver.find_elements(*by_locator)

    # overall_steps browser actions
    def goto_url(self, url: str):
        """
        Open URL in browser
        :param url: URL to be opened
        """
        self.driver.get(url)

    def refresh_current_page(self):
        """
        Refresh current browser page
        """
        self.driver.refresh()

    def clean_browser_cookies(self):
        """
        Clear browser cookies
        """
        self.driver.delete_all_cookies()

    def take_screenshot(self, screenshot_title: str):
        """
        Take screenshoot and saves it as .png file to ./artifacts directory
        :param screenshot_title: screenshoot name
        """
        self.driver.save_screenshot(
            path.join(path.dirname(path.dirname(path.realpath(__file__))))
            + "/artifacts/["
            + screenshot_title
            + "].png"
        )

    def quit(self):
        """
        Close all browser windows and end the session
        """
        if self.driver is not None:
            self.driver.quit()
