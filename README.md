# Pytest Setup Guide

This guide provides detailed instructions on how to set up `pytest` for testing in a Python project, including downloading and installing Python, setting up PyCharm, and configuring `pytest` with an HTML reporter.

## Table of Contents
- [Step 1: Install Python](#step-1-install-python)
- [Step 2: Install PyCharm](#step-2-install-pycharm)
- [Step 3: Create a New PyCharm Project](#step-3-create-a-new-pycharm-project)
- [Step 4: Download Test Code from GitHub](#step-4-download-test-code-from-github)
- [Step 5: Install Required Libraries](#step-5-install-required-libraries)
- [Step 6: Execute Tests](#step-6-execute-tests)
- [Step 7: Install and Use Pytest HTML Reporter](#step-7-install-and-use-pytest-html-reporter)
- [Conclusion](#conclusion)

## Step 1: Install Python

1. **Download Python**:
   - Visit the official Python website: [python.org](https://www.python.org/downloads/).
   - Download the latest version of Python compatible with your operating system.

2. **Install Python**:
   - Run the installer.
   - Ensure you check the box that says **"Add Python to PATH"** before clicking **"Install Now"**.

3. **Verify Python Installation**:
   - Open a command prompt (Windows) or terminal (macOS/Linux).
   - Type the following command and press Enter:
     ```bash
     python --version
     ```
   - You should see the installed version of Python.

## Step 2: Install PyCharm

1. **Download PyCharm**:
   - Go to the [JetBrains PyCharm download page](https://www.jetbrains.com/pycharm/download/).
   - Choose the Community edition (free) or Professional edition (paid) based on your needs.

2. **Install PyCharm**:
   - Run the installer and follow the installation instructions.

3. **Launch PyCharm**:
   - Open PyCharm after installation is complete.

## Step 3: Create a New PyCharm Project

1. **Create a New Project**:
   - Click on **"New Project"** on the welcome screen.
   - Choose a location for your project and ensure the **Python interpreter** is set to the version you installed earlier.

2. **Set Up a Virtual Environment** (optional but recommended):
   - Check the box for **"Create a new virtual environment"**.
   - Select the base interpreter (Python version) and click **"Create"**.

## Step 4: Download Test Code from GitHub

1. **Add Test Code and `pytest.ini`**:
   - Copy the test code files and the `pytest.ini` configuration file into your PyCharm project directory.

## Step 5: Install Required Libraries

1. **Open the Terminal in PyCharm**:
   - Go to **View > Tool Windows > Terminal**.

2. **Install Pytest**:
   - Run the following command to install `pytest`:
     ```bash
     pip install pytest
     ```

3. **Install Additional Libraries** (if needed):
   - If your tests require additional libraries, install them similarly. For example:
     ```bash
     pip install requests
     ```

## Step 6: Execute Tests

### From PyCharm

1. **Run Tests**:
   - Right-click on the test file or the test function in the editor.
   - Select **"Run 'pytest in <filename>'"** to execute the tests.

2. **View Results**:
   - The test results will appear in the Run window at the bottom of PyCharm.

### From Command Line

1. **Navigate to Your Project Directory**:
   - Open a terminal and navigate to the directory containing your test files.

2. **Run Pytest**:
   - Execute the following command:
     ```bash
     pytest
     ```
   - You can also specify a particular test file:
     ```bash
     pytest <test_file>.py
     ```

## Step 7: Install and Use Pytest HTML Reporter

1. **Install Pytest HTML Reporter**:
   - In the terminal, run the following command to install the `pytest-html` library:
     ```bash
     pip install pytest-html
     ```

2. **Configure `pytest.ini`**:
   - Open your `pytest.ini` file and add the following configuration to enable HTML reporting:
     ```ini
     [pytest]
     addopts = --html=report.html
     ```

3. **Generate HTML Report**:
   - Run your tests again using pytest:
     ```bash
     pytest
     ```
   - This will generate an HTML report named `report.html` in your project directory.

4. **View the Report**:
   - Open the `report.html` file in your web browser to view the test results in a structured format.

