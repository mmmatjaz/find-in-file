import os
import unittest
from solution import process_file

SOLUTIONS = {
    "test1": ("[cat sees me]", "[mary likes trees]"),
    "test2": ("[to get very]", "[by her sister]")
}

SHOULD_FAIL = {
    "test3": ValueError,
}


class MyTestCase(unittest.TestCase):
    def test_good_files(self):
        for fn, result in SOLUTIONS.items():
            path = os.path.join("test_examples", f"{fn}.txt")
            self.assertEqual(list(result), process_file(path))

    def test_bad_files(self):
        for fn, error in SHOULD_FAIL.items():
            path = os.path.join("test_examples", f"{fn}.txt")
            self.assertRaises(error, lambda: process_file(path))

if __name__ == '__main__':
    unittest.main()
