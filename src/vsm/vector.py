

class Vector(list):
    def __init__(self, *args):
        super().__init__(*args)

    def __mul__(self, operand):
        type_ = type(operand).__name__

        if type_ == 'Vector':
            if len(operand) != len(self):
                print("Can not multiply vectors of different lengths")
                return self
            for i, coordinate in enumerate(operand):
                self[i] *= coordinate
            return self
        elif type_ == 'int':
            return [self for i in range(operand)]
        else:
            raise TypeError(
                "can't multiply sequence by non-vector, non-int of type '{}'".format(type_)
            )

    def normalize(self, norm):
        denominator = norm(self)
        return Vector([coordinate/denominator for coordinate in self])
