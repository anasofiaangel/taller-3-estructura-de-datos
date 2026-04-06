# Nodo para manejar colisiones (encadenamiento)
class Nodo:
    def _init_(self, codigo, cliente, estado):
        self.codigo = codigo
        self.cliente = cliente
        self.estado = estado
        self.siguiente = None


class TablaHash:
    def _init_(self, tamaño=10):
        self.tamaño = tamaño
        self.tabla = [None] * tamaño

    # Función hash
    def hash(self, codigo):
        return sum(ord(c) for c in codigo) % self.tamaño

    # Insertar envío
    def insertar(self, codigo, cliente, estado):
        indice = self.hash(codigo)
        nuevo = Nodo(codigo, cliente, estado)

        if self.tabla[indice] is None:
            self.tabla[indice] = nuevo
        else:
            actual = self.tabla[indice]
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Buscar envío
    def buscar(self, codigo):
        indice = self.hash(codigo)
        actual = self.tabla[indice]

        while actual:
            if actual.codigo == codigo:
                return actual
            actual = actual.siguiente

        return None

    # Eliminar envío
    def eliminar(self, codigo):
        indice = self.hash(codigo)
        actual = self.tabla[indice]
        anterior = None

        while actual:
            if actual.codigo == codigo:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.tabla[indice] = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente

        return False

    # Mostrar envíos
    def mostrar(self):
        for i in range(self.tamaño):
            actual = self.tabla[i]
            print(f"Índice {i}: ", end="")
            while actual:
                print(f"[{actual.codigo}, {actual.cliente}, {actual.estado}] -> ", end="")
                actual = actual.siguiente
            print("None")