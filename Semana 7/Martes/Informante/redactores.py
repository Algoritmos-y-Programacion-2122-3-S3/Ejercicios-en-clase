import random

class Empleado:
    def __init__(self,nombre,cedula,seccion):
        self.nombre = nombre
        self.cedula = cedula
        self.seccion = seccion

class Redactor(Empleado):

    def __init__(self,nombre,cedula,seccion):
        super().__init__(nombre,cedula,seccion)

    def escribir_articulo():
        print("Articulo Escrito")

class RedactorJefe(Empleado):

    def __init__(self,nombre,cedula,seccion,redactores):
        Empleado.__init__(nombre,cedula,seccion)
        self.redactores = list(redactores)

    def decidir_si_se_publica():
        rand = random.randint(0,1)
        if rand: 
            return True
        else:
            return False
    