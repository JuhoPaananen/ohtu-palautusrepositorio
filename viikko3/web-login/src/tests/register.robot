*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Reset Application
    Set Username    palle
    Set Password    palle123
    Set Password Confirmation    palle123
    Submit User Registration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Reset Application
    Set Username    pa
    Set Password    palle123
    Set Password Confirmation   palle123
    Submit User Registration
    Register Should Fail With Message    Invalid username, at least 3 characters and only a-z allowed

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Reset Application
    Set Username    palle
    Set Password    palle
    Set Password Confirmation   palle
    Submit User Registration
    Register Should Fail With Message    Invalid password, at least 8 characters and one special character required

Register With Nonmatching Password And Password Confirmation
    Reset Application
    Set Username    palle
    Set Password    palle123
    Set Password Confirmation   palle1234
    Submit User Registration
    Register Should Fail With Message    Password and password confirmation do not match

Login After Successful Registration
    Reset Application
    Set Username    palle
    Set Password    palle123
    Set Password Confirmation    palle123
    Submit User Registration
    Welcome Page Should Be Open
    Go To Ohtu Page
    Logout User
    Set Username  palle
    Set Password  palle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Reset Application
    Set Username    palle!
    Set Password    palle123
    Set Password Confirmation   palle123
    Submit User Registration
    Register Should Fail With Message    Invalid username, at least 3 characters and only a-z allowed
    Go To Login Page
    Set Username  palle!
    Set Password  palle123
    Submit Credentials
    Login Should Fail With Message    Invalid username or password

*** Keywords ***
Submit User Registration
    Click Button    Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open 
    Page Should Contain  ${message}


