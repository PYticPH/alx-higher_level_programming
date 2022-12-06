#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum = ()
    if not tuple_a:
        return (tuple_b)
    if not tuple_b:
        return (tuple_a)
    if len(tuple_a) < 2:
        sum = (tuple_a[0] + tuple_b[0], 0 + tuple_b[1])
    elif len(tuple_b) < 2:
        sum = (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
    else:
        sum = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (sum)
