class Base:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# PILA (LIFO)

class PilaEnlazada:
    def __init__(self):
        self.cima = None

    def apilar(self, dato):
        nuevo = Base(dato)
        nuevo.siguiente = self.cima
        self.cima = nuevo

    def mostrar(self):
        actual = self.cima
        elementos = []
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

    def cantidad_pares(self):
        actual = self.cima
        contador = 0
        while actual:
            if isinstance(actual.dato, int) and actual.dato % 2 == 0:
                contador += 1
            actual = actual.siguiente
        return contador

    def promedio(self):
        actual = self.cima
        suma, cantidad = 0, 0
        while actual:
            if isinstance(actual.dato, (int, float)): 
                suma += actual.dato
                cantidad += 1
            actual = actual.siguiente
        return suma / cantidad if cantidad > 0 else 0

    def ultimo(self):
        actual = self.cima
        if not actual:
            return None
        while actual.siguiente:
            actual = actual.siguiente
        return actual.dato


# COLA (FIFO)

class ColaEnlazada:
    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, dato):
        nuevo = Base(dato)
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

    def cantidad_pares(self):
        actual = self.frente
        contador = 0
        while actual:
            if isinstance(actual.dato, int) and actual.dato % 2 == 0:
                contador += 1
            actual = actual.siguiente
        return contador

    def promedio(self):
        actual = self.frente
        suma, cantidad = 0, 0
        while actual:
            if isinstance(actual.dato, (int, float)):
                suma += actual.dato
                cantidad += 1
            actual = actual.siguiente
        return suma / cantidad if cantidad > 0 else 0

    def ultimo(self):
        actual = self.frente
        if not actual:
            return None
        while actual.siguiente:
            actual = actual.siguiente
        return actual.dato

if __name__ == "__main__":
    print("=== PROGRAMA DE LISTAS ENLAZADAS ===")
    tipo = input("¿Quieres usar una Pila o una Cola? (p/c): ").lower()
    n = int(input("¿Cuántos datos quieres ingresar? "))

    if tipo == "p":
        estructura = PilaEnlazada()
        for i in range(n):
            dato = input(f"Ingrese el dato {i+1}: ")
            if dato.isdigit():
                dato = int(dato)
            else:
                try:
                    dato = float(dato)  
                except ValueError:
                    pass 
            estructura.apilar(dato)
    else:
        estructura = ColaEnlazada()
        for i in range(n):
            dato = input(f"Ingrese el dato {i+1}: ")
            if dato.isdigit():
                dato = int(dato)
            else:
                try:
                    dato = float(dato)
                except ValueError:
                    pass
            estructura.encolar(dato)

    print("\pn=== RESULTADOS ===")
    print("Los datos de la lista son:", estructura.mostrar())
    print("Cantidad de números pares:", estructura.cantidad_pares())
    print("El promedio es:", round(estructura.promedio(), 2))
    print("El último dato de la lista es:", estructura.ultimo())