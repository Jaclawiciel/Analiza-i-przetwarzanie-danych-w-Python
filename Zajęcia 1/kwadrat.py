class Prostokat:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def oblicz_pole(self):
        return self.a * self.b


class Kwadrat(Prostokat):

    def __init__(self, a):
        Prostokat.__init__(self, a, a)



prostokat = Prostokat(2, 3)
kwadrat = Kwadrat(2)

print("Pole prostokata: {}".format(prostokat.oblicz_pole()))
print("Pole kwadratu: {}".format(kwadrat.oblicz_pole()))

