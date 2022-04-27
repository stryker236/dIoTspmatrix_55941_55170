from __future__ import annotations
from ctypes import Union
from MatrixSparse import *
from Position import *

matrix = dict[Position, float]


class MatrixSparseDOK(MatrixSparse):
    _items = matrix

    def __init__(self, zero: float = 0.0):
        if isinstance(zero, (float, int)):
            super().__init__(zero)
            self._items = {}
        raise ValueError

    def __copy__(self):
        return {key: value for key, value in self._items.items()}

    def __eq__(self, other: MatrixSparseDOK):
        return self._items == other._items

    # Cria objeto iteravel
    def __iter__(self):
        self.current_index = 0
        self.max = len(self._items)
        self.iter_aux = sorted(self._items)
        # Não sei se retornar o proprio objeto é a melhor forma de lidar
        return self

    # Próximo elemento do iterador
    def __next__(self):
        if(self.current_index < self.max):
            value = self._items[self.iter_aux[self.current_index]]
            self.current_index += 1
            return 
        # Não sei se é suposto fazer raise
        raise StopIteration

    def __getitem__(self, pos: Union[Position, position]) -> float:
        return self._items[pos]

    def __setitem__(self, pos: Union[Position, position], val: Union[int, float]):
        self._items[pos] = val

    def __len__(self) -> int:
        return len(self._items)

    def _add_number(self, other: Union[int, float]) -> Matrix:
        if isinstance(other, (int, float)):
            for key in self._items:
                self._items[key] += other

    def _add_matrix(self, other: MatrixSparse) -> MatrixSparse:
        #TODO: Diogo
        pass

    def _mul_number(self, other: Union[int, float]) -> Matrix:
        if isinstance(other, (int, float)):
            for key in self._items:
                self._items[key] *= other

    def _mul_matrix(self, other: MatrixSparse) -> MatrixSparse:
        #TODO: DIOGO
        pass

    def dim(self) -> tuple[Position, ...]:
        # lista apenas de positions
        positions = sorted(self._items)
        # tem que ser spmatrix
        # se posiçoes na matrix

        if bool(self._items):
            # nao sei se aceder às linhas e às colunas resulta
            min_row = positions[0][0]
            max_col = positions[0][1]
            max_row = positions[0][0]
            min_col = positions[0][1]
            for pos in positions:
                if pos[0] > max_row:
                    max_row = pos[0]
                if pos[0] < min_row:
                    min_row = pos[0]
                if pos[1] > max_col:
                    max_col = pos[1]
                if pos[1] < min_col:
                    min_col = pos[1]
            return ((min_row, min_col), (max_row, max_col))
        return ()
    

    def row(self, row: int) -> Matrix:
        aux = {}
        if isinstance(row,int):
            for key, value in self._items:
                if(key[0] == row):
                    aux[key] = value
            # Não sei exatamente o retornar
            return aux

    def col(self, col: int) -> Matrix:
        aux = {}
        if isinstance(col,int):
            for key, value in self._items:
                if(key[1] == col):
                    aux[key] = value
            # Não sei exatamente o retornar
            return aux

    def diagonal(self) -> Matrix:
        aux = {}
        for key, value in self._items:
            if(key[0] == key[1]):
                aux[key] = value
        # Não sei exatamente o retornar
        return aux

    @staticmethod
    def eye(size: int, unitary: float = 1.0, zero: float = 0.0) -> MatrixSparseDOK:
        pass

    def transpose(self) -> MatrixSparseDOK:
        aux = {}
        for key, value in self._items.items():
            aux[(key[1],key[0])] = value
        # Não sei exatamente o retornar
        return aux 

    # TODO: Rui
    def compress(self) -> compressed:
        # primeiro temos que saber qual é o upper corner(dim)
        upper_left, bottom_right = self.dim()
        min_row,min_col = upper_left
        max_row,max_col = bottom_right
        # segundo tempo ques saber qual é o zero
        zero = self.zero
        values = []
        indexes = []
        offsets = []
        # terceiro começar a fazer a contagem dos vetores
        for x in range(max_row + 1):
            for y in range(max_col + 1):
                # Aqui seria o loop da compressao propriamente dita
                pass

    @staticmethod
    def doi(compressed_vector: compressed, pos: Position) -> float:
        #TODO: RUI
        pass

    @staticmethod
    def decompress(compressed_vector: compressed) -> MatrixSparse:
        #TODO: RUI
        pass
