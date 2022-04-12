from __future__ import annotations


class Position:
    _pos = tuple[int, int]

    def __init__(self, row: int, col: int):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        return str(self._pos)

    def __hash__(self):
        return hash(self._pos)

    def __getitem__(self, item: int) -> int:
        pass

    def __eq__(self, other: Position):
        pass
