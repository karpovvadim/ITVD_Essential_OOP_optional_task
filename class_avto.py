class Avtomobil:
    def __init__(self, name="honda", model="accord", power=150, transmission="avtomat", drive_wheel="front",
                 color="white", price=30000):
        self._name = name
        self._model = model
        self._power = power
        self._transmission = transmission
        self._drive_wheel = drive_wheel
        self._color = color
        self._price = price

    def __str__(self):
        return 'Car(%s, %s, %s, %s, %s, %s, %s)' % (self._name, self._model, self._power, self._transmission,
                                                    self._drive_wheel, self._color, self._price)

    def __repr__(self):
        return 'Avto(%s, %s, %s, %s, %s, %s, %s)' % (self._name, self._model, self._power, self._transmission,
                                                    self._drive_wheel, self._color, self._price)


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

    def circul_car(self):
        for car in self._list_car:
            print(car)


def main():
    salon = Avtosalon()
    salon.circul_car()
    salon.__repr__()


if __name__ == "__main__":
    main()
