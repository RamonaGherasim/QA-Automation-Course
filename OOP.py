# Importare
class Test_case1:
    # Definirea metodei
    def printeaza_test_case(self):
        print("Running Test case 1")


class Test_Case2:
    def printeaza_test_case(self):
        print("Running Test case 2")


class Test_Case3:
    def __init__(self, name, summary):
        # Aici construim un atribut de tip name si altul de tip summary
        self.name = name
        self.summary = summary

    def retun_name(self):
        return self.name

    def return_summary(self):
        return self.summary

    def printeaza_test_case(self):
        print("Running Test case 3")

