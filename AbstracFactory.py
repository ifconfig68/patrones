import math
#patron de familia de boejtos que se relaciona entre si

# Interfaz para la fábrica abstracta de triángulos fabricas concretas deben implementar
class TrianguloFactory: 
    def crear_triangulo(self):
        pass

# Clase base para todos los tipos de triángulos
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def tipo(self):
        pass

    def area(self):
        pass

# Implementación de la fábrica concreta para crear triángulos equiláteros
class TrianguloEquilateroFactory(TrianguloFactory):
    def crear_triangulo(self):
        return TrianguloEquilatero(5)

# Implementación de la clase concreta para triángulos equiláteros
class TrianguloEquilatero(Triangulo):
    def __init__(self, lado):
        super().__init__(lado, lado, lado)

    def tipo(self):
        return "Triángulo Equilátero"

    def area(self):
        return (math.sqrt(3) / 4) * self.lado1 ** 2

# Implementación de la fábrica concreta para crear triángulos rectángulos
class TrianguloRectanguloFactory(TrianguloFactory):
    def crear_triangulo(self):
        return TrianguloRectangulo(3, 4)

# Implementación de la clase concreta para triángulos rectángulos
class TrianguloRectangulo(Triangulo):
    def __init__(self, base, altura):
        super().__init__(base, altura, math.sqrt(base**2 + altura**2))

    def tipo(self):
        return "Triángulo Rectángulo"

    def area(self):
        return 0.5 * self.lado1 * self.lado2

# Función para crear y mostrar información sobre un triángulo
def mostrar_informacion_triangulo(triangulo):
    print("Tipo de Triángulo:", triangulo.tipo())
    print("Lados:", triangulo.lado1, triangulo.lado2, triangulo.lado3)
    print("Área:", triangulo.area())
    print()

# Crear y mostrar un triángulo equilátero
triangulo_equilatero_factory = TrianguloEquilateroFactory()
triangulo_equilatero = triangulo_equilatero_factory.crear_triangulo()
mostrar_informacion_triangulo(triangulo_equilatero)

# Crear y mostrar un triángulo rectángulo
triangulo_rectangulo_factory = TrianguloRectanguloFactory()
triangulo_rectangulo = triangulo_rectangulo_factory.crear_triangulo()
mostrar_informacion_triangulo(triangulo_rectangulo)
