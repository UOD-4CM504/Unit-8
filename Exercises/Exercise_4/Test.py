import unittest
from unittest.mock import patch

# Import the function to be tested
from Exercise import count_letters

class TestLetterCount(unittest.TestCase):
    def _run_count_letters_test(self, func, input_values, expected_output, *args):
        output = []

        def mock_input_func(*args):
            if len(args) > 0:
                output.append(args[0])
            return input_values.pop(0)

        def mock_print_func(*args, end="\n"):
            temp_str = ""
            if len(args) > 0:
                temp_str = " ".join([str(x) for x in args])
            output.append(f"{temp_str}{end}")

        with patch('builtins.input', side_effect=mock_input_func):
            with patch('builtins.print', side_effect=mock_print_func):
                try:
                    func(*args)
                except Exception as e:
                    error = f"Main method failed. {e}"
                    output.append(error)

        output = "".join(output)
        expected_output = "".join(expected_output)
        self.assertEqual(output, expected_output)

    def test_letter_count_for_files(self):
        # Test for test.txt
        expected_output1 = [
            'The count of the letters for the file test.txt is:\n\n', 'A: 1\n', 'T: 1\n',
            'W: 1\n', 'a: 3\n', 'c: 1\n', 'd: 3\n', 'e: 5\n', 'f: 2\n', 'g: 1\n',
            'h: 2\n', 'i: 7\n', 'l: 3\n', 'm: 2\n', 'n: 3\n', 'o: 2\n', 'p: 2\n',
            's: 6\n', 't: 1\n', 'w: 1\n'
        ]
        self._run_count_letters_test(count_letters, [], expected_output1, "test.txt")

        # Test for example.txt
        expected_output2 = [
            'The count of the letters for the file example.txt is:\n\n', 'A: 2\n', 'C: 4\n', 'D: 5\n', 'E: 1\n', 'F: 2\n',
            'I: 3\n', 'L: 1\n', 'M: 6\n', 'N: 4\n', 'P: 7\n', 'Q: 1\n', 'S: 3\n', 'U: 1\n', 'V: 2\n', 'a: 164\n',
            'b: 26\n', 'c: 87\n', 'd: 52\n', 'e: 251\n', 'f: 20\n', 'g: 40\n', 'h: 7\n', 'i: 171\n', 'j: 1\n',
            'l: 123\n', 'm: 84\n', 'n: 130\n', 'o: 84\n', 'p: 40\n', 'q: 26\n', 'r: 94\n', 's: 144\n', 't: 141\n',
            'u: 153\n', 'v: 25\n', 'x: 5\n'
        ]
        self._run_count_letters_test(count_letters, [], expected_output2, "example.txt")

if __name__ == '__main__':
    unittest.main()