class Shape:
    """
    Класс, представляющий фигуру.

    Атрибуты:
        color (str): Цвет фигуры.
    """

    def __init__(self, color: str) -> None:
        """
        Конструктор класса Shape.

        Args:
            color (str): Цвет фигуры.
        """
        self.color = color

    def area(self):
        """
        Метод для вычисления площади фигуры. 
        """
        pass

class Rectangle(Shape):
    """
    Класс, представляющий прямоугольник. Наследуется от класса Shape.

    Атрибуты:
        width (int): Ширина прямоугольника.
        height (int): Высота прямоугольника.
    """

    def __init__(self, color: str, width: int, height: int) -> None:
        """
        Конструктор класса Rectangle.

        Args:
            color (str): Цвет прямоугольника.
            width (int): Ширина прямоугольника.
            height (int): Высота прямоугольника.
        """
        super().__init__(color)  # Вызов конструктора родительского класса
        self.width = width
        self.height = height

    def area(self):
        """
        Метод для вычисления площади прямоугольника.

        Returns:
            int: Площадь прямоугольника (ширина * высота).
        """
        return self.width * self.height

    def perimeter(self):
        """
        Метод для вычисления периметра прямоугольника.

        Returns:
            int: Периметр прямоугольника (2 * (ширина + высота)).
        """
        return 2 * (self.width + self.height)

# Создаем объект прямоугольника
rect = Rectangle("Red", 50, 30)

# Выводим информацию о прямоугольнике
print(f"Цвет прямоугольника: {rect.color}")
print(f"Площадь прямоугольника: {rect.area()}")
print(f"Периметр прямоугольника: {rect.perimeter()}")
