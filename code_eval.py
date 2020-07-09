#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sys


class Cov:
    def __init__(self, e, t):
        self.effective = e
        self.term = t
    def __str__(self):
        return 'Effective: {} Term: {}'.format(self.effective,self.term)


def longest(coverage):

    if len(coverage) == 0:
        return None

    data = [0 for i in range(366)]

    for i in coverage:
        eff = i.effective
        term = i.term
        if eff < 1 or eff > 365:
            return None
        if term <1 or term > 365:
            return None

        for j in range(eff,term+1):
            data[j] = -1

    longest = 1
    start = 1
    end = 1

    while True:
        try:
            start = data.index(-1, end)
        except ValueError as e:
            break
        try:
            end   = data.index(0, start)
        except ValueError as e:
            break

        interval = end - start -1
        longest = interval if interval >= longest else longest

        if start == 0 and end == 0:
            break

    return longest


def main():
    coverages = [ Cov(1, 20),
                  Cov(21, 30),
                  Cov(15, 25),
                  Cov(28, 40),
                  Cov(50, 60),
                  Cov(61, 200)
                ]
    answer = longest(coverages)
    print(answer)


if __name__ == '__main__':
    main()
    sys.exit(0)


# eos






