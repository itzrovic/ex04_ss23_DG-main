class Rectangle:
    def __init__(self, length: int, height: int):
        self._length = length
        self._height = height

    def calc_area(self) -> int:
        return self._length * self._height

    def calc_perimeter(self) -> int:
        return 2 * self._length + 2 * self._height
