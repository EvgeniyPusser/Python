def time_on_rout(line: float):
    time = 0
    if line == 3:
        time = 110
    elif line == 5:
        time = 97
    elif line == 21:
        time = 121
    elif line == 33:
        time = 89
    else:
        print("ERROR: line is wrong")

    return time


def traffic_delay(period):
    delay = 0
    if 5.00 <= period <= 7.25:
        delay = 25
    elif 7.25 < period < 9.5:
        delay = 17
    elif 9.5 <= period < 12.5:
        delay = 15
    elif 12.5 <= period <= 14.00:
        delay = 9
    else:
        print("ERROR: wrong time of departure")

    return delay


line_of = int(input("Enter the line you chose"))
delay_of = float(input("Enter your time of going out"))

result = time_on_rout(line_of) + traffic_delay(delay_of)

# print(result)
if result >= 60 and (time_on_rout(line_of != 0) and traffic_delay(delay_of) != 0):
    result_h = result // 60
    result_minut = result % 60
    print(f"Your commuting time is {result_h} hours {result_minut} minutes")
