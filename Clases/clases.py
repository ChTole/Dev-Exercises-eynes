from math import pi

class Circulo:
    
    def comprobar_cero(numero):
        if numero <= 0:
            raise ValueError
        else:
            return numero
        
    def __init__(self, radio):
        try:
            self.radio = Circulo.comprobar_cero(radio)
        except ValueError as e:
            print(f"""
            {type(e).__name__} 
            Radio: {radio}
            No se puede crear un círculo con radio igual o menor a 0.
            """)
        
    def area(self, ):
        return round(pi * self.radio ** 2, 2)
    
    def perimetro(self, ):
        return round(pi * self.radio * 2, 2)