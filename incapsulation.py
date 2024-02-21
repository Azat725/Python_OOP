class Car:
    """
    Класс, представляющий автомобиль.

    Attributes:
        brand (str): Марка автомобиля.
        model (str): Модель автомобиля.
        year (int): Год выпуска автомобиля.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Конструктор класса Car. Инициализирует атрибуты автомобиля.

        Args:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска автомобиля.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        

    def drive(self, distance: int) -> int:
        """
        Метод для увеличения пробега автомобиля после поездки.

        Args:
            distance (int): Расстояние, на которое проехал автомобиль.

        Returns:
            int: Новый пробег автомобиля после проезда.
        """
        self.mileage += distance
        return self.mileage
    

    def get_mileage(self) -> int:
        """
        Метод для получения текущего пробега автомобиля.

        Returns:
            int: Текущий пробег автомобиля.
        """
        return self.mileage
    

    def set_mileage(self, new_mileage: int) -> bool:
        """
        Метод для установки нового значения пробега автомобиля.

        Args:
            new_mileage (int): Новое значение пробега автомобиля.

        Returns:
            bool: True, если новый пробег установлен успешно, False в случае ошибки.
        """
        if new_mileage >= 0:
            self.mileage = new_mileage
            return True
        else:
            return False

# Создаем экземпляр класса Car
user_car = Car("BMW", "5-Series", 2020)

# Пример использования методов класса
print(f"Проехали 100 км")
print(f"Новый пробег автомобиля: {user_car.drive(100)}")

print(f"Текущий пробег автомобиля: {user_car.get_mileage()}")

print(f"Устанавливаем отрицательный пробег: -200")
if user_car.set_mileage(-200):
    print("Пробег успешно установлен.")
else:
    print("Невозможно установить отрицательный пробег.")
