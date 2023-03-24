# 🎭Automate web browsers with [Python](https://www.python.org/) and [Playwright](https://playwright.dev/python/).
|               | Linux | Windows | macOS |
|---------------|-------|---------|-------|
| **Chromium**  | ✅     | ✅       | ✅     |
| **WebKit**    | ✅     | ✅       | ✅     |
| **Firefox**   | ✅     | ✅       | ✅     |

## ❓What is Playwright

>Playwright was created specifically to accommodate the needs of end-to-end testing. Playwright supports all modern rendering engines including Chromium, WebKit, and Firefox. Test on Windows, Linux, and macOS, locally or on CI, headless or headed with native mobile emulation.


## 📖 Documentation:

https://playwright.dev/python/docs/intro

## ❕Requirements:
* To run this testing framework, you will need:

  * [Python](https://www.python.org/) 3.7 or higher
  * [Docker](https://www.docker.com/) (if you want to run the tests in a container)
  * [Docker-compose](https://docs.docker.com/compose/) (if you want to run the tests in a container)
  * [Allure](https://github.com/allure-framework) (if you want to generate test reports)

## 🔧 Installation: 

- Install the [Pytest plugin](https://pypi.org/project/pytest-playwright/):
```sh
pip install pytest-playwright
```
- Install the required browsers:
```sh
playwright install
```


## 🚀 Running:
Follow these steps to install the necessary packages:
1. Clone the repository:
```sh
git clone https://github.com/ZhikharevAl/python-playwright-demo-project.git
```

2. Create and activate a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate
```
3. To install dependencies from the requirements.txt file, run the following command:
```sh
pip install -r requirements.txt
```
4. To run the example test, use the following command:
```sh
pytest -s --headed --slowmo 800 -k test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page
```
## 🐳 [Docker](https://www.docker.com/):
>Docker is a platform for developing, delivering, and running applications in containers. In the context of testing, Docker can be used to run tests in isolated containers to ensure environment consistency and avoid conflicts between dependencies. In this example, if you want to run tests in a Docker container, you need to install Docker and Docker-compose. Then, to run tests in a container, use the following command:
```sh
docker build -t <Container name> .
docker run -it <Container name>
docker-compose up
```
## 📈 [Allure Framework](https://github.com/allure-framework):
>Allure is a framework and report generator that can be used to create beautiful and informative reports on test results. In this example, Allure is used to generate reports on test execution results. If you want to generate reports, you need to install Allure and run tests with the --alluredir parameter, as shown below:
```sh
pytest --clean-alluredir
```
>After running tests, you can generate Allure reports using the command:

```sh
allure serve allure-results
```
## Testing report using the [Pandas library](https://github.com/pandas-dev/pandas):
```sh
pip install pandas
```
1. Load the test data into a Pandas DataFrame.
2. Write test functions that validate the expected behavior of the code being tested.
3. Run the test functions on the test data, and store the results in a new DataFrame.
4. Generate a summary of the test results using the Pandas library.
### Here's some example code that demonstrates how to do this:
```sh
import pandas as pd

# Load the test data into a DataFrame
test_data = pd.read_csv('test_data.csv')

# Define a test function
def test_function(input_data, expected_output):
    output = my_function(input_data)
    assert output == expected_output, f"Expected {expected_output}, but got {output}."

# Run the test function on the test data
test_results = []
for i, row in test_data.iterrows():
    input_data = row['input_data']
    expected_output = row['expected_output']
    try:
        test_function(input_data, expected_output)
        test_results.append('Pass')
    except AssertionError as e:
        test_results.append('Fail')

# Store the test results in a new DataFrame
test_data['test_result'] = test_results

# Generate a summary of the test results
summary = test_data.groupby('test_result').size()
print(summary)
```
>In this example, we load the test data into a Pandas DataFrame, define a test function, run the test function on the test data, store the test results in a new DataFrame, and generate a summary of the test results using the groupby() method. The resulting summary shows the number of tests that passed and the number of tests that failed.
# ![test report as an .xml](C:/Users/1/AquaProjects/AutomationToolsQA/test_report/2023-03-23_22-24-10.png)
## 📝 License:
This project is licensed under the MIT License - see the [LICENSE](https://ru.wikipedia.org/wiki/Лицензия_MIT) file for details.
## ![Jokes Card](https://readme-jokes.vercel.app/api)