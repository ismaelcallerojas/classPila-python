class Pila:
    def __init__(self):
        self.pila=["Bliding","Me porto bonito","Loba","California","Hey Brother","Hello Babies","Como la flor","Lindas Chiquillas","Aun te extraño"]
    
    #1.- Añadir un nuevo Tema en la lista de reproducción
    def addNew(self, tema):
        self.pila.append(tema)
    
    #2.- Borrar todos los elementos de la lista de reproducción
    def remove(self):
        self.pila.clear()
    
    #3.- Añadir a un Tema a la pila de reproducción
    def push(self, tema):
        self.pila.insert(0, tema)
    
    #4.- Sacar el último Tema
    def last(self):
        return self.pila[1]
    
    def current(self):
        return self.pila[0]
    
    #5.- Ordenar por nombre
    def order(self):
        self.pila.sort()
    
    #6.- Eliminar a un tema específico
    def delete(self, tema):
        self.pila.remove(tema)
    
    #7.- Ver la lista de reproducción
    def show(self):
        for i in range (len(self.pila)):
            print(i,"->",self.pila[i])
    
    #8.-Puede Añadir un tema de forma directa en una 
    # posición dentro la pila sin alterar su
    # comportamiento
    def addDirect(self, tema,posicion):
        self.pila.insert(posicion, tema)


#CREAMOS EL OBJETO
reproductor=Pila()


#Menu de opciones
def menu():
    opcion=1

    while opcion!=0:
        print("╔═════════════════════════════════════╗") 
        print("║              REPRODUCTOR            ║")
        print("╠═════════════════════════════════════╣")
        print("║     [1] AÑADIR NUEVO TEMA           ║")
        print("║     [2] BORRAR LISTA                ║")
        print("║     [3] AÑADIR ARRIBA               ║")
        print("║     [4] MOSTRAR SIGUIENTE           ║")
        print("║     [5] ORDENAR LISTA               ║")
        print("║     [6] ELIMINAR TEMA               ║")
        print("║     [7] VER LISTA                   ║")
        print("║     [8] AÑADIR EN POSICIÓN          ║")
        print("║     [0] SALIR                       ║")
        print("╚═════════════════════════════════════╝")
        opcion=int(input("\t>>>  "))
        if opcion==1:
            tema=input("\tIngrese el título del tema: ")
            reproductor.addNew(tema)
        elif opcion==2:
            reproductor.remove()
        elif opcion==3:
            tema=input("\tIngrese el título del tema: ")
            reproductor.push(tema)
        elif opcion==4:
            print("\tSe esta reproduciendo ",reproductor.current(),".......")
            print("El siguiente a reproducir es", reproductor.last())
        elif opcion==5:
            reproductor.order()
            print("\t¡ Se ha ordenado correctamente !")
        elif opcion==6:
            tema=input("\tIngrese el título del tema que desea quitar de la lista: ")
            reproductor.delete(tema)
        elif opcion==7:
            print("\tLista de reproducción actual")
            reproductor.show()
        elif opcion==8:
            posicion=int(input("\tIngrese la posición en la desea ingresar el tema: "))
            tema=input("\tIngrese el título del tema: ")
            reproductor.addDirect(posicion,tema)
menu()