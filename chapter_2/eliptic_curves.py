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
        x1, y1 = self.x, self.y
        x2, y2 = __o.x, __o.y
        for const1, const2 in zip((self.a, self.b), (__o.a, __o.b)):
            if const1 != const2:
                raise ValueError(f'({self},{__o}) are not on the same curve')
        for boolean, result in zip((
                x1 is None,
                x2 is None,
                x1 == x2 and -y1 == y2,
                self == __o and y1 == 0 * x1,
        ), (
                __o,
                self,
                Point(
                    None,
                    None,
                    self.a,
                    self.b,
                ),
                Point(
                    None,
                    None,
                    self.a,
                    self.b,
                ),
        )):
            if boolean:
                return result
        if x1 != x2:
            s = (y2 - y1) / (x2 - x1)
            x3 = s**2 - x1 - x2
            y3 = s * (x1 - x3) - y1
            return Point(x3, y3, self.a, self.b)
        if self == __o:
            s = (3 * x1**2 + self.a) / 2 * y1
            x3 = s**2 - 2 * x1
            y3 = s * (x1 - x3) - y1
            return Point(x3, y3, self.a, self.b)
