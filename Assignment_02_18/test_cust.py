import unittest
import main_cust


class TestStringMethods(unittest.TestCase):

    def test_case_1(self):
        response = main_cust.discount(True, True, True)
        self.assertEqual(response, None)

    def test_case_2(self):
        response = main_cust.discount(True, True, False)
        self.assertEqual(response, None)

    def test_case_3(self):
        response = main_cust.discount(True, False, True)
        self.assertEqual(response, 20)

    def test_case_4(self):
        response = main_cust.discount(True, False, False)
        self.assertEqual(response, 15)

    def test_case_5(self):
        response = main_cust.discount(False, True, True)
        self.assertEqual(response, 30)

    def test_case_6(self):
        response = main_cust.discount(False, True, False)
        self.assertEqual(response, 10)

    def test_case_7(self):
        response = main_cust.discount(False, False, True)
        self.assertEqual(response, 20)

    def test_case_8(self):
        response = main_cust.discount(False, False, False)
        self.assertEqual(response, 0)

if __name__ == '__main__':
    unittest.main()