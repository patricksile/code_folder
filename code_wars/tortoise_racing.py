#!/usr/bin/env python3.5
# Problem: Tortoise_racing (6kyu)
"""
Two tortoises named A and B must run a race. A starts with an average speed of 720 feet per hour. Young B knows she runs faster than A and furthermore has not finished her cabbage.

When she starts, at last, she can see that A has a 70 feet lead but B speed is 850 feet per hour. How long will it take B to catch A?

More generally: given two speeds v1 (A speed, integer > 0) and v2 (B speed, integer > 0) and a lead g (integer > 0) how long will it take B to catch A?

The result will be an array [h, mn, s] where h, mn, s is the time needed in hours, minutes and seconds (don't worry for fractions of second). If v1 >= v2 then return nil, nothing, null, None or {-1, -1, -1} for C++, C, Go.

Examples:

race(720, 850, 70) => [0, 32, 18]
race(80, 91, 37) => [3, 21, 49]

"""

# My Solution:


def race(v1, v2, g):
    # Calculate the time at which B catches A, variable time.
    time = g / (v2 - v1)
    # Calculate hours, minutes and seconds
    hours = (time)
    minutes = round((time - int(time)) * 60, 3)
    seconds = round((minutes - int(minutes)) * 60, 3)
    if time < 0:
        return None
    return [int(hours), int(minutes), int(seconds)]


# Other Solutions:

# Solution 1: By Homtao adn 3rogue

def race(v1, v2, g):
    if v1 > v2:
        return None
    res = g * 3600 / (v2 - v1)
    return [int(res / 3600), int(res % 3600 / 60), int(res % 60)]

# Solution 2: By DryFruit


def race(v1, v2, g):
    if v2 < v1:
        return None
    res = g / ((v2 - v1) / 3600)
    h = res // 3600
    m = (res % 3600) // 60
    s = (res % 3600) % 60
    return list(map(int, [h, m, s]))


print(race(720, 850, 70))
