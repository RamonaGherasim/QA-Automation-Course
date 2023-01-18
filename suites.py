import unittest
from Alerts import Alerts
# din numele fisierului import numele clasei
# daca fisierul din care importam e intr-un alt folder, se scrie numele folderului inainte

# instalare package pt a genera un raport
import HtmlTestRunner


class TestSuite(unittest.TestCase):
    def test_suite(self):
        test_derulat = unittest.TestSuite()
        test_derulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Alerts))
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title="My First Report", report_name="My First Report Name")
        runner.run(test_derulat)
        # Combine reports ne genereaza un singur raport cu toate rezultatele pentru toate testele



