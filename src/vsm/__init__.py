import math

__all__ = ['matrix', 'vector']

from vsm.matrix import Matrix
from vsm.vector import Vector


def l2_norm(v):
    return math.sqrt(sum(map(lambda x: x*x, v)))
