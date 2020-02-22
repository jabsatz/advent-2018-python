import functools
import operator
import json
import numpy as np
from Map2D import Map2D

data = json.load(open('inputs.json'))['day3']


def toInt(x): return int(x)


def parseString(string):
    splitted = string.split(" ")
    claim = str(splitted[0].replace('#', ''))
    size = list(map(toInt, splitted[3].split('x')))
    offset = list(map(toInt, splitted[2].replace(':', '').split(',')))
    return (offset, size, claim)


def part1(data):
    map2d = Map2D()
    for entry in data:
        offset, size, _ = parseString(entry)
        for i in range(size[0]):
            x = i + offset[0]
            for j in range(size[1]):
                y = j + offset[1]
                item = map2d.check(x, y)
                if item == None:
                    map2d.add(x, y, 'O')
                if item == 'O':
                    map2d.add(x, y, 'X')
    return map2d.count(lambda item: item == 'X')


print(part1(data))


def part2(data):
    map2d = Map2D()
    sharingClaims = set()
    allClaims = set()
    for entry in data:
        offset, size, claim = parseString(entry)
        allClaims.add(claim)
        for i in range(size[0]):
            x = i + offset[0]
            for j in range(size[1]):
                y = j + offset[1]
                item = map2d.check(x, y)
                if item == None:
                    map2d.add(x, y, [claim])
                else:
                    item.append(claim)
                    sharingClaims.update(set(item))
                    map2d.add(x, y, item)
    return allClaims.difference(sharingClaims).pop()


print(part2(data))
