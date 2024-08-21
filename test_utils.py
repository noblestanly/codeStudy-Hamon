import unittest
from utils import f

class TestUtils(unittest.TestCase):
    def test_uppercase_characters(self):
        self.assertEqual(f('HELLO'), {'H': 1, 'E': 1, 'L': 2, 'O': 1})

    def test_lowercase_characters(self):
        self.assertEqual(f('hello'), {'h': 1, 'e': 1, 'l': 2, 'o': 1})
        self.assertEqual(f('world'), {'w': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1})
        
    def test_empty_string(self):
        self.assertEqual(f(''), {})
        self.assertEqual(f(' '), {' ': 1})

    def test_single_character(self):
        self.assertEqual(f('a'), {'a': 1})
        self.assertEqual(f('z'), {'z': 1})

    def test_multiple_characters(self):
        self.assertEqual(f('abc'), {'a': 1, 'b': 1, 'c': 1})
        self.assertEqual(f('123'), {'1': 1, '2': 1, '3': 1})

    def test_duplicate_characters(self):
        self.assertEqual(f('aabbcc'), {'a': 2, 'b': 2, 'c': 2})
        self.assertEqual(f('111222'), {'1': 3, '2': 3})

    '''
    ToDo: Implement for handling mixed case
    '''
    # def test_mixed_case(self):
    #     self.assertEqual(f('HeLlO'), {'H': 1, 'e': 1, 'L': 2, 'O': 1})
    #     self.assertEqual(f('WoRlD'), {'W': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1})

if __name__ == '__main__':
    unittest.main()
