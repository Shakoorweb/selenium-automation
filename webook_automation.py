
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options
options = Options()
options.add_argument("--disable-search-engine-choice-screen")
options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})

service = ChromeService(executable_path=ChromeDriverManager().install())


class WebookAutomation:

    def __init__(self):
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get("https://webook.com/en")
        self.driver.maximize_window()

    def registration_flow(self, first_name: str, last_name: str, email: str, password: str, mobile: str) -> bool:
        print("yes")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Log In / Sign Up"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='email-login']/div[5]/button"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "first_name"))
        ).send_keys(first_name)

        self.driver.find_element(By.ID, "last_name").send_keys(last_name)
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "confirm_email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.NAME, "mobile").send_keys(mobile)
        self.driver.find_element(By.NAME, "agreeTerms").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "button[form='signup-form-info']")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        user_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/header/nav/ul/li[3]/button/div'))
        ).text

        expected_user_name = f"{first_name[0]}{last_name[0]}"

        return user_name == expected_user_name

    def search(self, search_title: str) -> bool:
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="search"]'))
        ).send_keys(search_title, Keys.ENTER)

        value = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/section[1]/h1'))
        ).text

        return value == f'Search results for "{search_title}"'

    def filter_search(self, filter_name: str) -> bool:
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="search"]'))
        ).click()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  f"//p[text()='Explore things to book']/following-sibling::ul[1]/li/a[@href='/en/explore?type={filter_name.lower()}']"))
            )
            return True
        except TimeoutException:
            return False
