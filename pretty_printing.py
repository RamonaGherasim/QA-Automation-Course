dictionary = {"Name": "Ana", "Age": 20, "Qualification": "Automation Tester", "Experience": 3.5}

def prettyPrinting():
    for key, value in dictionary.items():
        print(f'{key}: {value}')

prettyPrinting()