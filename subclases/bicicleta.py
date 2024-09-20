from superclases.vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        if tipo.lower() not in ['urbana', 'deportiva']:
            raise ValueError("El tipo de bicicleta debe ser 'urbana' o 'deportiva'")
        self.tipo = tipo
    def __str__(self):
        return super().__str__() + ", tipo {}".format(self.tipo)
