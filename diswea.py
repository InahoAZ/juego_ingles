# coding: utf-8
import pilasengine
pilas = pilasengine.iniciar()

#PERSONAJES
class Poroncho(pilasengine.actores.Actor):

	def iniciar(self):
		self.imagen = 'imagenes/personajes/poroncho/standing/frame-1.png'
            
    
                

class Pelirrojo(pilasengine.actores.Actor):

	def iniciar(self):
		self.animacion_detenida = pilas.imagenes.cargar_grilla("imagenes/personajes/pelirrojo/idle/frame-1.png", 1)
		self.animacion_movimiento = pilas.imagenes.cargar_grilla("imagenes/personajes/pelirrojo/running/grilla.png", 6)
	
	def poner_en_movimiento(self):
		self.imagen = self.animacion_movimiento

		
	def poner_en_reposo(self):
		self.imagen = self.animacion_detenida

	def actualizar(self):		
		self.poner_en_reposo()
		if pilas.control.izquierda:
			self.animacion_movimiento.avanzar(velocidad = 15)
			self.poner_en_movimiento()
			self.x -= 5
			self.espejado = True
		if pilas.control.derecha:
			self.animacion_movimiento.avanzar(velocidad = 15)
			self.poner_en_movimiento()
			self.x += 5 
			self.espejado = False
		if pilas.control.abajo:
			self.animacion_movimiento.avanzar(velocidad = 15)
			self.poner_en_movimiento()
			self.y -= 5 
			self.espejado = False
		if pilas.control.arriba:
			self.animacion_movimiento.avanzar(velocidad = 15)
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



fondo = pilas.fondos.Fondo()
fondo.imagen = 'imagenes/fondos/tech.png'


auriculares = Pelirrojo(pilas)
auriculares.escala = 0.2
auriculares.x = 0
auriculares.y = 0

objetos = ObjetoAleatorio(pilas)*4
objetos.escala = 0.2














pilas.ejecutar()