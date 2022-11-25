class TestCase1:
    def test_exe(selfself):
        print("Running testCase1")

    def runTwice(selfself):
        print("Run test again")


class TestCase2:
    def test_exe(self):
        print("Running testCase2")


class TestCase3:
    def __init__(self, name, summary):
        self.name = name
        self.summary = summary

    def get_name(self):
        return self.name

    def get_summary(self):
        return self.summary

    def test_exe(self):
        print("Running testCase3")

    def runTwice(self):
        print("Run test case 3 again")


# Daca suntem in main (adica in fisierul curent) atunci executam si codul asta si il afisam
# Altfel (daca accesam info din alt fisier => prin import), nu il executam si nu il afisam
if __name__ == "__main__":
    test3 = TestCase3("test case_0003", "this test case implements ...")
    print(test3.get_name())
    print(test3.name)

