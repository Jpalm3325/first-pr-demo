import unittest

from greet import greet


class TestGreet(unittest.TestCase):
    def test_greet_returns_hello_message(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_greet_raises_on_empty_name(self):
        with self.assertRaises(ValueError):
            greet("")


if __name__ == "__main__":
    unittest.main()
