class FieldElement:
    def __init__(self, num: int, prime: int) -> None:
        if num >= prime or num < 0:
            raise ValueError(f"{num} should be in range [0,{prime})")
        self._num = num
        self._prime = prime

    @property
    def num(self) -> int:
        return self._num

    @property
    def prime(self) -> int:
        return self._prime

    def __eq__(self, __o: object) -> bool:
        if __o is None:
            return False
        return self.num == __o.num and self.prime == __o.prime

    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)

    def __add__(self, __o: object) -> object:
        if self.prime != __o.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num + __o.num) % self.prime
        return FieldElement(num, self.prime)

    def __sub__(self, __o: object) -> object:
        if self.prime != __o.prime:
            raise TypeError('Cannot sub two numbers in different Fields')
        num = (self.num - __o.num) % self.prime
        return FieldElement(num, self.prime)

    def __mul__(self, __o: object) -> object:
        if self.prime != __o.prime:
            raise TypeError('Cannot mul two numbers in different Fields')
        num = (self.num * __o.num) % self.prime
        return FieldElement(num, self.prime)

    def __pow__(self, num: int) -> object:
        return FieldElement((self.num**num) % self.prime, self.prime)
