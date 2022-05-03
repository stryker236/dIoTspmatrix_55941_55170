from __future__ import annotations
from ctypes import Union
from MatrixSparse import *
from Position import *

matrix = dict[Position, float]


class MatrixSparseDOK(MatrixSparse):
    _items = matrix

    def __init__(self, zero: float = 0.0):
        # print(zero)
        # print(type(zero))
        if not isinstance(zero, (float, int)):
            raise ValueError("__init__() invalid arguments")
        super().__init__(zero)
        self._items = {}

    def __copy__(self):
        aux = MatrixSparseDOK(self.zero)
        for key,value in self._items.items():
            aux[key] = value
        print("retornando uma cópia da matriz")
        return aux

    def __eq__(self, other: MatrixSparseDOK):
        return self._items == other._items

    # Cria objeto iteravel
    def __iter__(self):
        self.current_index = 0
        self.max = len(self._items)
        # lista de key value pair do dicionario
        self.iter_aux = list(self._items.items())
        # Não sei se retornar o proprio objeto é a melhor forma de lidar
        return self.__copy__()

    # Próximo elemento do iterador
    def __next__(self):
        if(self.current_index < self.max):
            # print("Current iteration value: ", self.current_index)
            key,value = self.iter_aux[self.current_index]
            self.current_index += 1
            return (key,value)
        # Não sei se é suposto fazer raise
        return ()

    def __getitem__(self, pos: Union[Position, position]) -> float:

        if isinstance(pos,Position):
            return self._items[pos] if pos in self._items else self.zero
        if isinstance(pos,tuple) and len(pos) == 2:
             if isinstance(pos[0],int) and isinstance(pos[1],int):
                 if pos[0] >= 0 and pos[1] >= 0:
                    print("position")
                    return self._items[Position(pos[0],pos[1])] if Position(pos[0],pos[1]) in self._items else self.zero
        raise ValueError("__getitem__() invalid arguments")

    def __setitem__(self, pos: Union[Position, position], val: Union[int, float]):
        if isinstance(val,(float,int)) and isinstance(pos,(Position,tuple)):
            if isinstance(pos, Position):
                if val != self.zero:
                    self._items[pos] = val
                elif pos in self._items:
                    del self._items[pos]
            elif isinstance(pos, tuple) and len(pos) == 2 and isinstance(pos[0],int) and isinstance(pos[1],int) and pos[0] >= 0 and pos[1] >= 0:
                if val != self.zero:
                    self._items[Position(pos[0],pos[1])] = val
                elif Position(pos[0],pos[1]) in self._items:
                    del self._items[Position(pos[0],pos[1])]
            else:
                raise ValueError("__setitem__() invalid arguments")
        else:
            raise ValueError("__setitem__() invalid arguments")

    def __len__(self) -> int:
        return len(self._items)

    def _add_number(self, other: Union[int, float]) -> Matrix:
        if isinstance(other, (int, float)):
            aux = self.__copy__()
            for key,value in self._items.items():
                aux[key] += other
            return aux

    def _add_matrix(self, other: MatrixSparse) -> MatrixSparse:
        #TODO: Diogo
        pass

    def _mul_number(self, other: Union[int, float]) -> Matrix:
        if isinstance(other, (int, float)):
            aux = self.__copy__()
            for key in self._items:
                aux[key] *= other
            return aux

    def _mul_matrix(self, other: MatrixSparse) -> MatrixSparse:
        #TODO: DIOGO
        pass

    def dim(self) -> tuple[Position, ...]:
        # lista apenas de positions
        # tem que ser spmatrix
        # se posiçoes na matrix

        if bool(self._items):
            positions = list(self._items)
            min_row = positions[0][0]
            min_col = positions[0][1]
            max_row = positions[0][0]
            max_col = positions[0][1]
            for pos in positions:
                if pos[0] > max_row:
                    max_row = pos[0]
                if pos[0] < min_row:
                    min_row = pos[0]
                if pos[1] > max_col:
                    max_col = pos[1]
                if pos[1] < min_col:
                    min_col = pos[1]
            return (Position(min_row, min_col), Position(max_row, max_col))
        return ()
    

    def row(self, row: int) -> Matrix:
        aux = MatrixSparseDOK(self.zero)
        if isinstance(row,int):
            for key, value in self._items.items():
                if(key[0] == row):
                    aux[key] = value
            return aux

    def col(self, col: int) -> Matrix:
        aux = MatrixSparseDOK(self.zero)
        if isinstance(col,int):
            for key, value in self._items.items():
                if(key[1] == col):
                    aux[key] = value
            return aux

    def diagonal(self) -> Matrix:
        aux = MatrixSparseDOK(self.zero)
        for key, value in self._items.items():
            if(key[1] == key[0]):
                aux[key] = value
        return aux

    @staticmethod
    def eye(size: int, unitary: float = 1.0, zero: float = 0.0) -> MatrixSparseDOK:
        pass

    def transpose(self) -> MatrixSparseDOK:
        aux = MatrixSparseDOK(self.zero)
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
