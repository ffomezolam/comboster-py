# Comboster

Python library for working with combinations. Very much a work in progress and
not intended for widespread use.

## Description

All functions return a generator which yields the results.

### `all(seq)`

Get all combinations from sequence.

For example: `abc -> ab, ba, ac, ca, bc, cb, abc, acb, bac, bca, cab, cba`

### `none(seq)`

Returns the sequence itself.

Included for compatibility with other projects that use this library.

### `seq_all(seq)`

Get all sequential combinations.

For example: `abc -> ab, abc, bc`

### `seq_to_end(seq)`

Get all sequential combinations to end of sequence.

For example: `abc -> abc, bc`

### `random_unique(seq)`

Get unique random combinations without repeat or replacement.

For example: `abc -> cb, acb, ba, ca, bac, ...`

## Why?

I needed combinations for another project, and didn't realize `itertools`
provides functions for working with combinations. But on closer inspection,
those functions were too limited for my needs so I'm still here.
