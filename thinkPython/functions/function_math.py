# This will explore some 'math' functions

import math

print(math)
# <module 'math'(built-in)>

signal_power = 2
noise_power = 3

ration = signal_power / noise_power
decibels = 10 * math.log10(ration)
print(decibels)
# -1.7609125905568126

radians = 0.7
height = math.sin(radians)
print(height)
# 0.644217687237691

degrees = 45
radians2 = degrees / 180.0 * math.pi
print(math.sin(radians))
# 0.644217687237691

square_rt = math.sqrt(2)
print(square_rt)
# 1.4142135623730951
