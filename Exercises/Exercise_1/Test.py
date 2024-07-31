import unittest
from Exercise_1 import count_words


class TestCountWords(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(count_words("example.txt"), 15)

if __name__ == '__main__':
    unittest.main()
