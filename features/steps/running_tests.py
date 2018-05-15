from behave import given, when, then
from sure import this


@given(u'this step exists')
def step_exists(context):
    pass


@when(u'I run "python manage.py behave"')
def run_command(context):
    pass


@then(u'I should see the behave tests run')
def is_running(context):
    pass


@then(u'django_ready should be called')
def django_context(context):
    return this(context.django).should.be.ok
