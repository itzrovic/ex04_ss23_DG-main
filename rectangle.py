class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def calc_area(self) -> int:
        return self._width * self._height

    def calc_perimeter(self) -> int:
        return 2 * self._width + 2 * self._height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self._width, self._height) == (other._width, other._height)
        return False

    def __hash__(self):
        return hash((self._width, self._height))


class RectangleList:
    def __init__(self):
        self._rectangles = []

    def __len__(self) -> int:
        return len(self._rectangles)

    def add(self, r: Rectangle):
        if self.includes(r):
            raise ValueError("rectangle already part of the list")
        self._rectangles.append(r)

    def remove(self, r: Rectangle):
        if not self.includes(r):
            raise ValueError("rectangle does not exist in the list")
        self._rectangles.remove(r)

    def includes(self, r) -> bool:
        return r in self._rectangles
