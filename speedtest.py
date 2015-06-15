#!/usr/bin/env python

from fastcomp import compare
import random
import string

def randomstr(minlen=5, maxlen=7):
    charset = '01'
    length = random.randint(minlen, maxlen)
    return ''.join(random.choice(charset) for i in range(length))

if __name__ == "__main__":
    import timeit

    # Set up conditions
    setup = """
from __main__ import compare, randomstr
cases = [(randomstr(), randomstr()) for x in range(1000)]"""
    main = "for case in cases: compare(*case)"
    loops = 100
    
    # Run timeit 
    timer = timeit.Timer(main, setup=setup)
    result = timer.repeat(number=loops)

    # Result
    best = round(min(result)*1000/loops, 2)
    print('{} loops, best of 3: {} msec per loop'.format(loops, best))
