class Jugador:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol
        self.esta_vivo = True

    def accion_nocturna(self, objetivo=None):
        if not self.esta_vivo:
            return f"{self.nombre} está muerto."

        if self.rol == "lobo":
            if objetivo:
                objetivo.esta_vivo = False
                return f"El lobo {self.nombre} ha atacado a {objetivo.nombre}"

        elif self.rol == "vidente":
            if objetivo:
                return f"La vidente ve que {objetivo.nombre} es {objetivo.rol}"

        elif self.rol == "aldeano":
            return f" {self.nombre} duerme"

        return "Rol desconocido"