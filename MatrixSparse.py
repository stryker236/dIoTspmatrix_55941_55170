from __future__ import annotations
from Matrix import *

position = tuple[int, int]
compressed = tuple[position, float, tuple[float], tuple[int], tuple[int]]

class MatrixSparse(Matrix):
    _zero = float

    def __init__(self, zero):
        self._zero = zero

    @property
    def zero(self) -> float:
        return self._zero

    #TODO: Ver como funciona
    @zero.setter
    def zero(self, val: float):
        iter(self)
        elem = next(self)

        if isinstance(val,(int,float)):
            self._zero = val

        while not (elem == ()):
            key, value = elem
            if(value == self._zero):
                del self._items[key]
            elem = next(self)

    @abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError

    def sparsity(self) -> float:
        positions = self.dim()
        if bool(self._items):
            min_row = positions[0][0]
            min_col = positions[0][1]
            max_row = positions[1][0]
            max_col = positions[1][1]
            total_elem = (max_col-min_col+1)*(max_row-min_row+1)
            zero_null = total_elem - len(self._items)
            return zero_null/float(total_elem)
        else:
            return 1.0

    @staticmethod
    @abstractmethod
    def eye(size: int, unitary: float = 1.0, zero: float = 0.0) -> MatrixSparse:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def compress(self) -> compressed:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def doi(compressed_vector: compressed, pos: Position) -> float:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def decompress(compressed_vector: compressed) -> Matrix:
        raise NotImplementedError
