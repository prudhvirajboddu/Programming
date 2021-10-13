import unittest

# class Test(unittest.TestCase):
#     def upper(self):
#         self.var=15
#         self.assertEqual(self.var,15)

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(' '), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        # with self.assertRaises(TypeError):
        #     s.split(" ")

unittest.main()