from selenium import webdriver
from sitter import Sitter              # sitter 정보 class
from div import DivClassName as div    # div class name and path info
from parent import Parent
import log, time
import unittest


class SitterInterviewTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        """크롬 웹 드라이버를 통해 테스트 실행"""
        cls.driver = webdriver.Chrome()
        cls.driver.get(Sitter.PAGE + Sitter.ID)

    @log.log_error(user_msg='interview apply error')
    def test_checkInterviewButton(self):
        driver = self.driver

        try:
            driver.find_element_by_xpath(div.SITTER_PAGE_INTERVIEW_BUTTON_XPATH).click()
            time.sleep(1)

            self.parent_login(driver)

            time.sleep(1)
            driver.get(Sitter.PAGE + Sitter.ID)

            driver.find_element_by_xpath(div.SITTER_PAGE_INTERVIEW_BUTTON_XPATH).click()
            time.sleep(1)
            driver.find_elements_by_xpath(div.SITTER_PAGE_INTERVIEW_APPLY_BUTTON_XPATH)[0].click()

            if "신청 완료" in driver.title:
                driver.get(Sitter.MYJOB)
                self.assertTrue(Sitter.NAME in self.find_element_by_class_name(div.PARENT_APPLY_SITTER_CLASS_NAME).text)
            else:
                pass
        except Exception:
            raise Exception


    @classmethod
    def tearDown(cls):
        """테스트 종료"""
        cls.driver.implicitly_wait(10)
        cls.driver.quit()

    # @log.log_error(user_msg='login error')
    def parent_login(self, _driver):
        """ 로그인 코드 """
        _driver.find_element_by_name(div.LOGIN_ID).send_keys(Parent.ID)
        _driver.find_element_by_name(div.LOGIN_PW).send_keys(Parent.PW)

        _driver.find_element_by_class_name(div.LOGIN_BUTTON).click()

