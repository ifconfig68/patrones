class NaveEspacial:
    def __init__(self, tipo):
        self.tipo = tipo

    def mostrar(self):
        print(f"Dibujando nave espacial {self.tipo}")


class FabricaNaves:
    _naves = {}

    @staticmethod
    def obtener_nave(tipo):
        if tipo not in FabricaNaves._naves:
            FabricaNaves._naves[tipo] = NaveEspacial(tipo)
        return FabricaNaves._naves[tipo]


class Videojuego:
    def __init__(self):
        self.naves = []

    def agregar_nave(self, tipo, cantidad):
        for _ in range(cantidad):
            nave = FabricaNaves.obtener_nave(tipo)
            self.naves.append(nave)

    def dibujar_naves(self):
        for idx, nave in enumerate(self.naves, start=1):
            nave.mostrar()
            print(f"Nave {idx} en pantalla")


if __name__ == "__main__":
    juego = Videojuego()

    # Agregar diferentes tipos de naves
    juego.agregar_nave("Enemigo1", 3)
    juego.agregar_nave("Enemigo2", 2)
    juego.agregar_nave("Enemigo1", 1)

    # Dibujar las naves en pantalla
    juego.dibujar_naves()
