import unittest
import main

'''
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
'''

class Unit_Tests_PulseAlarm(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

class Unit_Tests_OxygenAlarm(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

class Unit_Tests_BloodPressureAlarm(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
