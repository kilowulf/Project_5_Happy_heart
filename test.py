import unittest

'''
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
'''

class Test_Case_PulseAlarm(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

class Test_Case_OxygenAlarm(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

class Test_Case_BloodPressureAlarm(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
