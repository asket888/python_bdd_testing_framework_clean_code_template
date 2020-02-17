from allure import attach, attachment_type
from behave.model import Scenario
from behave.runner import Context

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.question_page import QuestionPage

from utils.config_util import get_env, get_driver


def before_all(context: Context):
    # setup global variables
    context.env = get_env(context.config.userdata["env"])
    context.driver = get_driver(context.config.userdata["browser"])
    # setup page_objects
    context.login_page = LoginPage(context)
    context.main_page = MainPage(context)
    context.question_page = QuestionPage(context)


def after_scenario(context: Context, scenario: Scenario):
    if scenario.status == "failed":
        attach(
            context.driver.get_screenshot_as_png(),
            attachment_type=attachment_type.PNG
        )


def after_all(context: Context):
    context.driver.quit()
