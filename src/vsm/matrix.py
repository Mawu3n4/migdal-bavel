from vsm.vector import Vector


class Matrix(list):
    def __init__(self, vectors=None, x=None, y=None):
        if vectors:
            self.vectors = Vector([Vector(vector) for vector in vectors])
        elif x is not None and y is not None:
            self.vectors = Vector([Vector([0]*x) for i in range(y)])
        else:
            self.vectors = Vector([Vector([0])])
        super().__init__(self.vectors)

    def lencol(self):
        return len(self[0])

    def lenrow(self):
        return len(self)

    def __mul__(self, operand):
        type_ = type(operand).__name__

        if type_ == 'Matrix':
            if operand.lenrow() != self.lencol():
                print("Can not multiply matrixs of different lengths")
                return self

            res = Matrix(x=operand.lencol(), y=self.lenrow())
            for y in range(self.lenrow()):
                for x in range(operand.lencol()):
                    res[y][x] = sum(self[y][i] * operand[i][x] for i in range(operand.lenrow()))

            return res

    def normalize(self, norm):
        return Matrix(vectors=[vec.normalize(norm) for vec in self.vectors])
