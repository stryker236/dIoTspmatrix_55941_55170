from __future__ import annotations

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
        for key in self:
            aux[key] = self[key]
        print("retornando uma cópia da matriz")
        return aux

    def __eq__(self, other: MatrixSparseDOK):
        if isinstance(other,MatrixSparseDOK):
            return self._items == other._items

    # Cria objeto iteravel
    def __iter__(self):
        self.current_index = 0
        self.max = len(self._items)
        self.iter_aux = sorted(list(self._items))
        # Não sei se retornar o proprio objeto é a melhor forma de lidar
        # return self._items.items()
        return self


    # Próximo elemento do iterador
    def __next__(self):
        if(self.current_index < self.max):
            # print("Current iteration value: ", self.current_index)
            key = self.iter_aux[self.current_index]
            self.current_index += 1
            return key
        else:
            raise StopIteration

    def __getitem__(self, pos: Union[Position, position]) -> float:
        if isinstance(pos,Position):
            return self._items[pos] if pos in self._items else self.zero
        if isinstance(pos,tuple) and len(pos) == 2:
             if isinstance(pos[0],int) and isinstance(pos[1],int):
                 if pos[0] >= 0 and pos[1] >= 0:
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
            for key in self:
                aux[key] += other
            return aux

    def _add_matrix(self, other: MatrixSparse) -> MatrixSparse:
        dim1 = self.dim()
        dim2 = other.dim()
        dim1_length = (dim1[1][1] - dim1[0][1]) + 1
        dim1_height = (dim1[1][0] - dim1[0][0]) + 1
        dim2_length = (dim2[1][1] - dim2[0][1]) + 1
        dim2_height = (dim2[1][0] - dim2[0][0]) + 1

        if((dim1_length == dim2_length) and (dim1_height == dim2_height) and self.zero == other.zero):
            aux = MatrixSparseDOK(self.zero)
            for x in range(dim1_height):
                for y in range(dim1_length):
                    # if (self[x + dim1[0][0], y + dim1[0][1]] == self.zero) or (other[x + dim2[0][0], y + dim2[0][1]] == other.zero):
                    #     aux[x + dim1[0][0], y + dim1[0][1]] = self[x + dim1[0][0], y + dim1[0][1]] + other[x + dim2[0][0], y + dim2[0][1]] - self.zero
                    #     # aux[x + dim2[0][0], y + dim2[0][1]] += other[x + dim2[0][0], y + dim2[0][1]] - other.zero
                    # else:
                    #     aux[x + dim1[0][0], y + dim1[0][1]] += self[x + dim1[0][0], y + dim1[0][1]]
                    #     aux[x + dim2[0][0], y + dim2[0][1]] += other[x + dim2[0][0], y + dim2[0][1]]                   
                    if (self[x + dim1[0][0], y + dim1[0][1]] == self.zero):
                        pass
                    else:
                        aux[x + dim1[0][0], y + dim1[0][1]] = self[x + dim1[0][0], y + dim1[0][1]]

                    if (other[x + dim2[0][0], y + dim2[0][1]] == other.zero):
                        pass
                    elif aux[x + dim2[0][0], y + dim2[0][1]] != other.zero:
                        aux[x + dim2[0][0], y + dim2[0][1]] += other[x + dim2[0][0], y + dim2[0][1]]
                    else:
                        print("heyyyyyy gorada")
                        aux[x + dim2[0][0], y + dim2[0][1]] = other[x + dim2[0][0], y + dim2[0][1]]



            return aux
        else:
            raise ValueError("_add_matrix() incompatible matrices")

    def _mul_number(self, other: Union[int, float]) -> Matrix:
        if isinstance(other, (int, float)):
            aux = self.__copy__()
            for key in self:
                aux[key] *= other
            return aux

    def _mul_matrix(self, other: MatrixSparse) -> MatrixSparse:
        dim1 = self.dim(self)
        dim2 = self.dim(other)
        dim1_length = (dim1[1][1] - dim1[0][1]) + 1
        dim1_height = (dim1[1][0] - dim1[0][0]) + 1
        dim2_length = (dim2[1][1] - dim2[0][1]) + 1
        dim2_height = (dim2[1][0] - dim2[0][0]) + 1
        result = MatrixSparseDOK()

        if((dim1_length != dim2_height) or (self.zero != other.zero)):
            raise ValueError
        else:
            result = MatrixSparseDOK(self.zero)
            for x in dim1_height:
                for y in dim2_length:
                    for k in dim2_height:
                        result[x + dim1[0][0]][y + dim1[0][0]] += self[x + dim1[0][0], k + dim1[0][1]] * other[k + dim1[0][0], y + dim1[0][1]]
        return result

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
            for key in self:
                if(key[0] == row):
                    aux[key] = self[key]
            return aux

    def col(self, col: int) -> Matrix:
        aux = MatrixSparseDOK(self.zero)
        if isinstance(col,int):
            for key in self:
                if(key[1] == col):
                    aux[key] = self[key]
            return aux

    def diagonal(self) -> Matrix:
        aux = MatrixSparseDOK(self.zero)
        for key in self:
            if(key[1] == key[0]):
                aux[key] = self[key]
        return aux

    @staticmethod
    def eye(size: int, unitary: float = 1.0, zero: float = 0.0) -> MatrixSparseDOK:
        pass

    def transpose(self) -> MatrixSparseDOK:
        aux = MatrixSparseDOK(self.zero)
        for key in self:
            aux[(key[1],key[0])] = self[key]
        # Não sei exatamente o retornar
        return aux 

    #depois melhorar e entender a lógica, nao esquecer row_num-min_row nos indices do offset
    def compress(self) -> compressed:
        if self.sparsity() >= 0.5:
            #Vetores declarados e outras variáveis necessarias
            values = []
            indexes = []
            rows = [] # (matrix, row_num) antes do compress algorithm
            non_null_elem = []
            
            # Encontrar upper_left_corner(dim)
            upper_left, bottom_right = self.dim()
            min_row,min_col = upper_left
            max_row,max_col = bottom_right

            #total de elem por linha
            total_elem_row = max_col-min_col + 1
            total_rows = max_row-min_row + 1
            offsets = [0]*total_rows
            print("default offset",offsets)
            print()
            
            # isolar as linhas
            rows = []
            aux = []
            for x in range(min_row,max_row+1):
                aux = []
                for y in range(min_col,max_col+1):
                    aux.append(self[Position(x,y)])
                rows.append(aux)
            print("After isolation")
            print("dim: ",(min_row,min_col),(max_row,max_col))
            print("Rows isoladas: ", rows)

            #Contar elementos por linha
            for row_num,row in enumerate(rows):
                count = 0
                for elem in row:
                    if elem != self.zero:
                        count += 1
                non_null_elem.append((row,count,row_num+min_row))
            
            
            print("Counting: ", non_null_elem)
            # ordenar por densidade
            print("Checar se rows ficou bem definido: ")
            for row in rows:
                print(row)
            print()

            rows = list(map(lambda x:(x[0],x[2]),sorted(non_null_elem, key = lambda x: x[1],reverse = True)))
            print("checkar se rows ficou bem organizado")
            for row in rows:
                print(row)
            print()
            
            # Compress algorithm
            for c,aux in enumerate(rows):#iterar por linha
                row,row_num = aux
                offset_idx = 0
                value_idx = 0
                row_elem_idx = 0
                done = False
                if bool(values):# se nao estiver vazio
                    print("nao está vazio")
                    while row_elem_idx < total_elem_row: # procurar offset certo
                        if value_idx + offset_idx < len(values): # tem que estar aqui, offset determina fim do loop
                            if (values[value_idx+offset_idx] == self.zero or row[row_elem_idx] == self.zero): # quando deles for zero/null é uma posição válida
                                value_idx += 1
                                row_elem_idx += 1
                                print("shift")
                            else: # offset
                                print("add offset")
                                value_idx = 0
                                row_elem_idx = 0
                                offset_idx += 1
                                print(offset_idx)
                        else:
                            break

                    print("check values: ", values)
                    print("check rows: ", row)
                    print("offset value: ", offset_idx)
                    for i,elem in enumerate(row):# acontece apenas se encontrar o offset certo
                        if i + offset_idx < len(values):
                            print("adicionar")
                            # indexes[i+offset_idx] = row_num if indexes[i+offset_idx] == -1 and values[i+offset_idx] != self.zero else indexes[i+offset_idx] # tem que se -1 para nao se confundir com 0
                            indexes[i+offset_idx] = row_num if elem != self.zero else indexes[i+offset_idx] # tem que se -1 para nao se confundir com 0
                            values[i+offset_idx] = elem if elem != self.zero else values[i+offset_idx]
                            # indexes = list(map(lambda x: row_num if x != self.zero else -1,row)) # tem que se -1 para nao se confundir com 0
                            # offsets[i] = offset_idx    
                        else:
                            print("adicionar")
                            indexes.append(row_num if elem != self.zero else -1)
                            values.append(elem)
                        print("indice: ",i)
                        print("count: ",c)
                        offsets[row_num-min_row] = offset_idx  
                    print("Novo loop")
                    print("offset_index: ",offset_idx)
                    print("values: ",values)
                    print("indexes: ",indexes)
                    print("offests: ",offsets)
                    print("row: ",row)
                    print()                            
                else:
                    print("está vazio: ")
                    # definir vetores value e indexes com 
                    values = row
                    indexes = list(map(lambda x: row_num if x != self.zero else -1,row)) # tem que se -1 para nao se confundir com 0
                    offsets[0] = offset_idx
                    print("Novo loop: ", row_num)
                    print("values: ",values)
                    print("indexes: ",indexes)
                    print("offests: ",offsets)
                    print("row: ",row)
                    print()
            return ((min_row,min_col), self.zero, tuple(values), tuple(indexes), tuple(offsets))
        raise ValueError("compress() dense matrix")
    @staticmethod
    def doi(compressed_vector: compressed, pos: Position) -> float:
        #TODO: RUI
        pass

    @staticmethod
    def decompress(compressed_vector: compressed) -> MatrixSparse:
        if isinstance(compressed_vector,compressed):
            upper_left, zero, values, indices, offsets = compressed_vector
            min_row,min_col = upper_left
            aux = MatrixSparseDOK(zero)
            for 

