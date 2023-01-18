import unittest
from Alerts import Alerts
from tema9_Verificatori import Login
# din numele fisierului import numele clasei
# daca fisierul din care importam e intr-un alt folder, se scrie numele folderului inainte

# instalare package pt a genera un raport
import HtmlTestRunner


class TestSuite(unittest.TestCase):
    def test_suite(self):
        test_derulat = unittest.TestSuite()
        test_derulat.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Alerts), unittest.defaultTestLoader.loadTestsFromTestCase(Login)])
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title="Tests Report", report_name="Alerts and Login Suite")
        runner.run(test_derulat)
        # Combine reports ne genereaza un singur raport cu toate rezultatele pentru toate testele



