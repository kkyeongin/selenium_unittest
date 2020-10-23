from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from sitter import Sitter              # sitter 정보 class
from div import DivClassName as div    # div class name and path info
import log
import unittest


class SitterPageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        """크롬 웹 드라이버를 통해 테스트 실행"""
        cls.driver = webdriver.Chrome()
        cls.driver.get(Sitter.PAGE + Sitter.ID)

    @log.log_error(user_msg='SitterPageTest ERROR')
    def test_checkSitterInfo(self):
        driver = self.driver

        self.checkSitterInfo(driver)
        self.checkButton(driver)

    @log.log_error(user_msg='not Exists sitter page element')
    def test_checkPageElement(self):
        """시터 프로필 페이지가 구성이 제대로 이뤄졌는지 확인(정적 페이지로 구성된 요소 체크)"""
        self.assertTrue(self.exists_element(By.CLASS_NAME, div.SITTER_NAME))
        self.assertTrue(self.exists_element(By.CLASS_NAME, div.SITTER_ID))
        self.assertTrue(self.exists_element(By.CLASS_NAME, div.SITTER_ADDRESS))
        self.assertTrue(self.exists_element(By.CLASS_NAME, div.SITTER_PAYMENT))

        self.assertEquals(len(self.driver.find_elements_by_xpath("//h4[@class='" + div.SITTER_PAGE_SUBTITLE_H4 + "']")), Sitter.sub_title)
        self.assertEquals(len(self.driver.find_elements_by_xpath("//h4[@class='" + div.SITTER_PAGE_FILTER_H4 + "']")), Sitter.filter_count)

    @classmethod
    def tearDown(cls):
        """테슽트 종료"""
        cls.driver.quit()

    @log.log_error(user_msg='Not equal sitter page info and server info')
    def checkSitterInfo(self, _driver):
        """restful api를 통해서 받은 json 객체의 sitter 정보와 html 페이지의 정보와 일지하는지 확인"""
        self.assertEqual(_driver.find_element_by_class_name(div.SITTER_NAME).text, Sitter.NAME)
        self.assertTrue(Sitter.ID in _driver.find_element_by_class_name(div.SITTER_ID).text)
        self.assertEqual(_driver.find_element_by_class_name(div.SITTER_ADDRESS).text, Sitter.ADDRESS)
        self.assertTrue(Sitter.WANT_PAYMENT in _driver.find_element_by_class_name(div.SITTER_PAYMENT).text)

    @log.log_error(user_msg='No Such Element of interview button')
    def checkButton(self, _driver):
        """버튼이 제대로 노출 됬는지 확인"""
        self.assertEquals(len(_driver.find_elements_by_xpath(div.INTERVIEW_BUTTON_PATH)), 2)

    def exists_element(self, byObject: By, idOrName: str):
        """ element 존재 여부 확인 """
        try:
            self.driver.find_element(by=byObject, value=idOrName)
        except NoSuchElementException:
            return False
        return True
