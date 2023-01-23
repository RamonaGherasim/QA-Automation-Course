# Create a HTML test report for homework 10
import HtmlTestRunner
import unittest
from tema10_Verificari_extra import TheInternetFirefox


class Hw10TestSuite(unittest.TestCase):
    def test_hw10_suite(self):
        test_cases = unittest.TestSuite()
        test_cases.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TheInternetFirefox))
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, open_in_browser=True, report_title="Homework 10 Test Report")
        runner.run(test_cases)