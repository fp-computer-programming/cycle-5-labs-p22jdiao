# Author: JD 10/25/2021

import time

import math

time_start = time.perf_counter_ns()

x = math.pow(2,2)

time_end = time.perf_counter_ns()

time_change = time_end - time_start

print(time_change)

time_start_2 = time.perf_counter_ns()

y = 2 ** 2

time_end_2 = time.perf_counter_ns()

time_change_2 = time_end_2 - time_start_2

print(time_change_2)