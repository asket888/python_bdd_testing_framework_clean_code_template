from behave.runner import Context
from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):

    # static xpath. used as is
    _MAIN_PAGE_VERIFICATION_MESSAGE = (By.XPATH, "//a[@label='home ask question top']")
    _MAIN_PAGE_SUBJECTS_TAB = (By.XPATH, "//div[contains(@class,'sg-box__hole')]//li[2]")
    _MAIN_PAGE_GRADES_FILTER_DROPDOWN = (By.ID, "grades")
    _MAIN_PAGE_GRADES_FILTER_OPTION = (By.XPATH, "//select[@id='grades']/option[@value='2']")
    _MAIN_PAGE_STATUS_FILTER_DROPDOWN = (By.ID, "status")
    _MAIN_PAGE_STATUS_FILTER_OPTION = (By.XPATH, "//select[@id='status']/option[@value='ANSWERED']")
    _MAIN_PAGE_FIRST_QUESTION_BUTTON = (By.XPATH, "//div[@data-test='feed-item'][1]//a/p/span")

    def __init__(self, context: Context):
        super().__init__(context.driver, context.env)

    # action methods
    def click_first_question(self):
        """
        Click first available question in questions list
        """
        self.click(self._MAIN_PAGE_FIRST_QUESTION_BUTTON)

    def get_grade_name_by_value(self) -> str:
        """
        Get grade text name from locator
        :returns grade text name depends from its value in DOM model
        """
        return self.get_text(self._MAIN_PAGE_GRADES_FILTER_OPTION)

    def get_subject_name_by_value(self) -> str:
        """
        Get subject text name from locator
        :returns subject text name depends from its value in DOM model
        """
        return self.get_text(self._MAIN_PAGE_SUBJECTS_TAB)

    def filter_questions(self):
        """
        Filter questions by subject, grade and answer status parameters
        """
        self.click(self._MAIN_PAGE_SUBJECTS_TAB)
        self.select_from_dropdown(
            self._MAIN_PAGE_GRADES_FILTER_DROPDOWN, self._MAIN_PAGE_GRADES_FILTER_OPTION
        )
        self.select_from_dropdown(
            self._MAIN_PAGE_STATUS_FILTER_DROPDOWN, self._MAIN_PAGE_STATUS_FILTER_OPTION
        )

    # assert methods
    def assert_that_main_page_presented(self):
        """
        Check if main page was downloaded successfully
        """
        assert_that(
            self.if_element_displayed(self._MAIN_PAGE_VERIFICATION_MESSAGE),
            equal_to(True)
        )
