class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def calc_area(self) -> int:
        return self._width * self._height

    def calc_perimeter(self) -> int:
        return 2 * self._width + 2 * self._height
