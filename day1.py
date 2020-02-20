import functools
import operator
import json

data = json.load(open('inputs.json'))['day1']


def part1(data):
    return functools.reduce(lambda x, y: x + int(y), data, 0)


print(part1(data))


def part2(data):
    numbers = list(map(lambda x: int(x), data))
    previous_frenquencies = set([])
    frequency = 0
    pos = 0
    while (frequency not in previous_frenquencies):
        previous_frenquencies.add(frequency)
        frequency += numbers[pos]
        pos = (pos + 1 if pos != numbers.__len__() - 1 else 0)
    return frequency


print(part2(data))
