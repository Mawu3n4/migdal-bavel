from vsm.vector import Vector


class Matrix(list):
    def __init__(self, vectors=None, x=None, y=None):
        if vectors:
            self.vectors = Vector([Vector(vector) for vector in vectors])
        elif x is not None and y is not None:
            self.vectors = Vector([Vector([0]*x)]*y)
        else:
            self.vectors = Vector([Vector([0])])
        super().__init__(self.vectors)

    def __mul__(self, operand):
        type_ = type(operand).__name__

        if type_ == 'Matrix':
            if len(operand) != len(self):
                print("Can not multiply matrixs of different lengths")
                return self
            for y, vector in enumerate(operand):
                for x, coordinate in enumerate(vector):
                    self[y][x] *= coordinate
            return self

    def normalize(self, norm):
        return Matrix(vectors=[vec.normalize(norm) for vec in self.vectors])
