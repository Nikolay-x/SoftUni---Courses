from collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()
total_cars = 0
crash = False

while True:
    command = input()

    if command == "END":
        break

    if command != "green":
        cars.append(command)
    else:
        in_out_time = green_light
        out_time = free_window
        count = 0
        for car in cars:
            needed_time = len(car)
            if needed_time <= in_out_time:
                total_cars += 1
                in_out_time -= needed_time
            else:
                count += 1
                remaining_needed_time = needed_time - in_out_time
                if remaining_needed_time <= out_time:
                    total_cars += 1
                elif remaining_needed_time > out_time:
                    index = remaining_needed_time - out_time + 2
                    ch = car[index]
                    print("A crash happened!")
                    print(f"{car} was hit at {ch}.")
                    crash = True
                    break
            if count > 0:
                break
        if cars:
            cars.popleft()
    if crash:
        break

if not crash:
    print("Everyone is safe.")
    print(f"{total_cars} total cars passed the crossroads.")
