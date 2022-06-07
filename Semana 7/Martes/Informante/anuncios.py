class Anuncios:
    def __init__(self,seccion,nombre,cedula,titulo,cuerpo,clase):
        self.seccion = seccion
        self.nombre = nombre
        self.cedula = cedula
        self.titulo = titulo
        self.cuerpo = cuerpo
        self.clase = clase

class AnunciosComerciales(Anuncios):
    def __init__(self,seccion,nombre,cedula,titulo,cuerpo):
        super().__init__(seccion,nombre,cedula,titulo,cuerpo,"Comercial")


class AnunciosClasificados(Anuncios):
    def __init__(self,seccion,nombre,cedula,titulo,cuerpo,precio,fecha_publicacion,dias,tipo):
        super().__init__(seccion,nombre,cedula,titulo,cuerpo,"Claficados")
        self.precio = precio
        self.fecha_publicacion = fecha_publicacion
        self.dias = dias
        self.tipo = tipo

class AnunciosClasificadosVivienda(AnunciosClasificados):
    def __init__(self,seccion,nombre,cedula,titulo,cuerpo,precio,fecha_publicacion,dias,m2,cuartos,baños,puestos,politica_hab):
        super().__init__(seccion,nombre,cedula,titulo,cuerpo,precio,fecha_publicacion,dias,"Vivienda")
        self.m2 = m2
        self.cuartos = cuartos
        self.baños = baños
        self.puestos = puestos
        self.politica_hab = politica_hab

class AnunciosClasificadosVehiculo(AnunciosClasificados):
    def __init__(self,seccion,nombre,cedula,titulo,cuerpo,precio,fecha_publicacion,dias,marca,modelo,año,color,km):
        super().__init__(seccion,nombre,cedula,titulo,cuerpo,precio,fecha_publicacion,dias,"Vehiculo")
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color 
        self.km = km
