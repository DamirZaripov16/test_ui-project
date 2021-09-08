[![Build Status](https://app.travis-ci.com/DamirZaripov16/test_ui-project.svg?branch=master)](https://app.travis-ci.com/DamirZaripov16/test_ui-project)

# Autotests for ["Qamoodle"](https://qacoursemoodle.innopolis.university) app

## Installation
***
1. Define a directory on a local machine
2. Clone the [project](https://github.com/DamirZaripov16/test_ui-project) <br>
   ```git clone https://github.com/DamirZaripov16/test_ui-project```
3. Open the project
4. Install all the requirements within **requirements.txt** <br>
pip install -r /path/to/requirements.txt
## About
***
### Authorization form check
Positive tests:
* Authorization with valid login and valid password<br>

Negative tests:
* Empty login
* Empty password<br>
__Initial file__: tests/auth/test_auth.py
### Course creation check
Positive tests:
* Course creation/deletion<br>

Negative tests:
* Unavailable course creation without fullname of the course
* Unavailable course creation without shortname of the course<br>
__Initial file__: tests/auth/test_auth.py
### Personal data update check
Positive tests:
* Filling all the fields with valid data

Required fields negative tests:
* Required fields consequent filling with invalid data<br>
__Initial file__: \tests\personal_data\test_personal_data.py
### Signing up check
Positive tests:
* Filling all the fields with valid data and eventual registration of a new user

Required fields negative tests:
* Required fields consequent filling with invalid data and unavailable registration of a new user<br>
* __Initial file__: tests/sign_up/test_sign_up.py
##  Allure reports
***
1) Install _**Allure commandline application**_ on your OS
   
**Windows-users**:
   1) Run _**PowerShell**_ and install _**Allure commandline application**_ by the following command:
   <br>```scoop install allure```<br>
   2) Download _**Allure commandline application**_ manually if you don't have **_scoop_** installed<br>
   3) Java is required no matter which installation way you choose<br>

**Linux and MacOS users** watch [this](https://docs.qameta.io/allure/#_installing_a_commandline). 

2) Run ```pytest --alluredir=allure_reports``` on your IDE for tests completion data generation
3) After tests are completed run ```allure serve allure_reports``` to see tests completion dashboard 
