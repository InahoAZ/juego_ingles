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



class Auriculares(pilasengine.actores.Actor):

	def iniciar(self):
		self.imagen = "imagenes/auriculares.png"

	def saludar(self):
		self.decir("Hola Mundo!")

	def dar_vuelta(self):
		self.rotacion = [360]	


class Blueray(pilasengine.actores.Actor):

	def iniciar(self):
		self.imagen = "imagenes/blueray.png"

class Cooler(pilasengine.actores.Actor):

	def iniciar(self):
		self.imagen = "imagenes/cooler.png"

class Cpu(pilasengine.actores.Actor):

	def iniciar(self):
		self.imagen = "imagenes/cpu.png"

class Hdd(pilasengine.actores.Actor):

	def iniciar(self):
		self.imagen = "imagenes/hdd.png"

class Impresora(pilasengine.actores.Actor):

	def iniciar(self):
		self.imagen = "imagenes/impresora.png"

class Mic(pilasengine.actores.Actor):

	def iniciar(self):
		self.imagen = "imagenes/mic.png"

class Monitor(pilasengine.actores.Actor):

	def iniciar(self):
		self.imagen = "imagenes/monitor.png"

class Mouse(pilasengine.actores.Actor):

	def iniciar(self):
		self.imagen = "imagenes/mouse.png"

class Parlantes(pilasengine.actores.Actor):

	def iniciar(self):
		self.imagen = "imagenes/parlantes.png"

class Pendrive(pilasengine.actores.Actor):

	def iniciar(self):
		self.imagen = "imagenes/pendrive.png"

class Teclado(pilasengine.actores.Actor):

	def iniciar(self):
		self.imagen = "imagenes/teclado.png"

class VideoCard(pilasengine.actores.Actor):

	def iniciar(self):
		self.imagen = "imagenes/videocard.png"

class Webcam(pilasengine.actores.Actor):

	def iniciar(self):
		self.imagen = "imagenes/webcam.png"






auriculares = Pelirrojo(pilas)
auriculares.escala = 0.5
auriculares.x = -240
auriculares.y = 0

blueray = ObjetoAleatorio(pilas)*5
blueray.escala = 0.5
blueray.x = auriculares.x + 160
blueray.y = 0

cooler = Mouse(pilas)
cooler.escala = 0.3
cooler.x = blueray.x + 160
cooler.y = 0

cpu = Monitor(pilas)
cpu.escala = 0.1
cpu.x = cooler.x + 160
cpu.y = 0










pilas.ejecutar()