from itertools import zip_longest
from collections.abc import Iterable

from .parameters import Params


def expand(layer):
    layer_has_depth = isinstance(layer[0], tuple)
    if layer_has_depth:
        depth_has_param = any(isinstance(i, Params) for i in layer[0])
    else:
        depth_has_param = False
    layer_has_param = any(isinstance(i, Params) for i in layer)
    # print('depth: ', layer_has_depth)
    # print('param: ', layer_has_param)

    if depth_has_param:
        yield from (i + layer[1] for i in expand(layer[0]))
    elif layer_has_param:
        yield sum(layer)
    else:
        yield layer


def engine(*iterators, group='auto'):
    if group == 'auto':
        group = len(iterators)
    iterators = sum(iterators)

    for i in iterators:
        out = expand(i)
        if group is not None:
            out = grouper(flatten(out), group)
        yield from out


def flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)
