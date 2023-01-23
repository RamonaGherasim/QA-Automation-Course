from Alerts import Alerts
from tema9_Verificatori import Login
from Keys import Key
from Context_menu import ContextMenu
from Firefox_auth import Firefox

# din numele fisierului import numele clasei
# daca fisierul din care importam e intr-un alt folder, se scrie numele folderului inainte

# instalare package pt a genera un raport
import HtmlTestRunner
import unittest


class TestSuite(unittest.TestCase):
    def test_suite(self):
        test_derulat = unittest.TestSuite()
        test_derulat.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Alerts), unittest.defaultTestLoader.loadTestsFromTestCase(Login), unittest.defaultTestLoader.loadTestsFromTestCase(Key), unittest.defaultTestLoader.loadTestsFromTestCase(Firefox), unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu)])
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title="Tests Report3", report_name="Alerts, Login, Key, ContextMenu and Firefox Suite")
        runner.run(test_derulat)
        # Combine reports ne genereaza un singur raport cu toate rezultatele pentru toate testele



