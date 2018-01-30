*** Settings ***
Library          Selenium2Library
Documentation    Suite description

*** Test Cases ***
Valid Login
    [Tags]    Smoke
    Open Login Page
    Input email     test@testr.co
    Input password  areallystrongpassword
    Submit Credentials
    Projects Page Should Be Open

*** Keywords ***
Provided precondition
    Setup system under test

Open Login Page
    Open Browser    http://localhost:8000/accounts/login


