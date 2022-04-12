from __future__ import annotations
from Matrix import *

position = tuple[int, int]
compressed = tuple[position, float, tuple[float], tuple[int], tuple[int]]

class MatrixSparse(Matrix):
    _zero = float

    def __init__(self, zero):
        self._zero = zero

    #TODO: Ver como funciona
    @property
    def zero(self) -> float:
        #TODO: RICARDO
        pass

    #TODO: Ver como funciona
    @zero.setter
    def zero(self, val: float):
        #TODO: RICARDO
        pass

    @abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError

    def sparsity(self) -> float:
        #TODO: DIOGO
        pass

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
