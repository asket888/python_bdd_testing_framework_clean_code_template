from behave import step
from behave.runner import Context


@step("I login to application with correct credentials")
def step_impl(context: Context):
    context.login_page.login_with_correct_credentials()
