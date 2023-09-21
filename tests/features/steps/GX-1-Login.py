from behave import *
from tests.utils.drivers import *


@given('user has signed up with credentials: "{username:S}", {number:d}, "{password:S}".')
def step_implX(context, username, number, password):
    assert username == "Saitest"
    assert number == 10
    assert password == "Sai1234"
    print(username)
    print(password)


@given('user is at the Login Page "{url:S}".')
def step_implA(context, url, web):
    web.get(url)


@when("user inserts username and password on the form.")
def step_implB(context):
    assert 1 == 1


@when("user clicks on the Submit button.")
def step_implC(context):
    assert 1 == 1


@then("user should login.")
def step_impl(context):
    assert 1 == 1
