class  Base:
    def __init__(self, codigo, nombre, telefono, edad):
        self.dato = (codigo, nombre, telefono, edad) 
        self.siguiente = None

# PILA (LIFO)

class PilaEnlazada:
    def __init__(self):
        self.cima = None

    def apilar(self, codigo, nombre, telefono, edad):
        nuevo =  Base(codigo, nombre, telefono, edad)
        nuevo.siguiente = self.cima
        self.cima = nuevo

    def mostrar(self):
        actual = self.cima
        elementos = []
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

    def eliminar(self):
        if self.cima:
            self.cima = self.cima.siguiente

    def contar(self):
        actual = self.cima
        contador = 0
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

# COLA (FIFO)

class ColaEnlazada:
    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, codigo, nombre, telefono, edad):
        nuevo =  Base(codigo, nombre, telefono, edad)
        if self.final:
            self.final.siguiente = nuevo
        self.final = nuevo
        if not self.frente:
            self.frente = nuevo

    def mostrar(self):
        actual = self.frente
        elementos = []
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

    def eliminar(self):
        if self.frente:
            self.frente = self.frente.siguiente
            if not self.frente:
                self.final = None 

    def contar(self):
        actual = self.frente
        contador = 0
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador


if __name__ == "__main__":
    print("=== LISTA ENLAZADA DE PERSONAS ===")
    tipo = input("¿Quieres usar una Pila o una Cola? (p/c): ").lower()
    n = int(input("¿Cuántos elementos quieres ingresar? "))

    if tipo == "p":
        estructura = PilaEnlazada()
        for i in range(n):
            print(f"\n--- Persona {i+1} ---")
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            edad = input("Edad: ")
            estructura.apilar(codigo, nombre, telefono, edad)
    else:
        estructura = ColaEnlazada()
        for i in range(n):
            print(f"\n--- Persona {i+1} ---")
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            edad = input("Edad: ")
            estructura.encolar(codigo, nombre, telefono, edad)

    print("\n=== RESULTADOS ===")
    print("Los elementos de la lista son:")
    print(estructura.mostrar())

    print("\nEliminando el primer elemento de la lista...")
    estructura.eliminar()
    print("Nuevos elementos de la lista:")
    print(estructura.mostrar())
    print("\nCantidad de elementos en la lista:", estructura.contar())