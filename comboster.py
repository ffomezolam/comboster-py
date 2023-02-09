""" comboster.py
-------------
helper module with functions for extracting combinations from input sequences
"""

import random
from itertools import permutations

# GENERAL

def all(seq, min=2):
    "Return all combinations of minimum [min] length"

    if min < 1: min = 1
    elif min > len(seq): min = len(seq)

    # recursive function
    def _all(s):
        nonlocal min, seq

        if len(s) > min:
            # we are able to create smaller sets
            # create subsets and recursively get combos from each
            for ix in range(len(s)-1, -1, -1):
                # get subset
                rest = [s[i] for i in range(len(s)) if i != ix]
                # get combos from subset
                yield from _all(rest)

        # get all combos of set
        for combo in permutations(s):
            # match input type
            if type(seq) == str: combo = ''.join(combo)
            elif type(seq) == list: combo = list(combo)

            # return the combo
            yield combo

    # start recursion
    yield from _all(seq)

def none(seq):
    "Return entire sequence as generator."
    return (seq for i in [0])

# SEQUENTIAL

def seq_all(seq, min=2):
    """
    Return all sequential combinations of minimum [min] length as generator.
    Example (min 2): abcd -> [ab, abc, abcd, bc, bcd, cd]
    """
    slen = len(seq)
    return (seq[i:j] for i in range(slen) for j in range(i + 1, slen + 1) if (j - i) >= min)

def seq_to_end(seq, min=2):
    """
    Return sequential combinations of minimum [min] length to end of sequence as generator.
    Example (min 2): abcd -> [abcd, bcd, cd]
    """
    slen = len(seq)
    return (seq[i:] for i in range(slen) if (slen - i) >= 2)

# RANDOM

def random_unique(seq, limit: int = 0, min=2, max_tries = 100, seed=None):
    "Return random combinations of minimum [min] length without replacement or repeat"

    random.seed(seed)

    # if no limit specified, limit is total number of possible combinations
    if not limit: limit = len(list(all(seq, min)))

    slen = max = len(seq)
    tries = 0

    picked = set() # combos already picked

    for _ in range(limit):
        # limit how many times we can grab a random combo before timeout
        # TODO: adjust to weighted randomness to underweigh matched combos?
        while tries < max_tries:
            tries += 1

            # 1. get random size
            size = random.randrange(min, max)

            # 2. get random indexes without replacement
            ixs = random.sample(range(max), size)
            hixs = ''.join([str(i) for i in ixs]) # hashable for set

            # 3. unique combo
            if hixs not in picked:
                picked.add(hixs) # add to set of picked combos
                combo = [seq[i] for i in ixs] # get the combo

                if(type(combo) == str): ''.join(combo) # convert to string if appropriate

                yield combo # yield the combo
                tries = 0 # reset tries for next combo

if __name__ == "__main__":
    print("Comboster is the ultimate in fun!")
