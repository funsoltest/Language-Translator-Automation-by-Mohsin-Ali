from core.driver_manager import start_driver

from core.base_flows import (
    handle_splash_and_ad,
    handle_language_ob,
    handle_feature_ob,
    handle_premium_screen,
    handle_home_screen
)

def launch_app():
    driver = start_driver()
    handle_splash_and_ad(driver)
    handle_language_ob(driver)
    handle_feature_ob(driver)
    handle_premium_screen(driver)
    handle_home_screen(driver)
    return driver


if __name__ == "__main__":
    driver = launch_app()
    driver.quit()