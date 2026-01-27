"""Test cases for text translator functionality."""
import pytest

from run_main import launch_app
from pages.home_page import HomePage
from pages.text_translator_page import TextTranslatorPage
from core.driver_manager import quit_driver
from utils.logger import setup_logger

logger = setup_logger(__name__)


@pytest.fixture(scope="function")
def driver():
    """Fixture to provide driver instance for each test.
    
    Yields:
        WebDriver instance
    """
    driver = None
    try:
        driver = launch_app()
        yield driver
    finally:
        if driver:
            quit_driver(driver)


@pytest.fixture(scope="function")
def home_page(driver):
    """Fixture to provide HomePage instance.
    
    Args:
        driver: WebDriver instance from driver fixture
        
    Returns:
        HomePage instance
    """
    return HomePage(driver)


# ---------------------------Text Translator Test---------------------- #
def test_text_translation(driver, home_page):
    """Test text translation functionality.
    
    Args:
        driver: WebDriver instance
        home_page: HomePage instance
    """
    logger.info("Starting text translation test...")
    
    # Navigate to text translator
    home_page.open_text_translator()
    
    # Enter text and translate
    text_page = TextTranslatorPage(driver)
    test_text = "Hello"
    text_page.enter_text(test_text)
    text_page.tap_translate()
    
    # Verify result
    result = text_page.get_result()
    assert result != "", "Translation result should not be empty"
    logger.info(f"Translation successful: '{test_text}' -> '{result}'")


def test_text_translation_urdu(driver, home_page):
    """Test text translation with Urdu text.
    
    Args:
        driver: WebDriver instance
        home_page: HomePage instance
    """
    logger.info("Starting Urdu text translation test...")
    
    # Navigate to text translator
    home_page.open_text_translator()
    
    # Enter text and translate
    text_page = TextTranslatorPage(driver)
    test_text = "Mara Nam Mohsin hai"
    text_page.enter_text(test_text)
    text_page.tap_translate()
    
    # Verify result is available
    assert text_page.is_result_available(), "Translation result should be available"
    result = text_page.get_result()
    assert result != "", "Translation result should not be empty"
    logger.info(f"Translation successful: '{test_text}' -> '{result}'")