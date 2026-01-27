"""Base flows for handling app initialization and onboarding screens."""
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from pages.home_page import HomePage
from pages.text_translator_page import TextTranslatorPage
from utils.logger import setup_logger
from utils.wait_utils import wait_for_element_clickable
from config.config import (
    DEFAULT_TIMEOUT, 
    SHORT_TIMEOUT,
    SPLASH_SCREEN_MIN_WAIT,
    SCREEN_TRANSITION_DELAY,
    ELEMENT_INTERACTION_DELAY
)

logger = setup_logger(__name__)


# -----------------------Splash Screen + Interstitial Ad-------------------- #
def handle_splash_and_ad(driver):
    """Handle splash screen and interstitial ad.
    
    Args:
        driver: WebDriver instance
    """
    logger.info(f"Waiting for splash screen (minimum {SPLASH_SCREEN_MIN_WAIT} seconds)...")
    
    # Wait for app to initialize - ensure current_activity is available
    start_time = time.time()
    try:
        WebDriverWait(driver, 15).until(
            lambda d: d.current_activity is not None
        )
        elapsed = time.time() - start_time
        logger.info(f"App activity detected after {elapsed:.2f} seconds")
    except TimeoutException:
        logger.warning("Activity not detected, but continuing...")
    
    # Ensure minimum wait time for splash screen
    elapsed = time.time() - start_time
    if elapsed < SPLASH_SCREEN_MIN_WAIT:
        remaining_wait = SPLASH_SCREEN_MIN_WAIT - elapsed
        logger.info(f"Waiting additional {remaining_wait:.2f} seconds for splash screen...")
        time.sleep(remaining_wait)
    
    logger.info("Splash screen wait completed")

    # Wait a bit more for UI to stabilize
    logger.info(f"Waiting {SCREEN_TRANSITION_DELAY} seconds for UI to stabilize...")
    time.sleep(SCREEN_TRANSITION_DELAY)

    logger.info("Checking for interstitial ad...")
    # Wait for ad to appear if it will (give it more time)
    try:
        # Try to find close button with multiple strategies
        close_button_xpath = (AppiumBy.XPATH, '//android.widget.Button')
        close_button_uiautomator = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.TextView").instance(0)'
        )
        
        # Wait up to 10 seconds for ad to appear
        if wait_for_element_clickable(driver, *close_button_xpath, timeout=10):
            logger.info("Closing ad using XPath button...")
            driver.find_element(*close_button_xpath).click()
            logger.info("Ad closed successfully")
            time.sleep(ELEMENT_INTERACTION_DELAY)
        elif wait_for_element_clickable(driver, *close_button_uiautomator, timeout=5):
            logger.info("Closing ad using UiSelector...")
            driver.find_element(*close_button_uiautomator).click()
            logger.info("Ad closed successfully")
            time.sleep(ELEMENT_INTERACTION_DELAY)
        else:
            logger.info("No ad detected, continuing...")
    except Exception as e:
        logger.warning(f"Could not close ad: {str(e)}, continuing anyway...")
    
    # Additional wait after ad handling
    time.sleep(SCREEN_TRANSITION_DELAY)


# ---------------------Language Onboarding Screen---------------------- #
def handle_language_ob(driver):
    """Handle language onboarding screen.
    
    Args:
        driver: WebDriver instance
    """
    logger.info("Waiting for Language Onboarding screen...")
    
    # Wait for screen to fully load
    time.sleep(SCREEN_TRANSITION_DELAY)
    
    lang_next_xpath = (
        AppiumBy.XPATH,
        "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]"
    )
    
    try:
        # Wait longer for the button to appear
        if wait_for_element_clickable(driver, *lang_next_xpath, timeout=SHORT_TIMEOUT):
            logger.info("Clicking Next button on Language OB...")
            driver.find_element(*lang_next_xpath).click()
            logger.info("Language OB Next clicked")
            
            # Wait for click to register
            time.sleep(ELEMENT_INTERACTION_DELAY)
            
            # Wait for screen transition
            logger.info("Waiting for screen transition...")
            time.sleep(SCREEN_TRANSITION_DELAY)
            
            # Verify transition completed
            WebDriverWait(driver, SHORT_TIMEOUT).until(
                lambda d: d.current_activity is not None
            )
        else:
            logger.warning("Language OB Next button not found, may have already passed")
    except Exception as e:
        logger.warning(f"Error handling language OB: {str(e)}")

    # Take screenshot for debugging
    try:
        from pages.base_page import BasePage
        base_page = BasePage(driver)
        base_page.take_screenshot("02_language_ob.png")
    except Exception as e:
        logger.warning(f"Could not take screenshot: {str(e)}")


# ---------------------Feature Onboarding (Swipe + Continue)--------------------- #
def handle_feature_ob(driver):
    """Handle feature onboarding screens with swipes.
    
    Args:
        driver: WebDriver instance
    """
    logger.info("Waiting for Feature Onboarding screen...")
    time.sleep(SCREEN_TRANSITION_DELAY)
    
    logger.info("Swiping through Feature Onboarding screens...")
    
    # Get screen dimensions for better swipe coordinates
    window_size = driver.get_window_size()
    start_x = int(window_size['width'] * 0.9)
    end_x = int(window_size['width'] * 0.2)
    y = int(window_size['height'] * 0.5)
    
    for i in range(3):
        logger.info(f"Swipe {i + 1}/3")
        driver.swipe(start_x, y, end_x, y, 800)  # Increased duration for smoother swipe
        
        # Wait for swipe animation to complete
        logger.info(f"Waiting {SCREEN_TRANSITION_DELAY} seconds for swipe animation...")
        time.sleep(SCREEN_TRANSITION_DELAY)

    # Take screenshot
    try:
        from pages.base_page import BasePage
        base_page = BasePage(driver)
        base_page.take_screenshot("03_feature_ob_last.png")
    except Exception as e:
        logger.warning(f"Could not take screenshot: {str(e)}")

    logger.info("Clicking Continue button...")
    continue_btn_xpath = (AppiumBy.XPATH, "//android.widget.Button")
    
    try:
        if wait_for_element_clickable(driver, *continue_btn_xpath, timeout=SHORT_TIMEOUT):
            driver.find_element(*continue_btn_xpath).click()
            logger.info("Continue button clicked")
            
            # Wait for click to register
            time.sleep(ELEMENT_INTERACTION_DELAY)
            
            # Wait for screen transition
            logger.info("Waiting for screen transition...")
            time.sleep(SCREEN_TRANSITION_DELAY)
            
            # Verify transition completed
            WebDriverWait(driver, SHORT_TIMEOUT).until(
                lambda d: d.current_activity is not None
            )
        else:
            logger.warning("Continue button not found")
    except Exception as e:
        logger.warning(f"Error clicking continue button: {str(e)}")


# ---------------------------Premium Screen---------------------- #
def handle_premium_screen(driver):
    """Handle premium screen popup.
    
    Args:
        driver: WebDriver instance
    """
    logger.info("Checking for Premium screen...")
    time.sleep(SCREEN_TRANSITION_DELAY)
    
    premium_close_xpath = (
        AppiumBy.XPATH,
        '//android.widget.ImageView[@content-desc="Premium Close"]'
    )
    
    try:
        if wait_for_element_clickable(driver, *premium_close_xpath, timeout=SHORT_TIMEOUT):
            logger.info("Closing Premium screen...")
            driver.find_element(*premium_close_xpath).click()
            logger.info("Premium screen closed")
            
            # Wait for click to register
            time.sleep(ELEMENT_INTERACTION_DELAY)
            
            # Wait for screen transition
            logger.info("Waiting for screen transition...")
            time.sleep(SCREEN_TRANSITION_DELAY)
            
            # Verify transition completed
            WebDriverWait(driver, SHORT_TIMEOUT).until(
                lambda d: d.current_activity is not None
            )
        else:
            logger.info("Premium screen not found, may have already passed")
    except Exception as e:
        logger.warning(f"Error handling premium screen: {str(e)}")


# ---------------------------Home Screen---------------------- #
def handle_home_screen(driver):
    """Handle home screen and verify it's loaded.
    
    Args:
        driver: WebDriver instance
    """
    logger.info("Waiting for Home screen...")
    
    # Wait for screen transition to complete
    time.sleep(SCREEN_TRANSITION_DELAY)
    
    # Wait for home screen to be ready
    try:
        home_page = HomePage(driver)
        logger.info("Waiting for home screen elements to be ready...")
        home_screen_loaded = wait_for_element_clickable(
            driver,
            *HomePage.TEXT_TRANSLATOR_BTN,
            timeout=DEFAULT_TIMEOUT
        )
        
        if home_screen_loaded:
            logger.info("Home screen loaded successfully")
            # Additional wait to ensure UI is fully rendered
            time.sleep(ELEMENT_INTERACTION_DELAY)
        else:
            logger.warning("Home screen elements not found")
    except Exception as e:
        logger.warning(f"Error verifying home screen: {str(e)}")