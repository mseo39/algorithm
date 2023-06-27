def elapsed_time(start_time, end_time):
    start_hour, start_min, start_sec = start_time
    end_hour, end_min, end_sec = end_time

    elapsed_hour = end_hour - start_hour
    elapsed_min = end_min - start_min
    elapsed_sec = end_sec - start_sec

    if elapsed_sec < 0:
        elapsed_min -= 1
        elapsed_sec += 60

    if elapsed_min < 0:
        elapsed_hour -= 1
        elapsed_min += 60

    if elapsed_hour < 0:
        elapsed_hour += 24

    return elapsed_hour, elapsed_min, elapsed_sec

# 예시로 주어진 경우
start_time = (23, 45, 0)
end_time = (9, 30, 0)

result = elapsed_time(start_time, end_time)
print(result)