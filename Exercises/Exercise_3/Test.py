import unittest
from unittest.mock import patch

# Import the functions from your Exercise script
from Exercise import coin_tosses, count, percentage, main


class TestCoinTossSimulation(unittest.TestCase):
    def setUp(self):
        # Example data for tests
        self.random_cases = [[1, 0, 1, 1, 0], [1, 1, 1, 0, 0, 1, 0, 1]]
        self.count_answers = [(3, 2), (5, 3)]
        self.percentage_answers = [(60.0, 40.0), (62.5, 37.5)]

    def mock_input(self, prompt):
        self.output.append(prompt)
        return self.input_values.pop(0)

    def mock_print(self, *args, **kwargs):
        end = kwargs.get('end', '\n')
        self.output.append(''.join(map(str, args)) + end)

    def run_test(self, tosses, expected_output):
        self.input_values = [str(len(tosses))]
        self.output = []

        with patch('builtins.input', side_effect=self.mock_input):
            with patch('builtins.print', side_effect=self.mock_print):
                with patch('Exercise.coin_tosses', return_value=tosses):
                    main()

        self.assertEqual(self.output, expected_output)

    def test_coin_toss_simulation(self):
        # Test case 1
        tosses1 = [1, 0, 0, 0, 1]
        expected_output1 = [
            'How many coin tosses would you like to simulate?\n',
            '\nNo. of Heads: 2\n',
            'No. of Tails: 3\n',
            '\n%   of Heads: 40.0\n',
            '%   of Tails: 60.0\n'
        ]
        self.run_test(tosses1, expected_output1)

        # Test case 2
        tosses2 = [0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1,
                   0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0,
                   0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0,
                   0]
        expected_output2 = [
            'How many coin tosses would you like to simulate?\n',
            '\nNo. of Heads: 47\n',
            'No. of Tails: 56\n',
            '\n%   of Heads: 45.63\n',
            '%   of Tails: 54.37\n'
        ]
        self.run_test(tosses2, expected_output2)

    def test_percentage_calculation(self):
        for count_tosses, per_tosses in zip(self.count_answers, self.percentage_answers):
            student_per = percentage(count_tosses)
            self.assertEqual(student_per, per_tosses, msg="Percentages incorrect to 2 decimal places")

    def test_count_function(self):
        for rand_nums, count_tosses in zip(self.random_cases, self.count_answers):
            student_count = count(rand_nums)
            self.assertEqual(student_count, count_tosses, msg="Count of heads and tails incorrect")

    def test_coin_tosses_function(self):
        x = coin_tosses(1000)
        y = coin_tosses(1000)
        self.assertNotEqual(x, y, msg="Random output for 1000 tosses is the same for two runs of the function coin_tosses(1000)")
        self.assertTrue(min(x) == 0 and max(x) == 1, msg="minimum value is not 0 or maximum value is not 1")
        self.assertTrue(min(y) == 0 and max(y) == 1, msg="minimum value is not 0 or maximum value is not 1")
        self.assertEqual(len(x), 1000, msg="Incorrect number of tosses generated")
        self.assertEqual(len(y), 1000, msg="Incorrect number of tosses generated")

if __name__ == '__main__':
    unittest.main()