#!/usr/bin/env python3

"""level_estimate
Rank cards with the data collected by level_assessment.py

Usage:
  anki_row.py [options] <file>...

Options:
  -h --help                     Show this screen.

"""

from docopt import docopt
from collections import defaultdict

import anki_row
from common import *

min_level = 1.
max_level = 100.

def get_level(comp, c1l, c2l):
    s = sum(comp)
    if s == 0:
        return c1l

    x = [i / s for i in comp]
    diff = abs(c1l - c2l) + (max_level-min_level)/10
    # less weight if the level difference is big
    weight = 1. - diff / (max_level-min_level)

    mid = (c1l+c2l)/2
    new_l = [mid-weight*(diff)-1, mid, mid+weight*(diff)+1]
    new_l = sum([x[i] * new_l[i] for i in range(3)])
    return new_l


def normalize(card_to_level, min_level, max_level):
    lower = min(card_to_level.values())
    upper = max(card_to_level.values())
    if upper == max_level and lower == 0:
        return

    for c, l in card_to_level.items():
        new_l = (l - lower) / (upper - lower) * (max_level - min_level) + min_level
        card_to_level[c] = float(int(new_l))


if __name__ == '__main__':
    data = from_json_file("output/level_data.json")

    arguments = docopt(__doc__, version='read_annotations')
    path_to_cards = anki_row.read_cards(arguments["<file>"])
    cards = list(path_to_cards.values())
    card_to_index = dict([(c["example"], i) for i,c in enumerate(cards)])

    card_to_level = defaultdict(lambda: (min_level + max_level)/2.)

    for it in range(100):
        # initialize
        card_count = defaultdict(lambda: 1.)
        card_to_level_sum = defaultdict(lambda: 0.)
        for c1, d in data.items():
            if not c1 in card_to_index: continue
            for c2, comp in d.items():
                if not c1 in card_to_index: continue
                c1l = card_to_level[c1]
                c2l = card_to_level[c2]
                card_to_level_sum[c1] += get_level(comp, c1l, c2l)
                card_to_level_sum[c2] += get_level(list(reversed(comp)), c2l, c1l)

                card_count[c1] += 1
                card_count[c2] += 1

        old_levels = [card_to_level[card["example"]] for card in cards]
        for card, count in card_count.items():
            new_level = float(card_to_level_sum[card]) / count
            card_to_level[card] = new_level

        normalize(card_to_level, min_level, max_level)
        new_levels = [card_to_level[card["example"]] for card in cards]
        if new_levels == old_levels:
            print("converged after " + str(it) + " iterations")
            break
        elif it == 99:
            print("diverged")
            print(old_levels)
            print(new_levels)



    lst = sorted(list(card_to_level.items()), key = lambda t: t[1])

    #print([c for c,l in lst])
    level_hist = []
    for cl in lst:
        hist_idx = int(cl[1]/10)
        while len(level_hist) <= hist_idx:
            level_hist += [0]
        level_hist[hist_idx] += 1
        print(str(cl))

    print("histogram: " + str(level_hist))

