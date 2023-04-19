#Crhistopher Isram Mancilla Laure
#Métodos y Atributos

#Ejemplo1
class persona:
    edad = 27
    doctor = 'Victor'

doctor = persona()

print('La edad es: ', doctor.edad)
print('La edad es: ', getattr(doctor, 'edad'))

#Ejemplo2
class Ropa:
    def __init__(self):
        self.marca = "willow"
        self.talla = "M"
        self.color = "Rojo"

camisa = Ropa()
print(camisa.talla)
print(camisa.marca)

#Ejemplo3
class Calculadora:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2
    
operacion = Calculadora(10, 3)
print(operacion.suma)