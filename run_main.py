"""Main entry point for launching the app."""
from core.driver_manager import start_driver, quit_driver
from core.base_flows import (
    handle_splash_and_ad,
    handle_language_ob,
    handle_feature_ob,
    handle_premium_screen,
    handle_home_screen
)
from utils.logger import setup_logger

logger = setup_logger(__name__)


def launch_app():
    """Launch the app and handle all onboarding screens.
    
    Returns:
        WebDriver instance ready for testing
    """
    logger.info("Starting app launch sequence...")
    
    try:
        driver = start_driver()
        handle_splash_and_ad(driver)
        handle_language_ob(driver)
        handle_feature_ob(driver)
        handle_premium_screen(driver)
        handle_home_screen(driver)
        
        logger.info("App launch sequence completed successfully")
        return driver
    except Exception as e:
        logger.error(f"Error during app launch: {str(e)}")
        raise


if __name__ == "__main__":
    driver = None
    try:
        driver = launch_app()
        logger.info("App launched successfully. Keeping it open for 5 seconds...")
        import time
        time.sleep(5)
    except Exception as e:
        logger.error(f"Failed to launch app: {str(e)}")
    finally:
        if driver:
            quit_driver(driver)