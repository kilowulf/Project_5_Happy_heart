import unittest
from collections import deque

import happyheart

'''
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
'''

class Unit_Tests_PulseMonitor(unittest.TestCase):
    pulseMonitor = happyheart.PulseMonitor()


    def test_pulse_safe_range(self):
        expectedResult = None
        # Edge cases
        self.assertEqual(expectedResult, self.pulseMonitor.check(40))
        self.assertEqual(expectedResult, self.pulseMonitor.check(110))
        # Middle case
        self.assertEqual(expectedResult, self.pulseMonitor.check(90))


    def test_pulse_equipment_malfunction(self):
        expectedSeverity = "Low"
        expectedMessage = "Pulse equipment malfunction"

        # Test cases that should output the expected.
        positiveTestPulses = [260, -1]

        for pulse in positiveTestPulses:
            testCase = self.pulseMonitor.check(pulse)
            errorMessage = f"Pulse: {pulse}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
            self.assertEqual(expectedSeverity, testCase.severity,errorMessage)
            self.assertEqual(expectedMessage, testCase.message, errorMessage)

        # Test cases that should not output the expected.
        negativeTestPulses = [259, 0]

        for pulse in negativeTestPulses:
            testCase = self.pulseMonitor.check(pulse)
            errorMessage = f"Pulse: {pulse}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
            self.assertNotEqual(expectedSeverity, testCase.severity,errorMessage)
            self.assertNotEqual(expectedMessage, testCase.message, errorMessage)


    def test_pulse_dangerously_low(self):
        expectedSeverity = "High"
        expectedMessage = "Pulse rate dangerously low"

        # Test cases that should output the expected.
        positiveTestPulses = [0, 19]

        for pulse in positiveTestPulses:
            testCase = self.pulseMonitor.check(pulse)
            errorMessage = f"Pulse: {pulse}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
            self.assertEqual(expectedSeverity, testCase.severity, errorMessage)
            self.assertEqual(expectedMessage, testCase.message, errorMessage)

        # Test cases that should not output the expected.
        negativeTestPulses = [-1, 20]

        for pulse in negativeTestPulses:
            testCase = self.pulseMonitor.check(pulse)
            errorMessage = f"Pulse: {pulse}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
            self.assertNotEqual(expectedSeverity, testCase.severity, errorMessage)
            self.assertNotEqual(expectedMessage, testCase.message, errorMessage)


    def test_pulse_low(self):
        expectedSeverity = "Medium"
        expectedMessage = "Pulse rate low"

        # Test cases that should output the expected.
        positiveTestPulses = [20, 39]

        for pulse in positiveTestPulses:
            testCase = self.pulseMonitor.check(pulse)
            errorMessage = f"Pulse: {pulse}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
            self.assertEqual(expectedSeverity, testCase.severity, errorMessage)
            self.assertEqual(expectedMessage, testCase.message, errorMessage)

        # Test cases that should not output the expected.
        negativeTestPulses = [19, 41]

        for pulse in negativeTestPulses:
            testCase = self.pulseMonitor.check(pulse)
            if testCase is not None:
                errorMessage = f"Pulse: {pulse}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
                self.assertNotEqual(expectedSeverity, testCase.severity, errorMessage)
                self.assertNotEqual(expectedMessage, testCase.message, errorMessage)

    
    def test_pulse_slightly_elevated(self):
        expectedSeverity = "Low"
        expectedMessage = "Pulse rate slightly elevated"

        # Test cases that should output the expected.
        positiveTestPulses = [130, 169]

        for pulse in positiveTestPulses:
            testCase = self.pulseMonitor.check(pulse)
            errorMessage = f"Pulse: {pulse}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
            self.assertEqual(expectedSeverity, testCase.severity, errorMessage)
            self.assertEqual(expectedMessage, testCase.message, errorMessage)

        # Test cases that should not output the expected.
        negativeTestPulses = [129, 170]

        for pulse in negativeTestPulses:
            testCase = self.pulseMonitor.check(pulse)
            if testCase is not None:
                errorMessage = f"Pulse: {pulse}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
                self.assertNotEqual(expectedSeverity, testCase.severity, errorMessage)
                self.assertNotEqual(expectedMessage, testCase.message, errorMessage)


    def test_pulse_high(self):
        expectedSeverity = "Medium"
        expectedMessage = "Pulse rate high"

        # Test cases that should output the expected.
        positiveTestPulses = [170, 209]

        for pulse in positiveTestPulses:
            testCase = self.pulseMonitor.check(pulse)
            errorMessage = f"Pulse: {pulse}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
            self.assertEqual(expectedSeverity, testCase.severity, errorMessage)
            self.assertEqual(expectedMessage, testCase.message, errorMessage)

        # Test cases that should not output the expected.
        negativeTestPulses = [169, 210]

        for pulse in negativeTestPulses:
            testCase = self.pulseMonitor.check(pulse)
            if testCase is not None:
                errorMessage = f"Pulse: {pulse}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
                self.assertNotEqual(expectedSeverity, testCase.severity, errorMessage)
                self.assertNotEqual(expectedMessage, testCase.message, errorMessage)


    def test_pulse_dangerously_high(self):
        expectedSeverity = "High"
        expectedMessage = "Pulse rate dangerously high"

        # Test cases that should output the expected.
        positiveTestPulses = [210, 259]

        for pulse in positiveTestPulses:
            testCase = self.pulseMonitor.check(pulse)
            errorMessage = f"Pulse: {pulse}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
            self.assertEqual(expectedSeverity, testCase.severity, errorMessage)
            self.assertEqual(expectedMessage, testCase.message, errorMessage)

        # Test cases that should not output the expected.
        negativeTestPulses = [209, 260]

        for pulse in negativeTestPulses:
            testCase = self.pulseMonitor.check(pulse)
            if testCase is not None:
                errorMessage = f"Pulse: {pulse}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
                self.assertNotEqual(expectedSeverity, testCase.severity, errorMessage)
                self.assertNotEqual(expectedMessage, testCase.message, errorMessage)

class Unit_Tests_OxygenMonitor(unittest.TestCase):
    oxygenMonitor = happyheart.OxygenMonitor()
    
    
    def test_missing_consecutive_readings(self):
        expectedSeverity = "Low"
        expectedMessage = "Missing 3 consecutive Blood Oxygen readings"

        # Test cases with missing consecutive readings
        for _ in range(2):
            testCase = self.oxygenMonitor.check(None)
            self.assertIsNone(testCase, "Expected result is None when there are less than 3 missing consecutive readings")
        for _ in range(3):
            testCase = self.oxygenMonitor.check(None)
        self.assertEqual(expectedSeverity, testCase.severity, expectedMessage)


    def test_oxygen_malfunction(self):
        expectedSeverity = "Low"
        expectedMessage = "Oxygen equipment malfunction"

    # Test cases that should output the expected.
        positiveTestOxygen = [0, 100]
        for oxygen in positiveTestOxygen:
            self.oxygenMonitor.oxygen_deque.clear()
            testCase = self.oxygenMonitor.check(oxygen)
            errorMessage = f"Oxygen: {oxygen}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
            self.assertEqual(expectedSeverity, testCase.severity, errorMessage)
            self.assertEqual(expectedMessage, testCase.message, errorMessage)

    # Test case that should not output the expected.
        negativeTestOxygen = [1]
        for oxygen in negativeTestOxygen:
            self.oxygenMonitor.oxygen_deque.clear()
            testCase = self.oxygenMonitor.check(oxygen)
            errorMessage = f"Oxygen: {oxygen}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
            self.assertNotEqual(expectedSeverity, testCase.severity, errorMessage)
            self.assertNotEqual(expectedMessage, testCase.message, errorMessage)

    # Test case that should have same severity but not messages
        negativeTestOxygen = [84]
        for oxygen in negativeTestOxygen:
            self.oxygenMonitor.oxygen_deque.clear()
            testCase = self.oxygenMonitor.check(oxygen)
            errorMessage = f"Oxygen: {oxygen}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
            self.assertEqual(expectedSeverity, testCase.severity, errorMessage)
            self.assertNotEqual(expectedMessage, testCase.message, errorMessage)


    def test_slightly_low_average_oxygen(self):
        expectedSeverity = "Low"
        expectedMessage = "Blood Oxygen slightly low"

        #Test cases that should output the expected.
        positiveTestOxygen = [80, 84]
        for oxygen in positiveTestOxygen:
            self.oxygenMonitor.oxygen_deque.clear()
            testCase = self.oxygenMonitor.check(oxygen)
            errorMessage = f"Oxygen: {oxygen}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
            self.assertEqual(expectedSeverity, testCase.severity, errorMessage)
            self.assertEqual(expectedMessage, testCase.message, errorMessage)

        # Test case that should not output the expected.
        negativeTestOxygen = [79]
        for oxygen in negativeTestOxygen:
            self.oxygenMonitor.oxygen_deque.clear()
            testCase = self.oxygenMonitor.check(oxygen)
            errorMessage = f"Oxygen: {oxygen}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
            self.assertNotEqual(expectedSeverity, testCase.severity, errorMessage)
            self.assertNotEqual(expectedMessage, testCase.message, errorMessage)

        # Test case that should output None.
        negativeTestOxygen = [85]
        for oxygen in negativeTestOxygen:
            self.oxygenMonitor.oxygen_deque.clear()
            testCase = self.oxygenMonitor.check(oxygen)
            self.assertIsNone(self.assertIsNone(testCase, "Expected result is None when Greater than 84"))


    def test_low_average_oxygen(self):
        expectedSeverity = "Medium"
        expectedMessage = "Blood Oxygen low"

        #Test cases that should output the expected.
        positiveTestOxygen = [50, 79]
        for oxygen in positiveTestOxygen:
            self.oxygenMonitor.oxygen_deque.clear()
            testCase = self.oxygenMonitor.check(oxygen)
            errorMessage = f"Oxygen: {oxygen}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
            self.assertEqual(expectedSeverity, testCase.severity, errorMessage)
            self.assertEqual(expectedMessage, testCase.message, errorMessage)

        # Test cases that should not output the expected.
        negativeTestOxygen = [49, 80]
        for oxygen in negativeTestOxygen:
            self.oxygenMonitor.oxygen_deque.clear()
            testCase = self.oxygenMonitor.check(oxygen)
            errorMessage = f"Oxygen: {oxygen}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
            self.assertNotEqual(expectedSeverity, testCase.severity, errorMessage)
            self.assertNotEqual(expectedMessage, testCase.message, errorMessage)


    def test_dangerously_low_average_oxygen(self):
        expectedSeverity = "High"
        expectedMessage = "Blood Oxygen dangerously low"

        #Test cases that should output the expected.
        positiveTestOxygen = [1, 49]
        for oxygen in positiveTestOxygen:
            self.oxygenMonitor.oxygen_deque.clear()
            testCase = self.oxygenMonitor.check(oxygen)
            errorMessage = f"Oxygen: {oxygen}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
            self.assertEqual(expectedSeverity, testCase.severity, errorMessage)
            self.assertEqual(expectedMessage, testCase.message, errorMessage)

        # Test cases that should not output the expected.
        negativeTestOxygen = [0, 50]
        for oxygen in negativeTestOxygen:
            self.oxygenMonitor.oxygen_deque.clear()
            testCase = self.oxygenMonitor.check(oxygen)
            errorMessage = f"Oxygen: {oxygen}\nSeverity: {testCase.severity}\nMessage: {testCase.message}\n"
            self.assertNotEqual(expectedSeverity, testCase.severity, errorMessage)
            self.assertNotEqual(expectedMessage, testCase.message, errorMessage)


class Unit_Tests_BloodPressureMonitor(unittest.TestCase):
    bloodPressureMonitor = happyheart.PressureMonitor()

    def automate_bp_systolic_positive_test_cases(self, expectedSeverity, expectedMessage, testCaseList):
        for testCase in testCaseList:
            result = self.bloodPressureMonitor.check_systolic(testCase)
            errorMessage = f"Sytstolic Pressure: {testCase}\nSeverity: {result.severity}\nMessage: {result.message}\n"
            self.assertEqual(expectedSeverity, result.severity, errorMessage)
            self.assertEqual(expectedMessage, result.message, errorMessage)

    def automate_bp_systolic_negative_test_cases(self, expectedSeverity, expectedMessage, testCaseList):
        for testCase in testCaseList:
            result = self.bloodPressureMonitor.check_systolic(testCase)
            errorMessage = f"Sytstolic Pressure: {testCase}\nSeverity: {result.severity}\nMessage: {result.message}\n"
            self.assertNotEqual(expectedSeverity, result.severity, errorMessage)
            self.assertNotEqual(expectedMessage, result.message, errorMessage)

    def automate_bp_diastolic_positive_test_cases(self, expectedSeverity, expectedMessage, testCaseList):
        for testCase in testCaseList:
            result = self.bloodPressureMonitor.check_diastolic(testCase)
            errorMessage = f"Diastolic Pressure: {testCase}\nSeverity: {result.severity}\nMessage: {result.message}\n"
            self.assertEqual(expectedSeverity, result.severity, errorMessage)
            self.assertEqual(expectedMessage, result.message, errorMessage)

    def automate_bp_diastolic_negative_test_cases(self, expectedSeverity, expectedMessage, testCaseList):
        for testCase in testCaseList:
            result = self.bloodPressureMonitor.check_diastolic(testCase)
            errorMessage = f"Diastolic Pressure: {testCase}\nSeverity: {result.severity}\nMessage: {result.message}\n"
            self.assertNotEqual(expectedSeverity, result.severity, errorMessage)
            self.assertNotEqual(expectedMessage, result.message, errorMessage)

    def test_bp_systolic_is_none(self):
        expected = None

        result = self.bloodPressureMonitor.check_systolic(None)
        self.assertEqual(expected, result)

    def test_bp_systolic_safe_zone(self):
        expected = None

        result = self.bloodPressureMonitor.check_systolic(70)
        self.assertEqual(expected, result)

        result = self.bloodPressureMonitor.check_systolic(150)
        self.assertEqual(expected, result)

    def test_bp_systolic_equipment_malfunction(self):
        expectedSeverity = "Low"
        expectedMessage = "Blood pressure equipment malfunction"

        # Test cases that should output the expected.
        positviveTestPressures = [-1, 231]
        self.automate_bp_systolic_positive_test_cases(expectedSeverity, expectedMessage, positviveTestPressures)

        # Test cases that should not output the expected.
        negativeTestPressures = [0, 230]
        self.automate_bp_systolic_negative_test_cases(expectedSeverity, expectedMessage, negativeTestPressures)

    def test_bp_systolic_dangerously_low(self):
        expectedSeverity = "High"
        expectedMessage = "Systolic Blood Pressure dangerously low"

        # Test cases that should output the expected.
        positviveTestPressures = [49]
        self.automate_bp_systolic_positive_test_cases(expectedSeverity, expectedMessage, positviveTestPressures)

        # Test cases that should not output the expected.
        negativeTestPressures = [50]
        self.automate_bp_systolic_negative_test_cases(expectedSeverity, expectedMessage, negativeTestPressures)

    def test_bp_systolic_low(self):
        expectedSeverity = "Medium"
        expectedMessage = "Systolic blood pressure low"

        # Test cases that should output the expected.
        positviveTestPressures = [50, 69]
        self.automate_bp_systolic_positive_test_cases(expectedSeverity, expectedMessage, positviveTestPressures)

        # Test cases that should not output the expected.
        negativeTestPressures = [49]
        self.automate_bp_systolic_negative_test_cases(expectedSeverity, expectedMessage, negativeTestPressures)

    def test_bp_systolic_slightly_elevated(self):
        expectedSeverity = "Low"
        expectedMessage = "Systolic blood pressure slightly elevated"

        # Test cases that should output the expected.
        positviveTestPressures = [151, 199]
        self.automate_bp_systolic_positive_test_cases(expectedSeverity, expectedMessage, positviveTestPressures)

        # Test cases that should not output the expected.
        negativeTestPressures = [200]
        self.automate_bp_systolic_negative_test_cases(expectedSeverity, expectedMessage, negativeTestPressures)

    def test_bp_systolic_high(self):
        expectedSeverity = "Medium"
        expectedMessage = "Systolic blood pressure high"

        # Test cases that should output the expected.
        positviveTestPressures = [200, 230]
        self.automate_bp_systolic_positive_test_cases(expectedSeverity, expectedMessage, positviveTestPressures)

        # Test cases that should not output the expected.
        negativeTestPressures = [231]
        self.automate_bp_systolic_negative_test_cases(expectedSeverity, expectedMessage, negativeTestPressures)

    def test_bp_diastolic_is_none(self):
        expected = None

        result = self.bloodPressureMonitor.check_diastolic(None)
        self.assertEqual(expected, result)

    def test_bp_diastolic_safe_zone(self):
        expected = None

        result = self.bloodPressureMonitor.check_diastolic(40)
        self.assertEqual(expected, result)

        result = self.bloodPressureMonitor.check_diastolic(90)
        self.assertEqual(expected, result)

    def test_bp_diastolic_equipment_malfunction(self):
        expectedSeverity = "Low"
        expectedMessage = "Blood pressure equipment malfunction"

        # Test cases that should output the expected.
        positviveTestPressures = [-1, 151]
        self.automate_bp_diastolic_positive_test_cases(expectedSeverity, expectedMessage, positviveTestPressures)

        # Test cases that should not output the expected.
        negativeTestPressures = [0, 150]
        self.automate_bp_diastolic_negative_test_cases(expectedSeverity, expectedMessage, negativeTestPressures)

    def test_bp_diastolic_dangerously_low(self):
        expectedSeverity = "High"
        expectedMessage = "Diastolic Blood Pressure dangerously low"

        # Test cases that should output the expected.
        positviveTestPressures = [0, 32]
        self.automate_bp_diastolic_positive_test_cases(expectedSeverity, expectedMessage, positviveTestPressures)

        # Test cases that should not output the expected.
        negativeTestPressures = [33]
        self.automate_bp_diastolic_negative_test_cases(expectedSeverity, expectedMessage, negativeTestPressures)

    def test_bp_diastolic_low(self):
        expectedSeverity = "Medium"
        expectedMessage = "Diastolic blood pressure low"

        # Test cases that should output the expected.
        positviveTestPressures = [33, 39]
        self.automate_bp_diastolic_positive_test_cases(expectedSeverity, expectedMessage, positviveTestPressures)

        # Test cases that should not output the expected.
        negativeTestPressures = [32]
        self.automate_bp_diastolic_negative_test_cases(expectedSeverity, expectedMessage, negativeTestPressures)

    def test_bp_diastolic_slightly_elevated(self):
        expectedSeverity = "Low"
        expectedMessage = "Diastolic blood pressure slightly elevated"

        # Test cases that should output the expected.
        positviveTestPressures = [91, 119]
        self.automate_bp_diastolic_positive_test_cases(expectedSeverity, expectedMessage, positviveTestPressures)

        # Test cases that should not output the expected.
        negativeTestPressures = [120]
        self.automate_bp_diastolic_negative_test_cases(expectedSeverity, expectedMessage, negativeTestPressures)

    def test_bp_diastolic_high(self):
        expectedSeverity = "Medium"
        expectedMessage = "Diastolic blood pressure high"

        # Test cases that should output the expected.
        positviveTestPressures = [120, 149]
        self.automate_bp_diastolic_positive_test_cases(expectedSeverity, expectedMessage, positviveTestPressures)

        # Test cases that should not output the expected.
        negativeTestPressures = [119, 151]
        self.automate_bp_diastolic_negative_test_cases(expectedSeverity, expectedMessage, negativeTestPressures)

    def test_bp_compare_alarms_both_none(self):
        expected = None
        result = self.bloodPressureMonitor.compare_alarms(None, None)
        self.assertEqual(result, expected)

    def test_bp_compare_alarms_systolic_none(self):
        expectedSeverity = "High"
        expectedMessage = "Diastolic Blood Pressure dangerously low"
        diastolicAlarm = self.bloodPressureMonitor.check_diastolic(32)
        result = self.bloodPressureMonitor.compare_alarms(None, diastolicAlarm)
        self.assertEqual(result.severity, expectedSeverity)
        self.assertEqual(result.message, expectedMessage)

    def test_bp_compare_alarms_diastolic_none(self):
        expectedSeverity = "High"
        expectedMessage = "Systolic Blood Pressure dangerously low"
        systolicAlarm = self.bloodPressureMonitor.check_systolic(40)
        result = self.bloodPressureMonitor.compare_alarms(systolicAlarm, None)
        self.assertEqual(result.severity, expectedSeverity)
        self.assertEqual(result.message, expectedMessage)

    def test_bp_compare_alarms_systolic_high(self):
        expectedSeverity = "High"
        expectedMessage = "Systolic Blood Pressure dangerously low"

        systolicAlarm = self.bloodPressureMonitor.check_systolic(40)

        # Diastolic Low Alarm
        diastolicAlarm = self.bloodPressureMonitor.check_diastolic(-1)

        result = self.bloodPressureMonitor.compare_alarms(systolicAlarm, diastolicAlarm)
        self.assertEqual(result.severity, expectedSeverity)
        self.assertEqual(result.message, expectedMessage)

        # Diastolic Medium Alarm
        diastolicAlarm = self.bloodPressureMonitor.check_diastolic(120)

        result = self.bloodPressureMonitor.compare_alarms(systolicAlarm, diastolicAlarm)
        self.assertEqual(result.severity, expectedSeverity)
        self.assertEqual(result.message, expectedMessage)

        # Diastolic High Alarm
        diastolicAlarm = self.bloodPressureMonitor.check_diastolic(32)

        result = self.bloodPressureMonitor.compare_alarms(systolicAlarm, diastolicAlarm)
        self.assertEqual(result.severity, expectedSeverity)
        self.assertEqual(result.message, expectedMessage)

    def test_bp_compare_alarms_diastolic_high(self):
        expectedSeverity = "High"
        expectedMessage = "Diastolic Blood Pressure dangerously low"

        diastolicAlarm = self.bloodPressureMonitor.check_diastolic(32)

        # Systolic Low Alarm
        systolicAlarm = self.bloodPressureMonitor.check_systolic(-1)

        result = self.bloodPressureMonitor.compare_alarms(systolicAlarm, diastolicAlarm)
        self.assertEqual(result.severity, expectedSeverity)
        self.assertEqual(result.message, expectedMessage)

        # Systolic Medium Alarm
        systolicAlarm = self.bloodPressureMonitor.check_systolic(200)

        result = self.bloodPressureMonitor.compare_alarms(systolicAlarm, diastolicAlarm)
        self.assertEqual(result.severity, expectedSeverity)
        self.assertEqual(result.message, expectedMessage)

        # Systolic High Alarm defaults to systolic because of priority
        systolicAlarm = self.bloodPressureMonitor.check_systolic(40)

        result = self.bloodPressureMonitor.compare_alarms(systolicAlarm, diastolicAlarm)
        self.assertEqual(result.severity, expectedSeverity)
        self.assertNotEqual(result.message, expectedMessage)

class Unit_Tests_HeartMonitor(unittest.TestCase):

    hm = happyheart.HeartMonitor()
    def test_heart_monitor_everything_normal(self):
        expected = None

        # Reset the oxygen deque for a fresh test
        self.hm.oxygen_monitor.oxygen_deque = deque(maxlen=6)

        pulse = 70
        oxygen = 95
        bp_s = 100
        bp_d = 50

        result = self.hm.check_all(pulse, oxygen, bp_s, bp_d)
        self.assertEqual(expected, result)

    def test_heart_monitor_pulse_first_priority(self):
        expectedSeverity = "High"
        expectedMessage = "Pulse rate dangerously high"

        # Reset the oxygen deque for a fresh test
        self.hm.oxygen_monitor.oxygen_deque = deque(maxlen=6)

        # All high alarms
        pulse = 210
        oxygen = 10
        bp_s = 25
        bp_d = 30

        result = self.hm.check_all(pulse, oxygen, bp_s, bp_d)
        self.assertEqual(expectedSeverity, result.severity)
        self.assertEqual(expectedMessage, result.message)

    def test_heart_monitor_oxygen_second_priority(self):
        expectedSeverity = "High"
        expectedMessage = "Blood Oxygen dangerously low"

        # Reset the oxygen deque for a fresh test
        self.hm.oxygen_monitor.oxygen_deque = deque(maxlen=6)

        # All high alarms except for pulse
        pulse = 70
        oxygen = 10
        bp_s = 25
        bp_d = 30

        result = self.hm.check_all(pulse, oxygen, bp_s, bp_d)
        self.assertEqual(expectedSeverity, result.severity)
        self.assertEqual(expectedMessage, result.message)

    def test_heart_monitor_bp_s_third_priority(self):
        expectedSeverity = "High"
        expectedMessage = "Systolic Blood Pressure dangerously low"

        # Reset the oxygen deque for a fresh test
        self.hm.oxygen_monitor.oxygen_deque = deque(maxlen=6)

        # All high alarms except for pulse and oxygen
        pulse = 70
        oxygen = 95
        bp_s = 25
        bp_d = 30

        result = self.hm.check_all(pulse, oxygen, bp_s, bp_d)
        self.assertEqual(expectedSeverity, result.severity)
        self.assertEqual(expectedMessage, result.message)

if __name__ == '__main__':
    unittest.main()