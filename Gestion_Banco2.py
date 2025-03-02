class Persona:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

class PersonaNatural(Persona):
    def __init__(self, nombre, identificacion, edad):
        super().__init__(nombre, identificacion)
        self.edad = edad

class PersonaJuridica(Persona):
    def __init__(self, nombre, identificacion, razon_social):
        super().__init__(nombre, identificacion)
        self.razon_social = razon_social

class Usuario(Persona):
    def __init__(self, nombre, identificacion):
        super().__init__(nombre, identificacion)
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def obtener_cuenta(self, numero_cuenta):
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                return cuenta
        return None

class Cuenta:
    def __init__(self, numero_cuenta, titular, saldo=0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("Cantidad inválida para depósito.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

class Banco:
    def __init__(self):
        self.usuarios = {}
        self.contador_cuentas = 1000  # Número de cuenta inicial

    def registrar_usuario(self, nombre, identificacion):
        if identificacion not in self.usuarios:
            self.usuarios[identificacion] = Usuario(nombre, identificacion)
            print(f"Usuario {nombre} registrado correctamente.")
        else:
            print("El usuario ya existe.")

    def crear_cuenta(self, identificacion):
        if identificacion in self.usuarios:
            usuario = self.usuarios[identificacion]
            cuenta = Cuenta(self.contador_cuentas, usuario.nombre)
            usuario.agregar_cuenta(cuenta)
            self.contador_cuentas += 1
            print(f"Cuenta creada con éxito. Número de cuenta: {cuenta.numero_cuenta}")
        else:
            print("Usuario no registrado.")

    def mostrar_usuarios(self):
        if self.usuarios:
            print("Usuarios registrados:")
            
            for usuario in self.usuarios.values():
                print(f"Nombre: {usuario.nombre}, ID: {usuario.identificacion}")
                for cuenta in usuario.cuentas:
                    print(f"  - Cuenta N° {cuenta.numero_cuenta}, Saldo: {cuenta.saldo}")
        else:
            print("No hay usuarios registrados.")

    def realizar_transferencia(self, id_origen, num_cuenta_origen, id_destino, num_cuenta_destino, cantidad):
        if id_origen in self.usuarios and id_destino in self.usuarios:
            usuario_origen = self.usuarios[id_origen]
            usuario_destino = self.usuarios[id_destino]
            cuenta_origen = usuario_origen.obtener_cuenta(num_cuenta_origen)
            cuenta_destino = usuario_destino.obtener_cuenta(num_cuenta_destino)

            if cuenta_origen and cuenta_destino:
                if cuenta_origen.saldo >= cantidad:
                    cuenta_origen.retirar(cantidad)
                    cuenta_destino.depositar(cantidad)
                    print(f"Transferencia exitosa de {usuario_origen.nombre} a {usuario_destino.nombre} por {cantidad}.")
                else:
                    print("Fondos insuficientes para la transferencia.")
            else:
                print("Una de las cuentas no fue encontrada.")
        else:
            print("Uno o ambos usuarios no están registrados.")

# Menú de opciones
banco = Banco()
while True:
    print("\n1. Registrar usuario")
    print("2. Crear cuenta bancaria")
    print("3. Mostrar usuarios y cuentas")
    print("4. Transferencia entre cuentas")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del usuario: ")
        identificacion = input("Ingrese la identificación del usuario: ")
        banco.registrar_usuario(nombre, identificacion)
    elif opcion == "2":
        identificacion = input("Ingrese la identificación del usuario: ")
        banco.crear_cuenta(identificacion)
    elif opcion == "3":
        banco.mostrar_usuarios()
    elif opcion == "4":
        id_origen = input("Ingrese la identificación del remitente: ")
        num_cuenta_origen = int(input("Ingrese el número de cuenta del remitente: "))
        id_destino = input("Ingrese la identificación del destinatario: ")
        num_cuenta_destino = int(input("Ingrese el número de cuenta del destinatario: "))
        cantidad = float(input("Ingrese la cantidad a transferir: "))
        banco.realizar_transferencia(id_origen, num_cuenta_origen, id_destino, num_cuenta_destino, cantidad)
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida, intente de nuevo.")




#######################################
    def mostrar_info(self):
        print(f"\n------------------------\nUsuario: \n - Nombre: {self.nombre}\n - ID: {self.identificacion}\n - Tipo: {self.tipo_persona.__class__.__name__}\n----------------------")
        for cuenta in self.cuentas:
            print(f"{type(cuenta).__name__}: \n - ID {cuenta.id_cuenta} \n - Saldo {cuenta.saldo}\n------------------------")