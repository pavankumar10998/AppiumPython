import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestTruecallerLogin:
    @pytest.fixture(autouse=True)
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "Pixel 4",
            "platformVersion": "10.0",
            "app": "/Users/rpkumar/Downloads/truecaller.apk",
            "automationName": "UiAutomator2",
            "appium:appWaitForLaunch": False
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

        yield

        self.driver.quit()

    def test_login_to_truecaller(self):
        # Locate and click on get started button
        get_started_btn = self.driver.find_element(MobileBy.ID, "com.truecaller:id/nextButton")
        get_started_btn.click()

        # click on allow permission button
        allow_permision_btn = self.driver.find_element(MobileBy.ID,
                                                       "com.android.permissioncontroller:id/permission_allow_button")
        allow_permision_btn.click()
        allow_permision_btn.click()
        allow_permision_btn.click()
        allow_permision_btn.click()

        # Locate and click on the 'Continue with Google' button
        continue_with_google_btn = self.driver.find_element(MobileBy.ID, "com.truecaller:id/btn_google")
        continue_with_google_btn.click()

        # Enter your Google account credentials and click on the 'Next' button
        email_field = self.driver.find_element(MobileBy.ID, "identifierId")
        email_field.send_keys("email@example.com")

        next_btn = self.driver.find_element(MobileBy.ID, "identifierNext")
        next_btn.click()

        password_field = self.driver.find_element(MobileBy.NAME, "password")
        password_field.send_keys("your_password")

        next_btn = self.driver.find_element(MobileBy.ID, "passwordNext")
        next_btn.click()

        # Assert that the user is logged in successfully and landed on the main screen
        main_screen_title = self.driver.find_element(MobileBy.ID, "com.truecaller:id/toolbar_title")
        assert main_screen_title.text == "Truecaller"

        # Add more assertions or further actions as needed
