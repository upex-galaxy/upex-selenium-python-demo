from behave import *
from tests.utils.drivers import Drivers
from tests.utils.locators import Locators
from tests.utils.asserts import Expect as expect


@given('user has signed up with credentials: "{username:S}", {number:d}, "{password:S}".')
def step_implX(context, username, number, password):
    global web, get
    web = Drivers().chromeDriver()
    get = Locators(web)
    assert username == "Saitest"
    assert number == 10
    assert password == "Sai1234"
    print(username)
    print(password)


@given('user is at the Login Page "{url:S}".')
def step_implA(context, url):
    web.get(url)
    expect(web.current_url).toContain("/login")


@when("user inserts username and password on the form.")
def step_implB(context):
    inputs = get.bySelectors("#login input")
    usernameInput = inputs[0]
    passwordInput = inputs[1]
    usernameInput.send_keys("upex")
    passwordInput.send_keys("galaxy")


@when("user clicks on the Submit button.")
def step_implC(context):
    submitBtn = get.bySelector('button[type=submit]')
    submitBtn.click()


@then("user should login.")
def step_impl(context):
    print(web.current_url)
    expect(web.current_url).toBeEqual("https://demo.testim.io/")
