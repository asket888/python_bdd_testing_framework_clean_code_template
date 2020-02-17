from behave.runner import Context
from hamcrest import assert_that, equal_to, contains_string
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class QuestionPage(BasePage):

    # static xpath. used as is
    _QUESTION_PAGE_QUESTION_PARAMETERS = (By.XPATH, "//ul[@itemtype]")
    _QUESTION_PAGE_ANSWER_LIST = (By.XPATH, "//div[@data-test='answer-content']")

    def __init__(self, context: Context):
        super().__init__(context.driver, context.env)

    # assert methods
    def assert_that_question_page_is_presented(self):
        """
        Check if question page was downloaded successfully
        """
        assert_that(
            self.if_element_displayed(self._QUESTION_PAGE_QUESTION_PARAMETERS),
            equal_to(True),
        )

    def assert_that_answers_are_presented(self):
        """
        Check if at least one answer is presented on the page
        """
        assert_that(
            self.if_element_displayed(self._QUESTION_PAGE_ANSWER_LIST), equal_to(True)
        )

    def assert_that_question_parameter_is_like_expected(self, expected_parameter: str):
        """
        Check if question has expected parameter on its description (e.g: subject, grade)
        """
        actual_parameter = self.get_text(
            self._QUESTION_PAGE_QUESTION_PARAMETERS
        ).lower()
        expected_parameter = expected_parameter.lower()
        assert_that(actual_parameter, contains_string(expected_parameter))
