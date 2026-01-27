"""Wait utilities for element interactions."""
from typing import Callable, Optional
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy

from utils.logger import setup_logger
from config.config import DEFAULT_TIMEOUT, SHORT_TIMEOUT, LONG_TIMEOUT

logger = setup_logger(__name__)


def wait_for_element(
    driver,
    by,
    value: str,
    timeout: int = DEFAULT_TIMEOUT,
    condition: Callable = EC.presence_of_element_located
) -> bool:
    """Wait for element with custom condition.
    
    Args:
        driver: WebDriver instance
        by: Locator strategy
        value: Locator value
        timeout: Wait timeout
        condition: Expected condition function
        
    Returns:
        True if element found, False otherwise
    """
    try:
        WebDriverWait(driver, timeout).until(condition((by, value)))
        logger.debug(f"Element found: {by}={value}")
        return True
    except TimeoutException:
        logger.warning(f"Element not found within {timeout}s: {by}={value}")
        return False


def wait_for_element_clickable(driver, by, value: str, timeout: int = DEFAULT_TIMEOUT) -> bool:
    """Wait for element to be clickable.
    
    Args:
        driver: WebDriver instance
        by: Locator strategy
        value: Locator value
        timeout: Wait timeout
        
    Returns:
        True if element is clickable, False otherwise
    """
    return wait_for_element(driver, by, value, timeout, EC.element_to_be_clickable)


def wait_for_element_visible(driver, by, value: str, timeout: int = DEFAULT_TIMEOUT) -> bool:
    """Wait for element to be visible.
    
    Args:
        driver: WebDriver instance
        by: Locator strategy
        value: Locator value
        timeout: Wait timeout
        
    Returns:
        True if element is visible, False otherwise
    """
    return wait_for_element(driver, by, value, timeout, EC.visibility_of_element_located)
