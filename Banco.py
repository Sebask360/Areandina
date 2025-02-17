class Usuario:
    def __init__(self, identificacion, nombre):
        """Inicializa un usuario con su identificación y nombre."""
        self.identificacion = identificacion
        self.nombre = nombre
        self.cuentas = []
    
    def agregar_cuenta(self, cuenta):
        """Agrega una cuenta a la lista de cuentas del usuario."""
        self.cuentas.append(cuenta)
    
    def mostrar_info(self):
        """Muestra la información del usuario y sus cuentas."""
        print(f"Usuario: {self.nombre} (ID: {self.identificacion})")
        for cuenta in self.cuentas:
            cuenta.mostrar_info()

class Cuenta:
    def __init__(self, id_cuenta, tipo_cuenta, saldo=0.0):
        """Inicializa una cuenta bancaria con un ID, tipo y saldo inicial."""
        self.id_cuenta = id_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = saldo
    
    def mostrar_info(self):
        """Muestra la información de la cuenta."""
        print(f"Cuenta {self.tipo_cuenta} - ID: {self.id_cuenta}, Saldo: ${self.saldo:.2f}")
    
    def depositar(self, monto):
        """Realiza un depósito en la cuenta."""
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de ${monto:.2f} realizado con éxito.")
        else:
            print("El monto del depósito debe ser positivo.")
    
    def retirar(self, monto):
        """Realiza un retiro de la cuenta si hay saldo suficiente."""
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de ${monto:.2f} realizado con éxito.")
        else:
            print("Fondos insuficientes o monto inválido.")
    
class Banco:
    def __init__(self, nombre):
        """Inicializa el banco con un nombre y una lista de usuarios."""
        self.nombre = nombre
        self.usuarios = {}
    
    def agregar_usuario(self, usuario):
        """Agrega un usuario al banco."""
        self.usuarios[usuario.identificacion] = usuario
    
    def realizar_transferencia(self, id_origen, id_destino, monto):
        """Realiza una transferencia entre cuentas del banco."""
        cuenta_origen = self.encontrar_cuenta(id_origen)
        cuenta_destino = self.encontrar_cuenta(id_destino)
        
        if cuenta_origen and cuenta_destino and cuenta_origen.saldo >= monto:
            cuenta_origen.retirar(monto)
            cuenta_destino.depositar(monto)
            print("Transferencia realizada con éxito.")
        else:
            print("Error en la transferencia: cuentas no encontradas o saldo insuficiente.")
    
    def encontrar_cuenta(self, id_cuenta):
        """Busca una cuenta por ID en todos los usuarios."""
        for usuario in self.usuarios.values():
            for cuenta in usuario.cuentas:
                if cuenta.id_cuenta == id_cuenta:
                    return cuenta
        return None
    
    def mostrar_usuarios(self):
        """Muestra la información de todos los usuarios."""
        for usuario in self.usuarios.values():
            usuario.mostrar_info()
    
    def agregar_cuenta_a_usuario(self, id_usuario):
        """Permite agregar una nueva cuenta a un usuario existente."""
        usuario = self.usuarios.get(id_usuario)
        if usuario:
            id_cuenta = input("Ingrese el ID de la nueva cuenta: ")
            tipo_cuenta = input("Ingrese el tipo de cuenta (Ahorro, Corriente, Crédito): ")
            saldo = float(input("Ingrese el saldo inicial: "))
            nueva_cuenta = Cuenta(id_cuenta, tipo_cuenta, saldo)
            usuario.agregar_cuenta(nueva_cuenta)
            print("Cuenta agregada con éxito.")
        else:
            print("Usuario no encontrado.")
    
# Menú principal
banco = Banco("Banco Central")

while True:
    print("\n--- Menú de Gestión Bancaria ---")
    print("1. Agregar usuario")
    print("2. Agregar cuenta a un usuario")
    print("3. Mostrar información de usuarios")
    print("4. Realizar transferencia")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        identificacion = input("Ingrese la identificación del usuario: ")
        nombre = input("Ingrese el nombre del usuario: ")
        usuario = Usuario(identificacion, nombre)
        banco.agregar_usuario(usuario)
        print("Usuario agregado con éxito.")
    
    elif opcion == "2":
        id_usuario = input("Ingrese la identificación del usuario: ")
        banco.agregar_cuenta_a_usuario(id_usuario)
    
    elif opcion == "3":
        banco.mostrar_usuarios()
    
    elif opcion == "4":
        id_origen = input("Ingrese el ID de la cuenta origen: ")
        id_destino = input("Ingrese el ID de la cuenta destino: ")
        monto = float(input("Ingrese el monto a transferir: "))
        banco.realizar_transferencia(id_origen, id_destino, monto)
    
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    
    else:
        print("Opción inválida, intente de nuevo.")