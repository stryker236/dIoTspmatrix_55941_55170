from __future__ import annotations
from ctypes import Union
from MatrixSparse import *
from Position import *

matrix = dict[Position, float]


class MatrixSparseDOK(MatrixSparse):
    _items = matrix

    def __init__(self, zero: float = 0.0):
        if isinstance(zero,(float,int)):
            super().__init__(self,zero)
            self._items = {}
        raise ValueError

    def __copy__(self):
        return {key: value for key, value in self._items.items()}

    def __eq__(self, other: MatrixSparseDOK):
        return self._items == other._items

    def __iter__(self):
        #TODO: RUI OU DIOGO
        pass

    def __next__(self):
        #TODO: RUI OU DIOGO
        pass

    def __getitem__(self, pos: [Position, position]) -> float:
        return self._items[pos]

    def __setitem__(self, pos: [Position, position], val: [int, float]):
        self._items[pos] = val

    def __len__(self) -> int:
        return len(self._items)
        pass

    def _add_number(self, other: Union[int, float]) -> Matrix:
        #TODO:RICARDO
        #NUMERO PARA TODOS AS POSIÇOES DA MATRIZ
        pass

    def _add_matrix(self, other: MatrixSparse) -> MatrixSparse:
        #TODO:RICARDO
        pass

    def _mul_number(self, other: [int, float]) -> Matrix:
        #TODO:RICARDO
        pass

    def _mul_matrix(self, other: MatrixSparse) -> MatrixSparse:
        #TODO:RUI
        pass

    def dim(self) -> tuple[Position, ...]:
        #TODO: DIOGO
        pass

    def row(self, row: int) -> Matrix:
        #TODO: DIOGO
        pass

    def col(self, col: int) -> Matrix:
        #TODO:DIOGO
        pass

    def diagonal(self) -> Matrix:
        #TODO:DIOGO
        pass

    @staticmethod
    def eye(size: int, unitary: float = 1.0, zero: float = 0.0) -> MatrixSparseDOK:
        pass

    def transpose(self) -> MatrixSparseDOK:
        #TODO: DIOGO
        pass

    def compress(self) -> compressed:
        #TODO: RUI
        pass

    @staticmethod
    def doi(compressed_vector: compressed, pos: Position) -> float:
        #TODO: RUI
        pass

    @staticmethod
    def decompress(compressed_vector: compressed) -> MatrixSparse:
        #TODO: RUI
        pass
