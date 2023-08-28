from main import *
import  unittest


class TestAuth(unittest.TestCase):
    def test_verify_code(self):
        self.assertEqual(verify_code(1234, 1234), "You are verified!!")
        self.assertEqual(verify_code(1234, 1235), "Wrong verification code")

    




if __name__ == '__main__':
    unittest.main()