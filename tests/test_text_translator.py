# from run_main import launch_app
# from pages.home_page import HomePage
# from pages.text_translator_page import TextTranslatorPage


# # ---------------------------Text Translator Test---------------------- #
# def test_text_translation():
#     driver = launch_app()

#     home = HomePage(driver)
#     home.open_text_translator()

#     text_page = TextTranslatorPage(driver)
#     text_page.enter_text("Hello")
#     text_page.tap_translate()

#     assert text_page.get_result() != ""

#     driver.quit()