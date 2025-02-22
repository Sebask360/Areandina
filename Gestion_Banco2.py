class Usuario:
    def __init__(self, identificacion, nombre):
        self.identificacion = identificacion
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def mostrar_info(self):
        print(f"Usuario: {self.nombre} (ID: {self.identificacion})")
        for cuenta in self.cuentas:
            print(f"  - Cuenta {type(cuenta).__name__}: Saldo {cuenta.saldo}")

class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = {}

    def agregar_usuario(self, usuario):
        self.usuarios[usuario.identificacion] = usuario

    def agregar_cuenta_a_usuario(self, id_usuario, cuenta):
        if id_usuario in self.usuarios:
            self.usuarios[id_usuario].agregar_cuenta(cuenta)
            print("Cuenta agregada con éxito.")
        else:
            print("Usuario no encontrado.")

    def mostrar_usuarios(self):
        for usuario in self.usuarios.values():
            usuario.mostrar_info()

    def realizar_transferencia(self, id_origen, id_destino, monto):
        cuenta_origen = None
        cuenta_destino = None
        
        for usuario in self.usuarios.values():
            for cuenta in usuario.cuentas:
                if cuenta.id_cuenta == id_origen:
                    cuenta_origen = cuenta
                if cuenta.id_cuenta == id_destino:
                    cuenta_destino = cuenta
        
        if cuenta_origen and cuenta_destino:
            if cuenta_origen.saldo >= monto:
                cuenta_origen.retirar(monto)
                cuenta_destino.depositar(monto)
                print("Transferencia realizada con éxito.")
            else:
                print("Fondos insuficientes para la transferencia.")
        else:
            print("Una o ambas cuentas no fueron encontradas.")

    def realizar_deposito(self, id_cuenta, monto):
        for usuario in self.usuarios.values():
            for cuenta in usuario.cuentas:
                if cuenta.id_cuenta == id_cuenta:
                    cuenta.depositar(monto)
                    return
        print("Cuenta no encontrada.")

    def realizar_retiro(self, id_cuenta, monto):
        for usuario in self.usuarios.values():
            for cuenta in usuario.cuentas:
                if cuenta.id_cuenta == id_cuenta:
                    cuenta.retirar(monto)
                    return
        print("Cuenta no encontrada.")

class Cuenta:
    def __init__(self, id_cuenta, titular, saldo=0.0):
        self.id_cuenta = id_cuenta
        self.titular = titular  # Puede ser PersonaNatural o PersonaJuridica
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito de {monto} realizado. Nuevo saldo: {self.saldo}")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de {monto} realizado. Nuevo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente")

class CuentaAhorro(Cuenta):
    def __init__(self, id_cuenta, titular, saldo=0.0, tasa_interes=0.02):
        super().__init__(id_cuenta, titular, saldo)
        self.tasa_interes = tasa_interes
        self.retiros_permitidos = 3

    def aplicar_interes(self):
        self.saldo += self.saldo * self.tasa_interes
        print(f"Interés aplicado. Nuevo saldo: {self.saldo}")

    def retirar(self, monto):
        if self.retiros_permitidos > 0:
            super().retirar(monto)
            self.retiros_permitidos -= 1
        else:
            print("Has alcanzado el límite de retiros mensuales")

class CuentaCorriente(Cuenta):
    def __init__(self, id_cuenta, titular, saldo=0.0, limite_sobregiro=500):
        super().__init__(id_cuenta, titular, saldo)
        self.limite_sobregiro = limite_sobregiro

    def retirar(self, monto):
        if monto <= self.saldo + self.limite_sobregiro:
            self.saldo -= monto
            print(f"Retiro de {monto} realizado. Nuevo saldo: {self.saldo}")
        else:
            print("Fondos insuficientes, incluso con sobregiro")

class CuentaEmpresa(Cuenta):
    def __init__(self, id_cuenta, titular, saldo=0.0, credito_disponible=10000):
        super().__init__(id_cuenta, titular, saldo)
        self.credito_disponible = credito_disponible

    def solicitar_credito(self, monto):
        if monto <= self.credito_disponible:
            self.saldo += monto
            self.credito_disponible -= monto
            print(f"Crédito de {monto} aprobado. Nuevo saldo: {self.saldo}")
        else:
            print("Monto del crédito excede el límite disponible")

# Menú principal de gestión bancaria
banco = Banco("Banco Central")

while True:
    print("\n--- Menú de Gestión Bancaria ---")
    print("1. Agregar usuario")
    print("2. Agregar cuenta a un usuario")
    print("3. Mostrar información de usuarios")
    print("4. Realizar transferencia")
    print("5. Realizar depósito")
    print("6. Realizar retiro")
    print("7. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        identificacion = input("Ingrese la identificación del usuario: ")
        nombre = input("Ingrese el nombre del usuario: ")
        usuario = Usuario(identificacion, nombre)
        banco.agregar_usuario(usuario)
        print("Usuario agregado con éxito.")
    
    elif opcion == "2":
        id_usuario = input("Ingrese la identificación del usuario: ")
        tipo_cuenta = input("Ingrese el tipo de cuenta (Ahorro/Corriente/Empresa): ")
        saldo_inicial = float(input("Ingrese el saldo inicial: "))
        if tipo_cuenta.lower() == "ahorro":
            cuenta = CuentaAhorro(id_usuario, id_usuario, saldo_inicial)
        elif tipo_cuenta.lower() == "corriente":
            cuenta = CuentaCorriente(id_usuario, id_usuario, saldo_inicial)
        elif tipo_cuenta.lower() == "empresa":
            cuenta = CuentaEmpresa(id_usuario, id_usuario, saldo_inicial)
        else:
            print("Tipo de cuenta no válido")
            continue
        banco.agregar_cuenta_a_usuario(id_usuario, cuenta)
    
    elif opcion == "3":
        banco.mostrar_usuarios()
    
    elif opcion == "4":
        id_origen = input("Ingrese el ID de la cuenta origen: ")
        id_destino = input("Ingrese el ID de la cuenta destino: ")
        monto = float(input("Ingrese el monto a transferir: "))
        banco.realizar_transferencia(id_origen, id_destino, monto)
    
    elif opcion == "5":
        banco.realizar_deposito(input("Ingrese el ID de la cuenta: "), float(input("Ingrese el monto a depositar: ")))
    
    elif opcion == "6":
        banco.realizar_retiro(input("Ingrese el ID de la cuenta: "), float(input("Ingrese el monto a retirar: ")))
    
    elif opcion == "7":
        print("Saliendo del sistema...")
        break
    
    else:
        print("Opción inválida, intente de nuevo.")