import unittest
from ticky_check import find_error_message


class FindErrorMessage(unittest.TestCase):

    def test_string(self):
        self.assertEqual(
            find_error_message(
                "Jan 31 00:21:30 ubuntu.local ticky: ERROR The ticket was modified while updating (breee)"
            ).groups(),
            ("ERROR", "The ticket was modified while updating", "breee"),
            "The output doesn't match")

    def test_not_log_message(self):
        self.assertIsNone(find_error_message(""), None)

    def test_not_string(self):
        self.assertIsInstance(find_error_message(3.14), TypeError)


if __name__ == '__main__':
    unittest.main()
