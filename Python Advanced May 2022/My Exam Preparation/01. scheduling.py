# 01. Scheduling
# You are hired to create a program that implements SJF (Shortest Job First). It works by letting the shortest jobs to take the CPU, so jobs won't get frozen.
# On the first line you will be given the jobs as integers (clock-cycles needed to finish the job) separated by comma and space ", ". On the second line you will be given the index of the job that we are interested in and want to know how many cycles will pass until the job is done.
# The tasks that need the least amount of clock-cycles will be completed first.
# For the jobs that need the same amount of clock-cycles, the order is FIFO (First In First Out).
# You have to print how many clock-cycles will pass until the task you are interested in is completed. For more clarifications, see the examples below.
# Input
# On the first line you will receive numbers separated by ", "
# On the second line you will receive the index of the task you are interested in
# Output
# Single line: the clock-cycles that will pass until the task you are interested in is finished
#
# Input
# 4, 10, 10, 6, 2, 99
# 2
#
# Output
# 32

from sys import maxsize

jobs = [int(x) for x in input().split(", ")]
job_index = int(input())
total_cycles = 0

while True:
    job = min(jobs)
    current_index = jobs.index(job)
    if current_index == job_index:
        total_cycles += job
        break
    else:
        total_cycles += job
        jobs[current_index] = maxsize

print(total_cycles)

# jobs = [int(x) for x in input().split(", ")]
# job_index = int(input())
# total_cycles = 0
#
# while True:
#     temp_jobs = jobs.copy()
#     job = min(temp_jobs)
#
#     while job == 0:
#         job = min(temp_jobs)
#         temp_jobs.remove(job)
#
#     current_index = jobs.index(job)
#     if current_index == job_index:
#         total_cycles += job
#         break
#     else:
#         total_cycles += job
#         jobs[current_index] = 0
#
# print(total_cycles)

# jobs = [int(x) for x in input().split(", ")]
# job_index = int(input())
# total_cycles = 0
#
# while True:
#     temp_jobs = [x for x in jobs if x != 0]
#     job = min(temp_jobs)
#
#     current_index = jobs.index(job)
#     if current_index == job_index:
#         total_cycles += job
#         break
#     else:
#         total_cycles += job
#         jobs[current_index] = 0
#
# print(total_cycles)
