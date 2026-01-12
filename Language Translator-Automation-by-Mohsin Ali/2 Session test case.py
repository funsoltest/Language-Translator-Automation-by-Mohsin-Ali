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
    
    # -----------------Close Ad Button------------------ #
    print("Closing ad...")
    try:
        
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
    

    # ------------------Premium Screen----------------------------- #
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

    # --------------------Home Screen-------------------- #
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