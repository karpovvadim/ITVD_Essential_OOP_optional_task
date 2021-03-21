
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

