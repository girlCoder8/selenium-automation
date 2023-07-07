# Automation Test - BDD + Python + Selenium

This is a demonstration for automatically website UI functional test as BDD + Page Objects design pattern demonstration.

# Features

  - Testing Script by Python + Selenium + WebDriver (Support Chrome, Firefox)

### Behavior Driven Development
  - BDD by Cucumber (behave lib.)

### 3rd Party Testing Tool
  - Browserstack - Perform testing on cloud
  - Bitbucket Pipeline for CI
  - Pretty Testing Reports by allure (local service)

# Installation

Two ways to trigger the testing package.

### Pre-Conditions
Before the installation, you need to install required packages.
if you want to do it manually by yourself, 
the following is the package list for your reference:

if not, please ignore this part.

- python 2.7.11
- pip (version: 18.1)
- behave (it's a cucumber lib.)
- selenium
- allure-behave (or you can install the other version as 'brew install allure')

### Run on Local Machine

1. Clone this project to local first.

```sh
git clone git@bitbucket.org:girlCoder8/selenium-automation.git
```

2. Launch terminal and go to the parent path of this project.
3. Run the following commands:
Makefile

```sh
make install
```

4. Trigger the test
```sh
make test
```

### Run on Cloud

1. navigate to [Home Page](https://www.yahoo.com)
2. Click the lastest build as succeed.
3. Click "Rerun" button on upper middle of the page.
4. Once the build has been completed, you can see the testing result in build logs.

If you want to see the details in each step, you can login into "Browserstack" website
[BrowserStack](https://www.browserstack.com/automate)

- TEST Account: test-email@mail.com
- TEST Password: testPW


As long as you logged in BrowserStack, you can see any details as each test step by dashboard.
Dashboard Link: [https://automate.browserstack.com/dashboard](https://automate.browserstack.com/dashboard)

[!
