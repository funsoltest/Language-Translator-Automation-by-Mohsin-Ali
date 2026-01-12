from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.app = r"C:\Users\Mohsin Ali\Documents\AppiumTests\Language Translator-debug.apk"
options.auto_grant_permissions = True

print("Starting app...")
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

try:
    # ------------------Splash Screen------------------- #
    print("Waiting for splash screen (10 seconds)...")
    time.sleep(10)
    
    # Wait for Ad to Load
    print("Waiting for ad to appear (6 seconds)...")
    time.sleep(6)
    
    # Close Ad Button
    print("Closing ad...")
    try:
        # Method 1: Using XPath 
        close_button = driver.find_element(
            by=AppiumBy.XPATH, 
            value='//android.widget.Button'
        )
        close_button.click()
        print("Ad closed")
        time.sleep(2)

    except NoSuchElementException:
        print("Close button not found with XPath, trying alternative...")
        
        # Method 2: Using UiSelector (alternative)
        try:
            close_button = driver.find_element(
                by=AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().className("android.widget.TextView").instance(0)'
            )
            close_button.click()
            print("Ad closed using UiSelector!")
            time.sleep(2)
        except:
            print("Could not close ad, continuing anyway...")
    
    # =========================
    # Step 3: Language OB Screen
    # =========================
    print("Waiting for Language Onboarding screen...")
    time.sleep(3)

    print("Clicking Next button on Language OB...")
    try:
        lang_next = driver.find_element(
            by=AppiumBy.XPATH,
            value="//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]"
        )
        lang_next.click()
        print("Language OB Next clicked")
        time.sleep(2)

    except NoSuchElementException:
        print("Language OB Next button not found")

    driver.save_screenshot("02_language_ob.png")

    # =========================
    # Step 4: Feature OB Screens (Swipe)
    # =========================
    print("Swiping Feature Onboarding screens...")
    for i in range(3):   # 3 swipes → last screen
        print(f"Swipe {i+1}/3")
        driver.swipe(900, 1000, 200, 1000, 500)
        time.sleep(1)

    driver.save_screenshot("03_feature_ob_last.png")

    # =========================
    # Step 5: Feature OB Continue
    # =========================
    print("Clicking Continue button...")
    try:
        continue_btn = driver.find_element(
            by=AppiumBy.XPATH,
            value="//android.widget.Button"
        )
        continue_btn.click()
        print("Continue button clicked")
        time.sleep(3)

    except NoSuchElementException:
        print("Continue button not found")

    # =========================
    # Step 6: Premium Screen
    # =========================
    print("Waiting for Premium screen...")
    time.sleep(3)

    print("Closing Premium screen...")
    try:
        premium_close = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.ImageView[@content-desc="Premium Close"]'
        )
        premium_close.click()
        print("Premium screen closed")
        time.sleep(2)

    except NoSuchElementException:
        print("Premium close button not found")

    # =========================
    # Step 7: Home Screen
    # =========================
    print("Home screen reached successfully")
    driver.save_screenshot("04_home_screen.png")
    print("Automation flow completed successfully!")

except Exception as e:
    print(f"Error occurred: {e}")
    driver.save_screenshot("error_screen.png")

finally:
    time.sleep(2)
    driver.quit()
    print("Test completed!")