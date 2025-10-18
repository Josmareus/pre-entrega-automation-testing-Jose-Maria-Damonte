import pytest
import os
from datetime import datetime
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def pytest_configure(config):
    """
    Configuración que se ejecuta al iniciar pytest.
    Crea la carpeta para capturas de pantalla si no existe.
    """
    if not os.path.exists('capturas'):
        os.makedirs('capturas')
        print("Carpeta 'capturas' creado.")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de pytest que captura screenshots cuando un test falla.
    """
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"failure_{item.name}_{timestamp}.png"
            driver.save_screenshot(f"capturas/{screenshot_name}")
            print(f"\nCaptura de pantalla guardada: {screenshot_name}")