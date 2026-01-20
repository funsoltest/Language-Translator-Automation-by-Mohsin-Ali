from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time


# -----------------------Splash Screen + Interstitial Ad-------------------- #
def handle_splash_and_ad(driver):
    print("Waiting for splash screen...")
    time.sleep(10)

    print("Waiting for ad...")
    time.sleep(6)

    try:
        driver.find_element(AppiumBy.XPATH, "//android.widget.Button").click()
        print("Ad closed")
    except:
        print("Ad not found")


# ---------------------Language Onboarding Screen---------------------- #
def handle_language_ob(driver):
    try:
        driver.find_element(
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]"
        ).click()
        print("Language OB Next clicked")
    except:
        print("Language OB skipped")


# ---------------------Feature Onboarding (Swipe + Continue)--------------------- #
def handle_feature_ob(driver):
    for i in range(3):
        print(f"Swipe {i + 1}/3")
        driver.swipe(900, 1000, 200, 1000, 500)


# ---------------------------Premium Screen---------------------- #
def handle_premium_screen(driver):
    try:
        driver.find_element(
            AppiumBy.XPATH,
            '//android.widget.ImageView[@content-desc="Premium Close"]'
        ).click()
        print("Premium closed")
    except:
        print("Premium screen skipped")


# ---------------------------Home Screen---------------------- #
def handle_home_screen(driver):
    print("Waiting for Home screen...")
    time.sleep(3)

    try:
        driver.find_element(
            AppiumBy.XPATH,
            "//android.widget.TextView"
        )
        print("Home screen reached successfully")
    except NoSuchElementException:
        print("Home screen not detected")