import json

f = open('syllogism-data.json')
tests = json.load(f)

result_file = []

for test in tests:
    premises = []
    premises.append(test["premise_1"])
    premises.append(test["premise_2"])
    conclusion = test["conclusion"]
    result = test["valid"]

    new_test = {
        "premises": premises,
        "conclusion": conclusion,
        "result": result
    }

    result_file.append(new_test)

with open('syllogism_tests.json', 'w') as outfile:
    json.dump(result_file, outfile)