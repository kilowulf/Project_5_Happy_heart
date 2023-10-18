import unittest
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

#
# class Unit_Tests_BloodPressureMonitor(unittest.TestCase):
#     bloodPressureMonitor = happyheart.BloodPressureMonitor()


if __name__ == '__main__':
    unittest.main()