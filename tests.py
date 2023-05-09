import unittest
from solution import proc_file

SOLUTIONS = {
    "test1": ("[cat sees me]", "[mary likes trees]"),
    "test2": ("[to get very]", "[by her sister]")
}


class MyTestCase(unittest.TestCase):
    def test_files(self):
        for fn, result in SOLUTIONS.items():
            self.assertEqual(list(result), proc_file(f"{fn}.txt"))  # add assertion here


if __name__ == '__main__':
    unittest.main()
