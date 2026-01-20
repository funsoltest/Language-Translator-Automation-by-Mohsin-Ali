from appium.webdriver.common.appiumby import AppiumBy


# ---------------------------Home Screen---------------------- #
class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # ---------------------------Locators---------------------- #
    text_translator_btn = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[4]"
    camera_translator_btn = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]"
    voice_translator_btn = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]"
    history_btn = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[4]"

    # ---------------------------Actions---------------------- #
    def open_text_translator(self):
        self.driver.find_element(AppiumBy.XPATH, self.text_translator_btn).click()

    def open_camera_translator(self):
        self.driver.find_element(AppiumBy.XPATH, self.camera_translator_btn).click()

    def open_voice_translator(self):
        self.driver.find_element(AppiumBy.XPATH, self.voice_translator_btn).click()

    def open_history(self):
        self.driver.find_element(AppiumBy.XPATH, self.history_btn).click()