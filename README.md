# Test with Selenium and Requests wih pytest in Python

- [Test with Selenium and Requests wih pytest in Python](#test-with-selenium-and-requests-wih-pytest-in-python)
  - [Installation](#installation)
    - [pyenv](#pyenv)
      - [For Linux](#for-linux)
      - [For Windows](#for-windows)
  - [Pipenv](#pipenv)
  - [Webdriver](#webdriver)
- [Setup](#setup)
- [Test](#test)
  - [Run test](#run-test)

This is a sample testing project written in Python. It uses [requests](https://docs.python-requests.org/en/master) as the http client for testing the services and [selenium](https://github.com/SeleniumHQ/selenium/tree/trunk/py) for the ui. Both are using [pytest](https://docs.pytest.org/en/latest) for the test runner.

## Installation

You will need to have [Python](https://www.python.org/) and [Pipenv](https://pypi.org/project/pipenv/) installed to manage python packages and creating a virtual environment. We will use [pyenv](https://github.com/pyenv/pyenv) to manage Python.

### [pyenv](https://github.com/pyenv/pyenv)

#### For Linux

```bash
# install required linraries to build python later on first
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

# then install pyenv
curl https://pyenv.run | bash

# add this to ~/.bashrc
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"

# check pyenv is working properly
pyenv

# install a python version
pyenv install 3.9.7

# set a default python version thru pyenv
vim ~/.pyenv/version

# enter the version to use and save file
```

#### [For Windows](https://github.com/pyenv-win/pyenv-win)

git clone pyenv

```bash
git clone https://github.com/pyenv-win/pyenv-win.git "$HOME/.pyenv"
```

add these to environment variables from powershell

```powershell
[System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('PYENV_ROOT',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")

```

add user path variable

```powershell
[System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', "User"),"User")

```

```bash
# check pyenv working
pyenv

# install a version of python
pyenv install 3.9.7

# set a global python version
pyenv global 3.9.7
pyenv rehash
```

## Pipenv

To install pipenv:
```bash
py -3.9 -m pip install pipenv
```

And set pipenv to create its virtual environment within the project itself by adding these to user's `PATH`:

`PIPENV_VENV_IN_PROJECT=1`
`PIPENV_VERBOSITY=-1`

## Webdriver

The UI tests requires the use of a web driver [chromedriver](https://chromedriver.chromium.org/) to run the UI tests. Make sure the chromdriver executable is added to `PATH`

# Setup

Open the project from shell and create your virtual environment from the [Pipfile](Pipfile) on the main project folder. Run command

```bash
py -3.9 -m pipenv install
```

# Test

The tests involves logging in and providing authorisation tokens retreived from the environment variables. When running these tests from a build pipeline, add these to the pipeline environment variables.

To set this on your machine, you will need to add these environment variables with the corresponding value **OR** you can **use the two test commands provided below under the Run test section**.

```text
testuser=REPLACEWITHusername
testpassword=REPLACEWITHuserpassword
token=REPLACEWITHoauthtoken
tokensecret=REPLACEWITHoauthtokensecret
key=REPLACEWITHconsumerkey
keysecret=REPLACEWITHconsumersecret
```
## Run test

We use [pytest](https://pypi.org/project/pytest/) to run the tests. With pipenv, run the pytest command.

```bash
pipenv run python -m pytest -s --disable-warnings -v -n 2
```

For running the ui tests, use:
```bash
pipenv run python -m pytest -s --disable-warnings -v -n 2 -m ui
```

**to include the required environment variables from the command line:**
```bash
testuser=**REPLACEWITHusername** testpassword=**REPLACEWITHuserpassword** token=**REPLACEWITHoauthtoken** tokensecret=**REPLACEWITHoauthtokensecret** key=**REPLACEWITHconsumerkey** keysecret=**REPLACEWITHconsumersecret** pipenv run python -m pytest -s --disable-warnings -v -n 2 -m ui
```

For running the api tests, use:
```bash
pipenv run python -m pytest -s --disable-warnings -v -n 2 -m api
```

**to include the required environment variables from the command line:**
```bash
testuser=**REPLACEWITHusername** testpassword=**REPLACEWITHuserpassword** token=**REPLACEWITHoauthtoken** tokensecret=**REPLACEWITHoauthtokensecret** key=**REPLACEWITHconsumerkey** keysecret=**REPLACEWITHconsumersecret** pipenv run python -m pytest -s --disable-warnings -v -n 2 -m api
```
