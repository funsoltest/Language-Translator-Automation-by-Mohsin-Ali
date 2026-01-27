"""Home page object for the language translator app."""
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage
from utils.logger import setup_logger

logger = setup_logger(__name__)


class HomePage(BasePage):
    """Page object for the home screen."""

    # ---------------------------Locators---------------------- #
    TEXT_TRANSLATOR_BTN = (
        AppiumBy.XPATH,
        "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[4]"
    )
    CAMERA_TRANSLATOR_BTN = (
        AppiumBy.XPATH,
        "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]"
    )
    VOICE_TRANSLATOR_BTN = (
        AppiumBy.XPATH,
        "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]"
    )
    HISTORY_BTN = (
        AppiumBy.XPATH,
        "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[4]"
    )

    # ---------------------------Actions---------------------- #
    def open_text_translator(self):
        """Open the text translator screen.
        
        Raises:
            TimeoutException: If text translator button is not found
        """
        logger.info("Navigating to text translator screen...")
        self.click_element(*self.TEXT_TRANSLATOR_BTN)
        
        # Wait for screen transition
        import time
        from config.config import SCREEN_TRANSITION_DELAY
        logger.info(f"Waiting {SCREEN_TRANSITION_DELAY} seconds for screen transition...")
        time.sleep(SCREEN_TRANSITION_DELAY)

    def open_camera_translator(self):
        """Open the camera translator screen.
        
        Raises:
            TimeoutException: If camera translator button is not found
        """
        logger.info("Navigating to camera translator screen...")
        self.click_element(*self.CAMERA_TRANSLATOR_BTN)

    def open_voice_translator(self):
        """Open the voice translator screen.
        
        Raises:
            TimeoutException: If voice translator button is not found
        """
        logger.info("Navigating to voice translator screen...")
        self.click_element(*self.VOICE_TRANSLATOR_BTN)

    def open_history(self):
        """Open the history screen.
        
        Raises:
            TimeoutException: If history button is not found
        """
        logger.info("Navigating to history screen...")
        self.click_element(*self.HISTORY_BTN)