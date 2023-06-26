"""
Iterators are fun!
Let's create some. Oh, and generators. Let's not forget generators!
"""
from typing import Any, Iterable, Hashable


class Dicterator:
    """
    Iterator that takes a dictionary and returns an index, key and value tuple.
    Useless, but works
    """
    def __init__(self, a_dict: dict[Hashable, Any]):
        self._dict = [(key, value) for key, value in a_dict.items()]
        self._max = len(self._dict)-1

    def __iter__(self):
        self._counter = -1
        return self

    def __next__(self):
        if self._counter < self._max:
            self._counter += 1
            return self._counter, self._dict[self._counter][0], self._dict[self._counter][1]
        else:
            raise StopIteration


def digenerator(a_dict: dict[Hashable, Any]):
    counter = 0
    for key, value in a_dict.items():
        yield counter, key, value
        counter += 1



if __name__ == '__main__':
    dictum = {
        'one': 1,
        'two': 2,
        'three': 'Three'
    }

    iterium = Dicterator(dictum)
    for idx, key, value in iterium:
        print(f"Index: {idx} -> {key}: {value}")

    for idx, key, value in digenerator(dictum):
        print(f"Index: {idx} -> {key}: {value}")
