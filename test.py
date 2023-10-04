import unittest
import main

'''
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
'''

class Unit_Tests_PulseAlarm(unittest.TestCase):
    
    pulseAlarm = main.PulseAlarm()

    def test_pulse_none(self):
        status, message = self.pulseAlarm.check(None)
        self.assertEqual(status, "None")
        self.assertEqual(message, "Everything normal")

    def test_pulse_dangerously_low(self):
        status, message = self.pulseAlarm.check(15)
        self.assertEqual(status, "Highest")
        self.assertEqual(message, "Pulse dangerously low")

    def test_pulse_too_low(self):
        status, message = self.pulseAlarm.check(35)
        self.assertEqual(status, "Medium")
        self.assertEqual(message, "Pulse too low")

    def test_pulse_dangerously_high(self):
        status, message = self.pulseAlarm.check(175)
        self.assertEqual(status, "Highest")
        self.assertEqual(message, "Pulse dangerously high")

    def test_pulse_too_high(self):
        status, message = self.pulseAlarm.check(135)
        self.assertEqual(status, "Medium")
        self.assertEqual(message, "Pulse too high")

    def test_pulse_elevated(self):
        status, message = self.pulseAlarm.check(115)
        self.assertEqual(status, "Low")
        self.assertEqual(message, "Pulse elevated")

    def test_pulse_normal(self):
        status, message = self.pulseAlarm.check(80)
        self.assertEqual(status, "None")
        self.assertEqual(message, "Everything normal")

class Unit_Tests_OxygenAlarm(unittest.TestCase):
    
    oxygenAlarm = main.OxygenAlarm()

    def test_oxygen_none(self):
        status, message = self.oxygenAlarm.check(None)
        self.assertEqual(status, "None")
        self.assertEqual(message, "Everything normal")

    def test_oxygen_dangerously_low(self):
        status, message = self.oxygenAlarm.check(10)
        self.assertEqual(status, "Highest")
        self.assertEqual(message, "Oxygen level dangerously low")

    def test_oxygen_too_low(self):
        status, message = self.oxygenAlarm.check(60)
        self.assertEqual(status, "Medium")
        self.assertEqual(message, "Oxygen level too low")

    def test_oxygen_slightly_low(self):
        status, message = self.oxygenAlarm.check(84)
        self.assertEqual(status, "Low")
        self.assertEqual(message, "Oxygen level slightly low")

    def test_oxygen_normal(self):
        status, message = self.oxygenAlarm.check(95)
        self.assertEqual(status, "None")
        self.assertEqual(message, "Everything normal")

class Unit_Tests_BloodPressureAlarm(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
