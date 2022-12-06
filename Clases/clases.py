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
    
    def modificar_radio(self, nuevo_radio):
        try:
            self.radio = Circulo.comprobar_cero(nuevo_radio)
        except ValueError as e:
            print(f"""
            {type(e).__name__} 
            Radio: {nuevo_radio}
            No se puede modificar el radio a valor igual o menor a 0.
            """)
    
    def __mul__(self, factor):
        try:
            return Circulo(self.radio * Circulo.comprobar_cero(factor))
        except ValueError as e:
            print(f"""
            {type(e).__name__}
            Multiplicar por {factor}
            No se puede multiplicar un Círculo por un valor igual o menor a 0.
            """)
            
    def __str__(self, ):
        return f"Círculo con valor de radio {self.radio}."