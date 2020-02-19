import functools
import operator
import json

data = json.load(open('inputs.json'))['day1']


def part1(input):
    return functools.reduce(lambda x, y: x + int(y), input, 0)


print(part1(data))


def part2(input):
    numbers = list(map(lambda x: int(x), input))
    previous_frenquencies = set([])
    frequency = 0
    pos = 0
    while (frequency not in previous_frenquencies):
        previous_frenquencies.add(frequency)
        frequency += numbers[pos]
        pos = (pos + 1 if pos != numbers.__len__() - 1 else 0)
    return frequency


print(part2(data))
