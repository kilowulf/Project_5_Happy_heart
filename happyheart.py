from collections import deque
import time
import sys

class PulseMonitor:
    def check(self, pulse):
        if 40 <= pulse <= 110:
            return None
        elif pulse < 0 or pulse > 259:
            return PulseAlarm("Low", "Pulse equipment malfunction")
        elif pulse < 20:
            return PulseAlarm("High", "Pulse rate dangerously low")
        elif pulse < 40:
            return PulseAlarm("Medium", "Pulse rate low")
        elif pulse >= 210:
            return PulseAlarm("High", "Pulse rate dangerously high")
        elif pulse >= 170:
            return PulseAlarm("Medium", "Pulse rate high")
        elif pulse >= 130:
            return PulseAlarm("Low", "Pulse rate slightly elevated")



class OxygenMonitor:
    def __init__(self):
        self.oxygen_deque = deque(maxlen=6)
        self.missing_oxygen_count = 0

    def check(self, oxygen):
        if oxygen is None:
            self.missing_oxygen_count += 1
            if self.missing_oxygen_count >= 3:
                return OxygenAlarm("Low", f"Missing {self.missing_oxygen_count} consecutive Blood Oxygen readings")
            return None
        if oxygen <= 0 or oxygen >= 100:
            self.missing_oxygen_count += 1
            return OxygenAlarm("Low", "Oxygen equipment malfunction")
        self.missing_oxygen_count = 0
        self.oxygen_deque.append(oxygen)
        oxygen_avg = sum(self.oxygen_deque) / len(self.oxygen_deque)
        if oxygen_avg < 50:
            return OxygenAlarm("High", "Blood Oxygen dangerously low")
        elif oxygen_avg < 80:
            return OxygenAlarm("Medium", "Blood Oxygen low")
        elif oxygen_avg < 85:
            return OxygenAlarm("Low", "Blood Oxygen slightly low")
        else:
            return None

class PressureMonitor:
    def check(self, bp_s, bp_d):
        systolic = self.check_systolic(bp_s)
        diastolic = self.check_diastolic(bp_d)
        return(self.compare_alarms(systolic, diastolic))

    def check_systolic(self, bp_s):
        if bp_s is None:
            return None
        if 70 <= bp_s <= 150:
            return None
        elif bp_s < 0 or bp_s > 230:
            return PressureAlarm("Low", "Blood pressure equipment malfunction")
        elif bp_s < 50:
            return PressureAlarm("High", "Systolic Blood Pressure dangerously low")
        elif bp_s < 70:
            return PressureAlarm("Medium", "Systolic blood pressure low")
        elif bp_s >= 200:
            return PressureAlarm("Medium", "Systolic blood pressure high")
        elif bp_s > 150:
            return PressureAlarm("Low", "Systolic blood pressure slightly elevated")


    def check_diastolic(self, bp_d):
        if bp_d is None:
            return None
        if 40 <= bp_d <= 90:
            return None
        elif bp_d < 0 or bp_d > 150:
            return PressureAlarm("Low", "Blood pressure equipment malfunction")
        elif bp_d < 33:
            return PressureAlarm("High", "Diastolic Blood Pressure dangerously low")
        elif bp_d < 40:
            return PressureAlarm("Medium", "Diastolic blood pressure low")
        elif bp_d >= 120:
            return PressureAlarm("Medium", "Diastolic blood pressure high")
        elif bp_d > 90:
            return PressureAlarm("Low", "Diastolic blood pressure slightly elevated")


    def compare_alarms(self, systolic_alarm, diastolic_alarm):
        if systolic_alarm is None and diastolic_alarm is None:
            return None
        if systolic_alarm is None:
            return diastolic_alarm
        elif diastolic_alarm is None:
            return systolic_alarm
        if systolic_alarm.get_level() >= diastolic_alarm.get_level():
            return systolic_alarm
        else:
            return diastolic_alarm

class PulseAlarm:
    def __init__(self, severity, message):
        self.severity = severity
        self.message = message
        self.levels = {"Low":1, "Medium":2, "High":3}

    def get_level(self):
        return self.levels[self.severity]

class OxygenAlarm:
    def __init__(self, severity, message):
        self.severity = severity
        self.message = message
        self.levels = {"Low":1, "Medium":2, "High":3}

    def get_level(self):
        return self.levels[self.severity]

class PressureAlarm:
    def __init__(self, severity, message):
        self.severity = severity
        self.message = message
        self.levels = {"Low":1, "Medium":2, "High":3}

    def get_level(self):
        return self.levels[self.severity]

class HeartMonitor:
    def __init__(self):
        self.pulse_monitor = PulseMonitor()
        self.oxygen_monitor = OxygenMonitor()
        self.pressure_monitor = PressureMonitor()
        self.pulse_alarm = None
        self.oxygen_alarm = None
        self.pressure_alarm = None

    def check_all(self, pulse, oxygen, bp_s, bp_d):
        self.pulse_alarm = self.pulse_monitor.check(pulse)
        self.oxygen_alarm = self.oxygen_monitor.check(oxygen)
        self.pressure_alarm = self.pressure_monitor.check(bp_s, bp_d)
        return self.highest_alarm()

    def highest_alarm(self):
        if self.pulse_alarm is None:
            pulse_level = 0
        else:
            pulse_level = self.pulse_alarm.get_level()
        if self.oxygen_alarm is None:
            oxygen_level = 0
        else:
            oxygen_level = self.oxygen_alarm.get_level()
        if self.pressure_alarm is None:
            pressure_level = 0
        else:
            pressure_level = self.pressure_alarm.get_level()
        if pressure_level == 0 and oxygen_level == 0 and pulse_level == 0:
            return None
        if pulse_level >= pressure_level and pulse_level >= oxygen_level:
            return self.pulse_alarm
        elif oxygen_level >= pressure_level:
            return self.oxygen_alarm
        else:
            return self.pressure_alarm

def read_data_source(data_source):
    data_line = data_source.readline().strip()
    pulse, oxygen, bp_s, bp_d = None, None, None, None

    if data_line == "":
        return None, None, None, None

    data_parts = data_line.split(" ")

    try:
        pulse = int(data_parts[0])
    except (ValueError, IndexError):
        print("Invalid pulse data")

    if len(data_parts) > 1:
        try:
            oxygen = float(data_parts[1])
            oxygen = round(oxygen, 1)
        except (ValueError, IndexError):
            print("Invalid oxygen data")

    if len(data_parts) > 2:
        try:
            bp_s, bp_d = map(int, data_parts[2].split('/'))
        except (ValueError, IndexError):
            print("Invalid blood pressure data")

    return pulse, oxygen, bp_s, bp_d

def main():
    #Welcome statements
    print("\n**WELCOME TO THE HAPPY HEART PROGRAM**")
    print("\nIf you have not provided a .txt document\ncontaining health data in the command line,\nenter health data manually in the following format:")
    print("\n'Pulse Reading' 'Oxygen Level' 'Blood Pressure'")
    print("\nEach value is separated by a space. You can omit\n'Oxygen Level' and 'Blood Pressure' but not 'Pulse Reading'.")
    print("\nIf you have provided a valid data file in the command line,\nthe program will execute on its own.\nTo exit, simply press Enter without entering any data.")
    print()

    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        data_source = open(file_name, 'r')
    else:
        data_source = sys.stdin

    heart_monitor = HeartMonitor()

    time_elapsed = 0

    while True:
        pulse, oxygen, bp_s, bp_d = read_data_source(data_source)

        if pulse is None and oxygen is None and bp_s is None and bp_d is None:
            break

        alarm = heart_monitor.check_all(pulse, oxygen, bp_s, bp_d)
        if alarm is None:
            severity = "None"
            message = "Everything is normal"
        else:
            severity = alarm.severity
            message = alarm.message
        print(f"{time.strftime('%M:%S', time.gmtime(time_elapsed))} {severity}:\t{message}")

        time_elapsed += 10
        # time.sleep(10)  # Sleep for 10 seconds

    if data_source != sys.stdin:
        data_source.close()

if __name__ == "__main__":
    main()