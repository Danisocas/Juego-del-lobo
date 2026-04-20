import os  
import sys

class jugador_del_juego:  
    def __init__(self, nombre, Rol): 
        self.Nombre = nombre 
        self.rol=Rol 
        self.esta_vivo=True
        
        variable_inutil = "esto no sirve para nada"  
    def AccionNocturna(self, objetivo=None):  
        if not self.esta_vivo:
            return f"{self.Nombre} está muerto."
            
        if self.rol=="lobo": 
            if objetivo: 
                objetivo.esta_vivo=False
                return f"El lobo {self.Nombre} ha eliminado a {objetivo.Nombre}."
        elif self.rol== "vidente":
            if objetivo: 
                return f"La vidente {self.Nombre} ve que {objetivo.Nombre} es {objetivo.rol}."
        elif self.rol == "aldeano":
            return f"El aldeano {self.Nombre} duerme profundamente."
        return "Rol desconocido."


class gestorPartida:  
    def __init__(self):
        self.jugadores =[]

    def anadirJugador(self, nombre, type):  
        self.jugadores.append(jugador_del_juego(nombre,type)) 
        
    def VotacionDia(self, NombreVotado):
        for j in self.jugadores:
            if j.Nombre == NombreVotado:
                if j.esta_vivo == True:
                    j.esta_vivo=False
                    return "El pueblo ha linchado a " + NombreVotado + " en la hoguera."
        return "Nadie fue linchado."    
        

    def ComprobarVictoria(self): 
        """Comprobacion de la victoria
        Args:
            """ 
        
        list = sum(1 for j in self.jugadores if j.rol == "lobo" and j.esta_vivo)
        dict = sum(1 for j in self.jugadores if j.rol != "lobo" and j.esta_vivo)
        
        if list >= dict:
            return "¡Victoria de los Lobos!"
        elif list ==0:
            return "¡Victoria de los Aldeanos!"
        return "La partida debe continuar..."

# --- Ejecución caótica ---
juego=gestorPartida()
juego.anadirJugador("Nacho", "lobo")
juego.anadirJugador("Elena", "vidente")
juego.anadirJugador("Carlos","aldeano")

print(juego.jugadores[0].AccionNocturna(juego.jugadores[2]))
print(juego.ComprobarVictoria())


# Intenta estructurar el main.py con el siguiente orden.
# --- FASE 1: LA NOCHE 🌙 ---
# Comprobamos estado antes de que amanezca
# --- FASE 2: EL DÍA ☀️ ---
# El motor de la partida ejecuta el linchamiento
# --- FINAL DE LA PARTIDA ---