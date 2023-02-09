""" comboster.py
-------------
helper module with functions for extracting combinations from input sequences
"""

import random
from itertools import permutations

# GLOBAL

# maximum items to return when doing random generation, based on testing of
# random generation algorithm
MAX_ITEM_LIMIT = 100_000

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

def random_unique(seq, limit: int = 0, min=2, *, max_tries = 100, seed = None, alg_cutoff = 8):
    "Return random combinations of minimum [min] length without replacement or repeat"

    random.seed(seed)

    if min >= len(seq):
        raise IndexError(f"Minimum combo length ({min}) exceeds sequence length ({len(seq)})")

    if len(seq) < alg_cutoff:
        # run easy version if length of sequence is below cutoff

        # get all possible combinations
        all_combos = list(all(seq, min))

        # number of total combos
        max = len(all_combos)

        # if no limit specified, limit is total number of possible combinations
        if not limit or limit > max or limit < 1: limit = max

        # get random indices by sampling without replacement
        combos = random.sample(all_combos, limit)

        yield from (c for c in combos)

    else:
        # large sequence: run complicated version

        # TODO: random.sample has an option to weigh the items in the sequence
        # so that might be usable to help balance the selection based on more
        # frequent or less frequent selection of certain items

        # set a safe limit
        if not limit: limit = MAX_ITEM_LIMIT

        # set tries counter to keep track of random attempts
        tries = 0

        # cache for generated sequences
        combo_cache = set()

        while tries < max_tries and len(combo_cache) < limit:
            # increase tries counter
            tries += 1

            # get a sequence size
            size = random.randrange(min, len(seq))

            # get a sample of values
            items = random.sample(seq, size)

            # convert to tuple for testing and storage
            titems = tuple(items)

            # if we haven't gotten combo before...
            if titems not in combo_cache:
                # store in combo cache
                combo_cache.add(titems)

                # convert to string if appropriate
                if type(seq) == str: items = ''.join(items)

                # reset tries counter
                tries = 0

                # yield
                yield items

if __name__ == "__main__":
    print("Comboster is the ultimate in fun!")
