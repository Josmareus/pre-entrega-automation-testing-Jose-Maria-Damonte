from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def is_element_present(driver, by, value, timeout=10):
    """
    Verifica si un elemento está presente en la página.
    """
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return True
    except TimeoutException:
        return False

def perform_login(driver, username, password):
    """
    Login en el sitio SauceDemo.
    """
    from selenium.webdriver.common.by import By
    
    driver.get("https://www.saucedemo.com/")
    
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    
    username_input.send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    
    driver.find_element(By.ID, "login-button").click()
    
    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )
