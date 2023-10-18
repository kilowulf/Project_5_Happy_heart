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

    # def test_pulse_slightly_elevated(self):
    #     return
    # def test_pulse_high(self):
    #     return
    # def test_pulse_high(self):
    #     return

# class Unit_Tests_OxygenMonitor(unittest.TestCase):
#     oxygenMonitor = happyheart.OxygenMonitor()
#
# class Unit_Tests_BloodPressureMonitor(unittest.TestCase):
#     bloodPressureMonitor = happyheart.BloodPressureMonitor()


if __name__ == '__main__':
    unittest.main()