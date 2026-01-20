from appium import webdriver
from appium.options.android import UiAutomator2Options


# ------------------------Driver Initialization---------------------------- #
def start_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app = r"C:\Users\Mohsin Ali\Documents\Automation\LanguageTranslatorAutomation\Language Translator-debug.apk"
    options.auto_grant_permissions = True

    print("Starting app...")
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver