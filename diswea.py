# coding: utf-8
import pilasengine
pilas = pilasengine.iniciar()

#PERSONAJES
class Poroncho(pilasengine.actores.Actor):

	def iniciar(self):
		self.imagen = 'imagenes/personajes/poroncho/standing/frame-1.png'
            
    
                

class Pelirrojo(pilasengine.actores.Actor):

	def iniciar(self):
		self.animacion_detenida = pilas.imagenes.cargar_grilla("imagenes/personajes/pelirrojo/idle/grilla.png", 2)
		self.animacion_movimiento = pilas.imagenes.cargar_grilla("imagenes/personajes/pelirrojo/running/grilla.png", 6)
		rect = pilas.fisica.Rectangulo(0, 0, 60, 115, sensor=True, dinamica=False)
		self.figura_de_colision = rect
		
	def poner_en_movimiento(self):
		self.imagen = self.animacion_movimiento

		
	def poner_en_reposo(self):
		self.imagen = self.animacion_detenida

	def actualizar(self):		
		self.poner_en_reposo()
		self.animacion_detenida.avanzar(velocidad = 1)
		if pilas.control.izquierda:
			self.animacion_movimiento.avanzar(velocidad = 5)
			self.poner_en_movimiento()
			self.x -= 5
			self.espejado = True
		if pilas.control.derecha:
			self.animacion_movimiento.avanzar(velocidad = 5)
			self.poner_en_movimiento()
			self.x += 5 
			self.espejado = False
		if pilas.control.abajo:
			self.animacion_movimiento.avanzar(velocidad = 5)
			self.poner_en_movimiento()
			self.y -= 5 
			self.espejado = False
		if pilas.control.arriba:
			self.animacion_movimiento.avanzar(velocidad = 5)
			self.poner_en_movimiento()
			self.y += 5 
			self.espejado = False	



#OBJETOS :v
class ObjetoAleatorio(pilasengine.actores.Actor):

	def iniciar(self):
		listimg = ["auriculares", "blueray", "cooler", "cpu", "hdd", "impresora", "mic", "monitor", "mouse", "pendrive", "teclado", "videocard", "webcam"]
		q = len(listimg)-1
		rnd = pilas.azar(0,+q)
		nameimg = listimg[rnd]
		self.imagen = "imagenes/"+nameimg+".png"
		self.x = pilas.azar(-220, 220)
		self.y = pilas.azar(-280, 280)       

 	def actualizar(self):
 		a = 0

 	def cambiar_posicion(self):
 		xrand = pilas.azar(-400, 400)
		xrand2 = pilas.azar(-400, 400)
		yrand = pilas.azar(-400, 400)
		yrand2 = pilas.azar(-400, 400)
		self.x = [xrand, xrand2],5
		self.y = [yrand, yrand2],5 
		

fondo = pilas.fondos.Fondo()
fondo.imagen = 'imagenes/fondos/tech.png'


auriculares = Pelirrojo(pilas)
auriculares.escala = 0.1
auriculares.x = 0
auriculares.y = 0

objetos = ObjetoAleatorio(pilas)*8
objetos.escala = 0.2

pilas.tareas.siempre(3, objetos.cambiar_posicion)












pilas.ejecutar()