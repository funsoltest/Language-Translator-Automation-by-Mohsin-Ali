"""Base page class with common utilities for all page objects."""
from typing import Optional
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy

from utils.logger import setup_logger
from config.config import DEFAULT_TIMEOUT, SHORT_TIMEOUT, LONG_TIMEOUT

logger = setup_logger(__name__)


class BasePage:
    """Base class for all page objects."""
    
    def __init__(self, driver):
        """Initialize base page with driver.
        
        Args:
            driver: Appium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)
        self.short_wait = WebDriverWait(driver, SHORT_TIMEOUT)
        self.long_wait = WebDriverWait(driver, LONG_TIMEOUT)
    
    def find_element(self, by, value: str, timeout: Optional[int] = None):
        """Find element with explicit wait.
        
        Args:
            by: Locator strategy (AppiumBy.XPATH, etc.)
            value: Locator value
            timeout: Optional timeout override
            
        Returns:
            WebElement if found
            
        Raises:
            TimeoutException: If element not found within timeout
        """
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            element = wait.until(EC.presence_of_element_located((by, value)))
            logger.debug(f"Element found: {by}={value}")
            return element
        except TimeoutException:
            logger.error(f"Element not found: {by}={value}")
            raise
    
    def find_elements(self, by, value: str, timeout: Optional[int] = None):
        """Find multiple elements with explicit wait.
        
        Args:
            by: Locator strategy
            value: Locator value
            timeout: Optional timeout override
            
        Returns:
            List of WebElements
        """
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            elements = wait.until(EC.presence_of_all_elements_located((by, value)))
            logger.debug(f"Found {len(elements)} elements: {by}={value}")
            return elements
        except TimeoutException:
            logger.warning(f"No elements found: {by}={value}")
            return []
    
    def click_element(self, by, value: str, timeout: Optional[int] = None):
        """Click element with explicit wait for clickability.
        
        Args:
            by: Locator strategy
            value: Locator value
            timeout: Optional timeout override
        """
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            element = wait.until(EC.element_to_be_clickable((by, value)))
            element.click()
            logger.info(f"Clicked element: {by}={value}")
        except TimeoutException:
            logger.error(f"Element not clickable: {by}={value}")
            raise
    
    def send_keys(self, by, value: str, text: str, timeout: Optional[int] = None, clear_first: bool = True):
        """Send keys to element with explicit wait.
        
        Args:
            by: Locator strategy
            value: Locator value
            text: Text to send
            timeout: Optional timeout override
            clear_first: Whether to clear the field before typing
        """
        element = self.find_element(by, value, timeout)
        if clear_first:
            element.clear()
        element.send_keys(text)
        logger.info(f"Sent keys to element: {by}={value}")
    
    def get_text(self, by, value: str, timeout: Optional[int] = None) -> str:
        """Get text from element.
        
        Args:
            by: Locator strategy
            value: Locator value
            timeout: Optional timeout override
            
        Returns:
            Element text
        """
        element = self.find_element(by, value, timeout)
        text = element.text
        logger.debug(f"Got text from element: {by}={value}, text={text}")
        return text
    
    def is_element_present(self, by, value: str, timeout: Optional[int] = None) -> bool:
        """Check if element is present without raising exception.
        
        Args:
            by: Locator strategy
            value: Locator value
            timeout: Optional timeout override
            
        Returns:
            True if element is present, False otherwise
        """
        try:
            self.find_element(by, value, timeout)
            return True
        except (TimeoutException, NoSuchElementException):
            return False
    
    def wait_for_element_visible(self, by, value: str, timeout: Optional[int] = None):
        """Wait for element to be visible.
        
        Args:
            by: Locator strategy
            value: Locator value
            timeout: Optional timeout override
        """
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.visibility_of_element_located((by, value)))
            logger.debug(f"Element visible: {by}={value}")
        except TimeoutException:
            logger.error(f"Element not visible: {by}={value}")
            raise
    
    def take_screenshot(self, filename: str):
        """Take screenshot and save to screenshots directory.
        
        Args:
            filename: Name of the screenshot file
        """
        from config.config import SCREENSHOT_DIR
        filepath = SCREENSHOT_DIR / filename
        self.driver.save_screenshot(str(filepath))
        logger.info(f"Screenshot saved: {filepath}")
