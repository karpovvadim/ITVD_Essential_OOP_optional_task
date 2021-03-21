from class_avto import Avtomobil


class Avtosalon:

    def __init__(self):
        self._list_car = list()
        honda_civic = Avtomobil("honda", "civic", 140, "manual", "front", "grey", 25000)
        honda_accord = Avtomobil()
        audi_A4 = Avtomobil("audi", "A4", 128, "manual", "front", "black", 32000)
        audi_A6 = Avtomobil("audi", "A6", 152, "avtomat", "4WD", "black", 40000)
        audi_A8 = Avtomobil("audi", "A8", 178, "avtomat", "4WD", "blue-black", 46000)
        self._list_car.append(honda_civic)
        self._list_car.append(honda_accord)
        self._list_car.append(audi_A4)
        self._list_car.append(audi_A6)
        self._list_car.append(audi_A8)

    def d(self):
        pass

    @property
    def list_car(self):
        return self._list_car
"""
    def print_car(self):
        for car in self.list_car:
            print(car._name, end="  ")
            print(car._model, end="  ")
            print(car._power, end="  ")
            print(car._transmission, end="  ")
            print(car._drive_wheel, end="  ")
            print(car._color, end="  ")
            print(car._price)
"""

def use_avto():
    salon = Avtosalon()
    #salon.print_car()
    print(salon)


if __name__ == "__mane__":
    use_avto()


