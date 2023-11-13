*** Settings ***
Resource    resource.robot
Test Setup    Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input User Details    palle   palle123
    Output Should Contain   New user registered


Register With Already Taken Username And Valid Password
    Input User Details    kalle   kalle123
    Output Should Contain   Username already exists


Register With Too Short Username And Valid Password
    Input User Details    ka   kalle123
    Output Should Contain   Invalid username, at least 3 characters and only a-z allowed

Register With Enough Long But Invald Username And Valid Password
    Input User Details    kalle1   kalle123
    Output Should Contain   Invalid username, at least 3 characters and only a-z allowed

Register With Valid Username And Too Short Password
    Input User Details    kallee   kalle12
    Output Should Contain   Invalid password, at least 8 characters and one special character required

Register With Valid Username And Long Enough Password Containing Only Letters
    Input User Details    kalleee   kallekoo
    Output Should Contain   Invalid password, at least 8 characters and one special character required

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User    kalle   kalle123

