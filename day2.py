import functools
import operator
import json

data = json.load(open('inputs.json'))['day2']


def part1(data):
    counts = {
        2: 0,
        3: 0,
    }
    for word in data:
        uniqueLetters = set(word)
        uniqueCounts = set(
            map(lambda currentLetter: [i for i, letter in enumerate(word) if letter == currentLetter].__len__(),
                uniqueLetters))
        for count in counts:
            if count in uniqueCounts:
                counts[count] += 1

    return functools.reduce(operator.mul, counts.values())


print(part1(data))


def getDifferentIndex(word, otherWord):
    differentIndex = 0
    for index, letter in enumerate(word):
        if letter != otherWord[index]:
            if differentIndex:
                return None
            else:
                differentIndex = index
    return differentIndex


def part2(data):
    for index, firstWord in enumerate(data):
        otherWords = data[index + 1:]
        for otherWord in otherWords:
            difference = getDifferentIndex(firstWord, otherWord)
            if difference:
                return firstWord[:difference] + firstWord[difference + 1:]
    return None


print(part2(data))
