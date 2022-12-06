from math import pi

class Circulo:
    
    def __init__(self, radio):
        self.radio = radio
        
    def area(self, ):
        return round(pi * self.radio ** 2, 2)
    
    def perimetro(self, ):
        return round(pi * self.radio * 2, 2)