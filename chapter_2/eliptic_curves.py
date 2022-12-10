import dataclasses


@dataclasses.dataclass
class Point:
    x: int
    y: int
    a: int
    b: int

    def __post_init__(self):
        if self.x is None and self.y is None:
            return
        if self.y**2 != self.x**3 + self.a * self.x + self.b:
            raise ValueError(f'({self.x},{self.y}) is not on the curve')

    def __add__(self, __o):
        for const1, const2 in zip((self.a, self.b), (__o.a, __o.b)):
            if const1 != const2:
                raise ValueError(f'({self},{__o}) are not on the same curve')
        if self.x is None:
            return __o
        if __o.x is None:
            return self
        if self.x == __o.x and -self.y == __o.y:
            return Point(None, None, self.a, self.b)
