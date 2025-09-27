cola=list()
print(cola)
cola.append(1)
cola.apprend(2)
print(cola)
cola.remove(1)
print(cola)
cola.pop(0)
print(cola)
#Simular un sistema de atencion bancaria con los siguientes requerimientos:
#cada nodo tendra el nombe del cliente,la cola debe permitir agregar un cliente de acuerdo al orden de llegada debe mostrar en pantalla el orden de atencion.
class Nodo:
    def __init__(self,nombre:str)->None:
        self.nombre=nombre
        self.siguiente=[None] =None
class Banco:
    def __init__(self):
        self.primero=[None]=None
        self.final=[None]=None
        self.cantidad=0
    def encolar(self,nombre):
        nodo=Nodo(nombre) 
        if self.primero == None:
            self.primero=nodo
            self.final=nodo

            self.cantidad+=1
        else:       
            self.final.siguiente=nodo
            self.final=nodo
            self.cantidad+=1
cola=Banco()
for n in range(3):
                nombre=input("Ingrese el nombre del cliente:")
                cola.encolar(nombre)


                
