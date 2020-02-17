from behave import step
from behave.runner import Context


@step("Main Page is downloaded successfully")
def step_impl(context: Context):
    context.main_page.assert_that_main_page_presented()


@step("I filter questions by following parameters")
def step_impl(context: Context):
    context.subject_name = context.main_page.get_subject_name_by_value()
    context.grade_name = context.main_page.get_grade_name_by_value()
    context.main_page.filter_questions()


@step("I click first filtered question")
def step_impl(context: Context):
    context.main_page.click_first_question()
