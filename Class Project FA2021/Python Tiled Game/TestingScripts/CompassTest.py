import math
"""
https://www.analytics-link.com/post/2018/08/21/calculating-the-compass-direction-between-two-points-in-python
"""
def direction_lookup(destination_x, origin_x, destination_y, origin_y):

    deltaX = destination_x - origin_x
    deltaY = destination_y - origin_y

    degrees_temp = math.atan2(deltaX, deltaY) / math.pi * 180

    if degrees_temp < 0:
        degrees_final = 360 + degrees_temp
    else:
        degrees_final = degrees_temp
    compass_brackets = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]
    compass_lookup = round(degrees_final / 45)

    return compass_brackets[compass_lookup], degrees_final


print(direction_lookup(7, 6, 7, 3))

print(direction_lookup(1, 1, 2, 1)) # should point up/North/0
print(direction_lookup(1, 1, 0, 1)) # should point down/south/180
print(direction_lookup(2, 1, 1, 1)) # should point right/east/90
print(direction_lookup(0, 1, 1, 1)) # should point left/west/270

# Above Testing Shows that the second (origin) should be player location

"""
For the radial compass, we could use this calc to return it as an 8 way arrow?
Feed the player XY into the first two params.
Feed target XY into second params.
Use on update and pull the degrees_final to rotate an arrow?
"""