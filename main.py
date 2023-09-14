import time
import sys
from collections import deque


def check_alarms(pulse, oxygen_avg, bp_s, bp_d):
    alarm = "None"
    message = "Everything normal"

    if pulse is not None:
        if pulse < 20:
            return "Highest", "Pulse dangerously low"
        if pulse < 40:
            return "Medium", "Pulse too low"
        if pulse > 170:
            return "Highest", "Pulse dangerously high"
        if pulse > 130:
            return "Medium", "Pulse too high"
        if pulse > 110:
            return "Low", "Pulse elevated"

    if oxygen_avg is not None:
        if oxygen_avg < 50:
            return "Highest", "Oxygen level dangerously low"
        if oxygen_avg < 80:
            return "Medium", "Oxygen level too low"
        if oxygen_avg < 85:
            return "Low", "Oxygen level slightly low"

    if bp_s is not None and bp_d is not None:
        if bp_s > 200 or bp_d > 120:
            return "Medium", "Blood pressure dangerously high"
        if bp_s > 150 or bp_d > 90:
            return "Low", "Blood pressure elevated"
        if bp_s < 70 or bp_d < 40:
            return "Medium", "Blood pressure too low"
        if bp_s < 50 or bp_d < 33:
            return "Highest", "Blood pressure dangerously low"

    return alarm, message


def read_data_source(data_source):
    data_line = data_source.readline().strip()
    pulse, oxygen, bp_s, bp_d = None, None, None, None

    if data_line == "":
        return None, None, None, None

    data_parts = data_line.split()

    try:
        pulse = int(data_parts[0])
    except (ValueError, IndexError):
        print("Invalid pulse data")

    try:
        oxygen = float(data_parts[1])
    except (ValueError, IndexError):
        print("Invalid oxygen data")

    try:
        bp_s, bp_d = map(int, data_parts[2].split('/'))
    except (ValueError, IndexError):
        print("Invalid blood pressure data")

    return pulse, oxygen, bp_s, bp_d


def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        data_source = open(file_name, 'r')
    else:
        data_source = sys.stdin

    oxygen_deque = deque(maxlen=6)  # For 1 minute moving average (6 x 10 seconds)
    missing_oxygen_count = 0
    time_elapsed = 0

    while True:
        pulse, oxygen, bp_s, bp_d = read_data_source(data_source)

        if pulse is None and oxygen is None and bp_s is None and bp_d is None:
            break

        if oxygen is not None:
            oxygen_deque.append(oxygen)
        else:
            missing_oxygen_count += 1

        if missing_oxygen_count >= 3:
            oxygen_avg = None
        else:
            oxygen_avg = sum(oxygen_deque) / len(oxygen_deque) if len(oxygen_deque) > 0 else None

        alarm, message = check_alarms(pulse, oxygen_avg, bp_s, bp_d)

        print(f"{time.strftime('%M:%S', time.gmtime(time_elapsed))} {alarm} {message}")

        time_elapsed += 10
        time.sleep(10)  # Sleep for 10 seconds

    if data_source != sys.stdin:
        data_source.close()


if __name__ == "__main__":
    main()