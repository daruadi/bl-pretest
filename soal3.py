import os, copy, pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

class TestAndroidBasicInteractions():
    PACKAGE = 'io.appium.android.apis'
    SEARCH_ACTIVITY = '.app.SearchInvoke'
    ALERT_DIALOG_ACTIVITY = '.app.AlertDialogSamples'

    EXECUTOR = 'http://127.0.0.1:4723/wd/hub'

    ANDROID_CAPS = {
        'app': 'http://localhost:8000/login_test.apk',
        'automationName': 'UIAutomator2',
        'platformName': 'Android',
        'platformVersion': '11',
        'deviceName': 'emulator-5554',
    }

    @pytest.fixture(scope='function')
    def driver(self, request):
        calling_request = request._pyfuncitem.name

        caps = copy.copy(self.ANDROID_CAPS)
        # caps['name'] = calling_request
        # caps['appActivity'] = self.SEARCH_ACTIVITY

        driver = webdriver.Remote(
            command_executor=self.EXECUTOR,
            desired_capabilities=self.ANDROID_CAPS
        )

        def fin():
            driver.quit()

        request.addfinalizer(fin)

        driver.implicitly_wait(10)
        return driver

    def test_register(self, driver):
        regis_link = driver.find_element_by_id('com.loginmodule.learning:id/textViewLinkRegister')
        regis_link.click()

        name = driver.find_element_by_id('com.loginmodule.learning:id/textInputEditTextName')
        name.send_keys('desta')

        email = driver.find_element_by_id('com.loginmodule.learning:id/textInputEditTextEmail')
        email.send_keys('desta@gmail.com')

        password = driver.find_element_by_id('com.loginmodule.learning:id/textInputEditTextPassword')
        password.send_keys('destapass')

        confirmpassword = driver.find_element_by_id('com.loginmodule.learning:id/textInputEditTextConfirmPassword')
        confirmpassword.send_keys('destapass')


        button = driver.find_element_by_id('com.loginmodule.learning:id/appCompatButtonRegister')
        button.click()

        msg = driver.find_element_by_id('com.loginmodule.learning:id/snackbar_text')

        assert 'Registration Successful' == msg.text

    def test_login(self, driver):
        regis_link = driver.find_element_by_id('com.loginmodule.learning:id/textViewLinkRegister')
        regis_link.click()

        name = driver.find_element_by_id('com.loginmodule.learning:id/textInputEditTextName')
        name.send_keys('desta')

        email = driver.find_element_by_id('com.loginmodule.learning:id/textInputEditTextEmail')
        email.send_keys('desta@gmail.com')

        password = driver.find_element_by_id('com.loginmodule.learning:id/textInputEditTextPassword')
        password.send_keys('destapass')

        confirmpassword = driver.find_element_by_id('com.loginmodule.learning:id/textInputEditTextConfirmPassword')
        confirmpassword.send_keys('destapass')


        button = driver.find_element_by_id('com.loginmodule.learning:id/appCompatButtonRegister')
        button.click()

        driver.back()

        email = driver.find_element_by_id('com.loginmodule.learning:id/textInputEditTextEmail')
        email.send_keys('desta@gmail.com')

        password = driver.find_element_by_id('com.loginmodule.learning:id/textInputEditTextPassword')
        password.send_keys('destapass')

        button = driver.find_element_by_id('com.loginmodule.learning:id/appCompatButtonLogin')
        button.click()

        textEmail = driver.find_element_by_id('com.loginmodule.learning:id/textViewEmail')

        assert 'desta@gmail.com' == textEmail.text
