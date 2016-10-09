import pilasengine
pilas = pilasengine.iniciar()

#impresora = pilas.actores.Actor()
#impresora.imagen = "imagenes/personajes/pelirrojo/running/grilla.jpg"
#impresora.escala = 0.2

grilla = pilas.imagenes.cargar_grilla("imagenes/personajes/pelirrojo/running/grilla.png", 6)
p = grilla.avanzar()
p.escala = 0.2