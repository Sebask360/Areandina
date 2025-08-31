class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar(self.raiz, dato)

    def _insertar(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izq is None:
                nodo.izq = Nodo(dato)
            else:
                self._insertar(nodo.izq, dato)
        else:
            if nodo.der is None:
                nodo.der = Nodo(dato)
            else:
                self._insertar(nodo.der, dato)

    # Recorrido en orden
    def en_orden(self, nodo):
        if nodo is not None:
            yield from self.en_orden(nodo.izq)
            yield nodo.dato
            yield from self.en_orden(nodo.der)

    # Nodos con dos hijos
    def nodos_dos_hijos(self, nodo):
        if nodo is not None:
            yield from self.nodos_dos_hijos(nodo.izq)
            if nodo.izq is not None and nodo.der is not None:
                yield nodo.dato
            yield from self.nodos_dos_hijos(nodo.der)

    # Nodos con al menos un hijo par (en preorden)
    def nodos_hijo_par(self, nodo):
        if nodo is not None:
            if (nodo.izq and nodo.izq.dato % 2 == 0) or (nodo.der and nodo.der.dato % 2 == 0):
                yield nodo.dato
            yield from self.nodos_hijo_par(nodo.izq)
            yield from self.nodos_hijo_par(nodo.der)

    # Suma de hijos (en preorden)
    def suma_hijos(self, nodo):
        if nodo is not None:
            suma = 0
            if nodo.izq:
                suma += nodo.izq.dato
            if nodo.der:
                suma += nodo.der.dato
            yield suma
            yield from self.suma_hijos(nodo.izq)
            yield from self.suma_hijos(nodo.der)

    # Camino hacia un nodo X
    def camino(self, dato):
        camino = []
        actual = self.raiz
        while actual:
            camino.append(actual.dato)
            if dato == actual.dato:
                return camino
            elif dato < actual.dato:
                actual = actual.izq
            else:
                actual = actual.der
        return None


# ---------- Programa principal ----------
if __name__ == "__main__":
    arbol = ArbolBinario()
    n = int(input("Ingrese la cantidad de nodos: "))
    datos = list(map(int, input("Ingrese los nodos separados por espacio: ").split()))
    
    for d in datos:
        arbol.insertar(d)

    print("\nRecorrido en orden:")
    print(*arbol.en_orden(arbol.raiz))

    print("\nLos que tienen 2 hijos:")
    print(*arbol.nodos_dos_hijos(arbol.raiz))

    print("\nLos nodos con al menos un hijo par (preorden):")
    print(*arbol.nodos_hijo_par(arbol.raiz))

    print("\nSuma de hijos (preorden):")
    print(*arbol.suma_hijos(arbol.raiz))

    buscar = int(input("\nEscriba el nodo a buscar: "))
    camino = arbol.camino(buscar)
    if camino:
        print("El camino es:", *camino)
    else:
        print("El nodo no existe")
