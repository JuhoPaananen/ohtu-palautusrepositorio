*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username    palle
    Set Password    palle123
    Set Password    palle123
    Submit User Registration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username    pa
    Set Password    palle123
    Set Password    palle123
    Submit User Registration
    Register Should Fail

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username    palle
    Set Password    palle
    Set Password    palle
    Submit User Registration
    Register Should Fail

Register With Nonmatching Password And Password Confirmation
    Set Username    palle
    Set Password    palle123
    Set Password    palle1234
    Submit User Registration
    Register Should Fail

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

Register Should Fail
    Register Page Should Be Open

