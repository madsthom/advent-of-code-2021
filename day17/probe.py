# parse string 'target area: x=282..314, y=-80..-45' with regex
import re


def parse_target_area(area_string):
    area_regex = r'^target area: x=(-?\d+\.?\d*)\.\.(-?\d+\.?\d*), y=(-?\d+\.?\d*)\.\.(-?\d+\.?\d*)$'
    area_match = re.match(area_regex, area_string)
    if area_match:
        x_min = int(area_match.group(1))
        x_max = int(area_match.group(2))
        y_min = int(area_match.group(3))
        y_max = int(area_match.group(4))
        return x_min, y_min, x_max, y_max
    else:
        raise ValueError('invalid target area string')


def contains_point(point, target_area):
    x_min, y_min, x_max, y_max = target_area
    return x_min <= point[0] <= x_max and y_min <= point[1] <= y_max


def step_probe(position, velocity):
    x, y = position
    v, h = velocity
    if v == 0:
        position = x, y + h
    elif v == 0 and h == 0:
        position = x, y
    else:
        position = x + v, y + h

    if v == 0:
        velocity = v, h - 1
    else:
        velocity = v - 1, h - 1

    return position, velocity


def multiple_steps_probe(position, velocity, steps, target_area):
    inside_area = False
    highest_y = 0
    for _ in range(steps):
        position, velocity = step_probe(position, velocity)
        highest_y = max(highest_y, position[1])
        if contains_point(position, target_area):
            inside_area = True
            break
    return position, velocity, inside_area, highest_y


def find_highest_y():
    target_area = (282, -80, 314, -45)
    position = (0, 0)
    highest_y = 0
    for i in range(0, 100):
        for j in range(0, 100):
            velocity = (i, j)
            position = (0, 0)
            position, velocity, inside_area, y = multiple_steps_probe(position, velocity,
                                                                      500,
                                                                      target_area)
            if inside_area and y > highest_y:
                print(inside_area, y, velocity, position)
                highest_y = y
    return highest_y


def find_velocities_within_target_area():
    target_area = (282, -80, 314, -45)
    position = (0, 0)
    velos = []
    for i in range(0, 1000):
        for j in range(-1000, 1000):
            velocity = (i, j)
            position = (0, 0)
            position, new_velocity, inside_area, y = multiple_steps_probe(position, velocity,
                                                                          500,
                                                                          target_area)
            if inside_area:
                velos.append(velocity)
    return velos
