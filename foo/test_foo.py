import unittest
import foo


class TestFoo(unittest.TestCase):
    """Test for foo"""

    def test_encode(self):
        # setup
        id_num = 760
        expected = "PUFqTjMwRFpwWlNaMUpIZDlrSGR3MVda"
        # exercise
        actual = foo.encode(id_num)
        # verify
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
