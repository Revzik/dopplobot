import unittest
from dopplobot.commands import utils


class UtilsTest(unittest.TestCase):
    def test_ping(self):
        self.assertEqual("pong", utils.ping())


if __name__ == "__main__":
    unittest.main()
