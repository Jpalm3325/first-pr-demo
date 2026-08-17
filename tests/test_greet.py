import unittest

from greet import greet


class TestGreet(unittest.TestCase):
    def test_greet_returns_hello_message(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")


if __name__ == "__main__":
    unittest.main()
