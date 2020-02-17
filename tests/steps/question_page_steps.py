from behave import step
from behave.runner import Context


@step("question page is presented")
def step_impl(context: Context):
    context.question_page.assert_that_question_page_is_presented()


@step("question has correct subject and education_level parameter")
def step_impl(context: Context):
    expected_grade_name = context.grade_name
    expected_subject_name = context.subject_name
    context.question_page.assert_that_question_parameter_is_like_expected(
        expected_parameter=expected_grade_name
    )
    context.question_page.assert_that_question_parameter_is_like_expected(
        expected_parameter=expected_subject_name
    )


@step("at least one answer is presented on the page")
def step_impl(context: Context):
    context.question_page.assert_that_answers_are_presented()
