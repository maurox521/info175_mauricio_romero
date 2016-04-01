# -*- coding: utf-8 -*-

class Auto():
  
    def __init__(self, kilometraje=0, bencina=0, rendimiento=10 ,encendido=False):
        self.kilometraje = kilometraje
        self.bencina = bencina
        self.rendimiento = rendimiento
        self.encendido = encendido
        
    def encender(self):
        if self.encendido:
           print "Motor ya está encendido."
        else:
            self.encendido = not self.encendido

    def apagar(self):
        if not self.encendido:
           print "Motor ya está apagado."
        else:
            self.encendido = not self.encendido

    def mover(self,kilometros):
        if not self.encendido:
            print "Motor apagado."
        elif self.bencina*self.rendimiento <= kilometros:
            print "Bencina insuficiente"
        else:
            print "sumaremos kilometraje y quitaremos bencina  "
            self.kilometraje += kilometros
            print self.kilometraje
            self.bencina -=  kilometros/self.rendimiento
            print self.bencina
            
    def obtener_kilometraje(self):
        print self.kilometraje

    def obtener_bencina(self):
        print self.bencina

    def cargar_bencina(self, bencina):
        if self.encendido:
            print "Primero debe apagar el motor."
        else:
            self.bencina += bencina
            
if __name__=="__main__":
    print ("***Comenzemos***")
    a = Auto()
    a.encender()
    a.cargar_bencina(35)
    a.mover(45)
    a.apagar()
    a.cargar_bencina(35)
    a.obtener_bencina()
    a.encender()
    a.mover(5)
    a.obtener_kilometraje()
    a.mover(100)
    a.apagar()

#camion

class camion (Auto):
    def __init__(self, peso=float, ruedas=int, acoplado=""):
        self.peso=peso
        self.ruedas=ruedas
        self.acoplado=acoplado
        
    
    def agregar_acoplado(self):
        
    def quitar_acoplado(self):
        
    def obtener_acoplado(self):
        
    def obtener_ruedas(self):
        
    def obtener_peso(self):
