import json

from logics.NaturalTableauxSolver import NaturalTableauxSolver

from termcolor import colored

test_files = [
    #"simple_tests.json",
     #"syllogism_tests.json",
     #"todo_tests.json",
    "iff_tests.json",
    "quantified_tests.json"
]

class FailedTest:
    def __init__(self, test, expected_result, actual_result):
        self.test = test
        self.expected_result = expected_result
        self.actual_result = actual_result

    def print(self):
        print(f"Test case failed")
        print(self.test)
        print(f"Expected result: {self.expected_result}")
        print(f"Actual result: {self.actual_result}")

for test_file_name in test_files:
    try:
        f = open(f"../data/{test_file_name}")
    except FileNotFoundError:
        f = open(f"data/{test_file_name}")
    current_file = json.load(f)

    failed_tests = []

    print(f"Evaluating tests file {test_file_name}")

    for test in current_file:
        premises = test["premises"]
        conclusion = test["conclusion"]
        expected_result = True if test["result"] == "valid" else False if test["result"] == "invalid" else None

        try:
            nts = NaturalTableauxSolver(premises, conclusion)
            result = nts.solve()

            if expected_result != result:
                failed_tests.append(FailedTest(test, expected_result, result))
        except Exception as e:
            failed_tests.append(FailedTest(test, expected_result, e.args[0]))


    if len(failed_tests) > 0:
        print(colored(f"{len(failed_tests)} of {len(current_file)} test(s) failed", "red"))
        for test in failed_tests:
            test.print()
            print("----------------")
    else:
        print(colored(f"All {len(current_file)} test(s) succeeded", "green"))

    print()
    print()
