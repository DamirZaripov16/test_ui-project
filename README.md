[![Build Status](https://app.travis-ci.com/DamirZaripov16/test_ui-project.svg?branch=master)](https://app.travis-ci.com/DamirZaripov16/test_ui-project)
# Autotests for ["Qamoodle"](https://qacoursemoodle.innopolis.university) app
## Navigation
***
####1. About
####2. Installation
####3. Instruments
####4. Checks
####5. Allure reports
## About
***
In this project the autotests check main "Qamoodle" course-making site functionality.<br>
I have chosen _Page Object model_ as a code design pattern to ensure further comfort editing and extension.
## Installation
***
1. Define a directory on a local machine
2. Clone the [project](https://github.com/DamirZaripov16/test_ui-project) <br>
   ```git clone https://github.com/DamirZaripov16/test_ui-project```
3. Open the project
4. Install all the requirements within **requirements.txt** <br>
pip install -r /path/to/requirements.txt
## Instruments
***
### _**Pytest**_
* The Easiest and yet the best test-writing tool in Python
* Multiple tests execution in parallel to reduce general execution time
* Unique way to detect tests in your project without additional imports etc.<br>
### _**Selenium**_
* Supports various commonly used Browsers
* Supports parallel test execution which perfectly combines with _**Pytest**_
### _**Logger**_
* Helps to track what exactly happening during test execution with minimum effort
* Easy to implement
### _**TravisCI**_
* "The final gate" to ensure the success of your recent build<br>
* Automated integration possibility with your linters, validators etc.<br>
### _**Allure reports (see ["Allure reports"](https://github.com/DamirZaripov16/test_ui-project#allure-reports) section for more)**_
* Detailed tests execution reports
* User-friendly dashboard to help to keep in touch with tests state<br>
* Gives a negative feedback by creating a screenshot<br>
## Checks
***
### **_Authorization form check_**
**Positive tests:**
* Authorization with valid login and valid password<br>

**Negative tests:**
* Empty login
* Empty password<br><br>

**Initial file and detailed docstring-test cases**: tests/auth/test_auth.py
### _**Course creation check**_
**Positive tests:**
* Course creation/deletion<br>

**Negative tests:**
* Unavailable course creation without fullname of the course
* Unavailable course creation without shortname of the course<br><br>

**Initial file and detailed docstring-test cases**: tests/auth/test_auth.py
### Personal data update check
**Positive tests:**
* Filling all the fields with valid data<br>

**Required fields negative tests:**
* Required fields consequent filling with invalid data<br><br>

**Initial file and detailed docstring-test cases**: \tests\personal_data\test_personal_data.py
### Signing up check
**Positive tests:**
* Filling all the fields with valid data and eventual registration of a new user<br>

**Required fields negative tests:**
* Required fields consequent filling with invalid data and unavailable registration of a new user<br>

**Initial file and detailed docstring-test cases**: tests/sign_up/test_sign_up.py
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
