from __future__ import annotations


class Position:
    _pos = tuple[int, int]

    #----"__init__"---------------------------------------------------------------------------------------------------------
    #   Creates new instance of Position from a given row and column. Verifies if arguments are float, int and non negative.
    #   Arguments: row - row of the given position; col - column of the given position.
    #-----------------------------------------------------------------------------------------------------------------------
    def __init__(self, row: int, col: int):
        if isinstance(row,(float,int)) and isinstance(col,(float,int)):
            if col >= 0 and row >= 0:
                self._pos = (row,col)
        else:
            raise ValueError

    #----"__str__"----------------------------------------------------------------------------------------------------------
    #   Represents the Position object as a string.
    #-----------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        return str(self._pos)

    #----"__repr__"---------------------------------------------------------------------------------------------------------
    #   Represents the Position object as a string.
    #-----------------------------------------------------------------------------------------------------------------------
    def __repr__(self):
        return self.__str__()

    #----"__hash__"---------------------------------------------------------------------------------------------------------
    #   Returns the Position object hash value as an integer.
    #-----------------------------------------------------------------------------------------------------------------------
    def __hash__(self):
        return hash(self._pos)

    #----"__getitem__"------------------------------------------------------------------------------------------------------
    #   Returns one of the Position object value from a given argument.
    #   Arguments: item - 0 for row return or 1 for column return.)
    #-----------------------------------------------------------------------------------------------------------------------
    def __getitem__(self, item: int) -> int:
        if isinstance(item,int):
            return self._pos[item]

    #----"__eq__"-----------------------------------------------------------------------------------------------------------
    #   Verifies if two given Positions are equal or not.
    #   Arguments: Position - Position from which to compare.
    #-----------------------------------------------------------------------------------------------------------------------
    def __eq__(self, other: Position):
        if isinstance(other,Position):
            return self._pos == other._pos
        return False
    
    #----"__lt__"-----------------------------------------------------------------------------------------------------------
    #   Verifies if the object is lesser then a given Position.
    #   Arguments: other - Position from which to compare.
    #-----------------------------------------------------------------------------------------------------------------------
    def __lt__(self,other):
        if isinstance(other,Position):
            if self[0] < other[0]:
                return True
            elif self[0] == other[0]:
                if self[1] < other[1]:
                    return True
            return False
        
