class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def calc_perimeter(self) -> int:
        return 2 * self._width + 2 * self._height
