'''Contains the engine function and other helper functions.
'''
from itertools import zip_longest
from collections.abc import Iterable

from .parameters import Parameter


def expand(layer):
    '''Runs the combination expansion of nested Zipables/Productables.

    Args:
        layer (tuple): tuple containing the layer to expand.

    Yields:
        Zipable: The Zipable containing the expanded parameter combinations.
    '''
    layer_has_depth = isinstance(layer[0], tuple)
    if layer_has_depth:
        depth_has_param = any(isinstance(i, Parameter) for i in layer[0])
    else:
        depth_has_param = False
    layer_has_param = any(isinstance(i, Parameter) for i in layer)

    if depth_has_param:
        yield from (i + layer[1] for i in expand(layer[0]))
    elif layer_has_param:
        yield sum(layer)
    else:
        yield layer


def engine(*iterators):
    '''Expansion engine, runs the expansion and cleans up the output.

    Args:
        *iterators (Zipable): Sums the provided Zipables and expands the
        remaining combinations.

    Yields:
        Iterable: containing the expanded paremeters.
    '''
    group = len(iterators)
    iterators = sum(iterators)

    for i in iterators:
        out = expand(i)
        if group is not None:
            out = grouper(flatten(out), group)
        yield from out


def flatten(iterable):
    '''Flattens an iterable.

    Args:
        iterable (iterable): nested iterable to be falttened.

    Yields:
        element of iterable: element of the flattened iterable.
    '''
    for i in iterable:
        if isinstance(i, Iterable) and not isinstance(i, (str, bytes)):
            yield from flatten(i)
        else:
            yield i


def grouper(iterable, group_size, fillvalue=None):
    '''Groups elemeent of the provided iterable.

    Args:
        iterable: iterable to be grouped.
        group_size (int): group size.
        fillvalue (optional): value with which to fill missing elements.

    Yields:
        generator: a generator providing the grouped elements.
    '''
    args = [iter(iterable)] * group_size
    return zip_longest(*args, fillvalue=fillvalue)
