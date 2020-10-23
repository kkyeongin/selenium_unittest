import unittest
import HtmlTestRunner
from seleniumSitterPageTest import SitterPageTest
from seleniumSitterInterviewTest import SitterInterviewTest

# test class 정의
sitter_page = unittest.TestLoader().loadTestsFromTestCase(SitterPageTest)
sitter_Interview = unittest.TestLoader().loadTestsFromTestCase(SitterInterviewTest)

# test suit 정의
test_suite = unittest.TestSuite([sitter_page, sitter_Interview])

# run test suite
if __name__ == '__main__':
    reportFolder = "../reports/"
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=reportFolder), verbosity=2).run(test_suite)
