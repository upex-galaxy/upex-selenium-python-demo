Feature: Login

    As an User
    I want to Login the website
    so that I can select and checkout an destination.

    Scenario Outline: user logins successfully.
        Given user has signed up with credentials: "<username>", 10, "<password>".
        And user is at the Login Page "http://demo.testim.io/login".
        When user inserts username and password on the form.
        And user clicks on the Submit button.
        Then user should login. 
        Examples:
            | username | password |
            | Saitest  | Sai1234  |