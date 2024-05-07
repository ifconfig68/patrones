from abc import ABC, abstractmethod

class Juego(ABC):
    def jugar(self):
        self.inicializar()
        self.jugar_turno()
        self.finalizar()

    @abstractmethod
    def inicializar(self):
        pass

    @abstractmethod
    def jugar_turno(self):
        pass

    @abstractmethod
    def finalizar(self):
        pass

class Ajedrez(Juego):
    def inicializar(self):
        print("Inicializando juego de Ajedrez")

    def jugar_turno(self):
        print("Jugando un turno de Ajedrez")

    def finalizar(self):
        print("Finalizando juego de Ajedrez")

class Damas(Juego):
    def inicializar(self):
        print("Inicializando juego de Damas")

    def jugar_turno(self):
        print("Jugando un turno de Damas")

    def finalizar(self):
        print("Finalizando juego de Damas")

if __name__ == "__main__":
    print("Juego de Ajedrez:")
    ajedrez = Ajedrez()
    ajedrez.jugar()

    print("\nJuego de Damas:")
    damas = Damas()
    damas.jugar()
