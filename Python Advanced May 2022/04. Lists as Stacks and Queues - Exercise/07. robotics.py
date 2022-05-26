# 7.*Robotics
# There is a robotics factory. The current project is assembly-line robots.
# Each robot has a processing time – it is the time in seconds the robot needs to process a product. When a robot is free, it should take a product for processing and log its name, product, and processing start time.
# Each robot processes a product coming from the assembly line. A product is coming from the line each second (so the first product should appear at [start time + 1 second]). If a product passes the line and there is not a free robot to take it, it should be queued at the end of the line again.
# The robots are standing in the line in the order of their appearance.
# Input
# On the first line, you will receive the robots' names and their processing times in the format "robotName-processTime;robotName-processTime;robotName-processTime..."
# On the second line, you will get the starting time in the format "hh:mm:ss"
# Next, until the "End" command, you will get a product on each line.
# Output
# Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"
#
# Input
# ROB-15;SS2-10;NX8000-3
# 8:00:00
# detail
# glass
# wood
# apple
# End
#
# Output
# ROB - detail [08:00:01]
# SS2 - glass [08:00:02]
# NX8000 - wood [08:00:03]
# NX8000 - apple [08:00:06]

from collections import deque


def time_to_sec(t):
    result = t[0] * 60 * 60 + t[1] * 60 + t[2]
    return result


def sec_to_time(seconds):
    seconds = seconds % (24 * 60 * 60)

    # hours = seconds // 3600
    # minutes = (seconds % 3600) // 60
    # seconds = (seconds % 3600) % 60
    # return f'{hours:02d}:{minutes:02d}:{seconds:02d}'

    hours = seconds // (60 * 60)
    seconds -= hours * (60 * 60)
    minutes = seconds // 60
    seconds -= minutes * 60
    if hours < 10:
        hh = f"0{hours}"
    else:
        hh = hours
    if minutes < 10:
        mm = f"0{minutes}"
    else:
        mm = minutes
    if seconds < 10:
        ss = f"0{seconds}"
    else:
        ss = seconds
    return f"{hh}:{mm}:{ss}"


robots_line = input().split(";")
robots = {}

for robot in robots_line:
    name, process_time = robot.split("-")
    robots[name] = int(process_time)

available_robots = [k for k in robots.keys()]
processing_robots = {}

start_time_list = [int(x) for x in input().split(":")]
start_time = time_to_sec(start_time_list)

products_que = deque()
while True:
    product = input()
    if product == "End":
        break
    products_que.append(product)

while products_que:
    start_time += 1
    for robot_name in [k for k in processing_robots.keys()]:
        processing_robots[robot_name] -= 1
        if processing_robots[robot_name] <= 0:
            processing_robots.pop(robot_name)
    current_product = products_que.popleft()
    for robot_name in available_robots:
        if robot_name not in processing_robots:
            print(f"{robot_name} - {current_product} [{sec_to_time(start_time)}]")
            processing_robots[robot_name] = robots[robot_name]
            break
    else:
        products_que.append(current_product)
