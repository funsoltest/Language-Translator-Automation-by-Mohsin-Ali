"""Text translator page object."""
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from utils.logger import setup_logger
from config.config import DEFAULT_TIMEOUT

logger = setup_logger(__name__)


class TextTranslatorPage(BasePage):
    """Page object for the text translator screen."""

    # ----------------------Locators---------------------- #
    INPUT_TEXT_FIELD = (AppiumBy.XPATH, "//android.widget.EditText")
    TRANSLATE_BUTTON = (AppiumBy.XPATH, "//android.widget.Button")
    RESULT_TEXT = (AppiumBy.XPATH, "//android.widget.TextView")

    # ----------------------Actions---------------------- #
    def enter_text(self, text: str):
        """Enter text into the translation input field.
        
        Args:
            text: Text to enter for translation
            
        Raises:
            TimeoutException: If input field is not found
        """
        import time
        from config.config import ELEMENT_INTERACTION_DELAY
        
        logger.info(f"Entering text: {text}")
        self.click_element(*self.INPUT_TEXT_FIELD)
        time.sleep(ELEMENT_INTERACTION_DELAY)
        self.send_keys(*self.INPUT_TEXT_FIELD, text, clear_first=True)
        time.sleep(ELEMENT_INTERACTION_DELAY)

    def tap_translate(self):
        """Tap the translate button.
        
        Raises:
            TimeoutException: If translate button is not found
        """
        import time
        from config.config import ELEMENT_INTERACTION_DELAY
        
        logger.info("Tapping translate button...")
        self.click_element(*self.TRANSLATE_BUTTON)
        
        # Wait for click to register
        time.sleep(ELEMENT_INTERACTION_DELAY)
        
        # Wait for translation to complete (result to appear)
        logger.info("Waiting for translation to complete...")
        try:
            WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
                EC.presence_of_element_located(self.RESULT_TEXT)
            )
            logger.info("Translation completed")
            # Additional wait to ensure result is fully rendered
            time.sleep(ELEMENT_INTERACTION_DELAY)
        except TimeoutException:
            logger.warning("Translation result not found within timeout")

    def get_result(self) -> str:
        """Get the translation result text.
        
        Returns:
            Translation result text
            
        Raises:
            TimeoutException: If result element is not found
        """
        result_text = self.get_text(*self.RESULT_TEXT)
        logger.info(f"Translation result: {result_text}")
        return result_text

    def is_result_available(self) -> bool:
        """Check if translation result is available.
        
        Returns:
            True if result is available, False otherwise
        """
        return self.is_element_present(*self.RESULT_TEXT)