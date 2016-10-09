# coding: utf-8
import pilasengine
pilas = pilasengine.iniciar()

#PERSONAJES
class Pelirrojo(pilasengine.actores.Actor):

	def iniciar(self):
		self.animacion_detenida = pilas.imagenes.cargar_grilla("imagenes/personajes/pelirrojo/idle/frame-1.png", 1)
		self.animacion_movimiento = pilas.imagenes.cargar_grilla("imagenes/personajes/pelirrojo/running/frame-1.png")
	
	def poner_en_movimiento(self):
		self.imagen = self.animacion_movimiento

	def poner_en_reposo(self):
		self.imagen = self.animacion_detenida

	def actualizar(self):
		self.imagen.avanzar()

		if pilas.control.izquierda:
			self.x -= 5
			self.espejado = True
		if pilas.control.derecha:
			self.x += 5 
			self.espejado = False



#OBJETOS :v
class ObjetoAleatorio(pilasengine.actores.Actor):

	def iniciar(self):
		listimg = ["auriculares", "monitor", "blueray", "cooler", "cpu", "impresora", "mic"]
		q = len(listimg)-1
		rnd = pilas.azar(0,+q)
		nameimg = listimg[rnd]
		self.imagen = "imagenes/"+nameimg+".png"




auriculares = Pelirrojo(pilas)
auriculares.escala = 0.5
auriculares.x = -240
auriculares.y = 0

blueray = ObjetoAleatorio(pilas)*5
blueray.escala = 0.1
blueray.x = pilas.azar(-220,220)
blueray.y = pilas.azar(-280,280)












pilas.ejecutar()