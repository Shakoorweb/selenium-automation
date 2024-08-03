## README.md

### Webook Automation

This project automates basic interactions with webook.com using Selenium and Pytest. It provides functionalities for creating an account, searching by text, and searching by filter.

### Installation

1. **Prerequisites**: Ensure you have Python 3.x installed on your system.
2. **Install Dependencies**: Open a terminal in your project directory and run the following command:

```bash
pip install -r requirements.txt
```

This will install all the necessary libraries like Selenium, Pytest, and webdriver-manager.

### Project Structure

The project consists of three main files:

* `webook_automation.py`: Contains the `WebookAutomation` class responsible for interacting with the webook.com website.
* `test_webook.py`: Implements Pytest fixtures and tests for the functionalities offered by `webook_automation.py`.
* `requirements.txt`: Lists all the required Python libraries for this project.


### Usage

#### Running Tests
Navigate to your project directory in the terminal and run the following command:

```bash
pytest
```

This will execute all the tests defined in `test_webook.py`. A successful run will indicate that the automation works as expected.

#### Manual Execution (Optional)
- Open `webook_automation.py` and comment out the `@pytest.fixture` decorator in the `TestWebook` class.
- Create an instance of `WebookAutomation` and call the desired methods (e.g., `registration_flow`, `search`, `filter_search`) with necessary arguments.

**Note**: Running tests directly modifies the browser state, so it's recommended to use the Pytest fixture approach for isolated test execution.

### Documentation

**`webook_automation.py` Class**
* `__init__(self)`: Initializes a new Chrome webdriver instance and navigates to webook.com
* `registration_flow(self, first_name, last_name, email, password, mobile)`: Attempts to register a new account with provided credentials. Returns `True` if successful, `False` otherwise.
* `search(self, search_title)`: Searches for the provided `search_title` on the website. Returns `True` if the search result title matches the expected format, `False` otherwise.
* `filter_search(self, filter_name)`: Attempts to filter by the provided `filter_name`. Returns `True` if the filter option is found, `False` otherwise.

**`test_webook.py` Tests**
* Defines Pytest fixtures and tests for each implemented functionality in `webook_automation.py`.
