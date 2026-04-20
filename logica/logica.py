from personajes.jugador import Jugador

class GestorPartida:
    def __init__(self):
        self.jugadores = []

    def anadir_jugador(self, nombre, rol):
        self.jugadores.append(Jugador(nombre, rol))

    def votacion_dia(self, nombre):
        for j in self.jugadores:
            if j.nombre == nombre and j.esta_vivo:
                j.esta_vivo = False
                return f" {nombre} ha sido eliminado"
        return "Nadie fue eliminado"

    def comprobar_victoria(self):
        lobos = sum(1 for j in self.jugadores if j.rol == "lobo" and j.esta_vivo)
        aldeanos = sum(1 for j in self.jugadores if j.esta_vivo and j.rol != "lobo")

        if lobos >= aldeanos:
            return "Victoria de los lobos"
        elif lobos == 0:
            return "Victoria de los aldeanos"
        return "La partida continúa"