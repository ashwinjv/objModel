import numbers
import math


class Vector:

    def __init__(self, components):
        self.components = tuple(components)

    @property
    def u(self):
        return self.components[0]

    @property
    def v(self):
        return self.components[1]

    @property
    def angle(self):
        return math.atan2(self.v, self.u)
        
    def __len__(self):
        return len(self.components)

    def __str__(self):
        return str(self.components)

    def __repr__(self):
        return '{} object: {}'.format(self.__class__.__name__, self)

    def __iter__(self):
        return iter(self.components)

    # def __eq__(self, other):
    #     if len(self) != len(other):
    #         return False
    #     for i, j in zip(self, other):
    #         if i != j:
    #             return False
    #     return True

    def __eq__(self, other):
        return len(self) == len(other) and \
            all(i == j for i, j in zip(self, other))

    def __add__(self, other):
        if len(self) != len(other):
            raise NotImplemented
        return Vector([i + j for i, j in zip(self, other)])

    def __sub__(self, other):
        if len(self) != len(other):
            raise NotImplemented
        return Vector([i - j for i, j in zip(self, other)])

    def __mul__(self, number):
        if not isinstance(number, numbers.Real):
            raise NotImplemented
        return Vector([number * i for i in self])

    def __rmul__(self, number):
        return self * number

    def __abs__(self):
        return math.sqrt(sum(i * i for i in self))

    # def __getitem__(self, index):
    #     return self.components[index]

    def __getitem__(self, key):
        if isinstance(key, str):
            return getattr(self, key)
        if isinstance(key, slice):
            return self.components[key]
        if isinstance(key, numbers.Integral):
            return self.components[key]
        raise NotImplemented
