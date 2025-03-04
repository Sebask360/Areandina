class Persona:
    def __init__(self, identificacion, nombre):
        self.identificacion = identificacion
        self.nombre = nombre

class PersonaNatural(Persona):
    def __init__(self, identificacion, nombre):
        super().__init__(identificacion, nombre)

class PersonaJuridica(Persona):
    def __init__(self, identificacion, nombre, empresa):
        super().__init__(identificacion, nombre)
        self.empresa = empresa

class Usuario(Persona):
    def __init__(self, identificacion, nombre, tipo_persona):
        super().__init__(identificacion, nombre)
        self.tipo_persona = tipo_persona  # Puede ser PersonaNatural o PersonaJuridica
        self.cuentas = []
        self.contador_cuentas = 1
        
    def agregar_cuenta(self, cuenta):
        numero_cuenta = f"{self.identificacion}000{str(self.contador_cuentas).zfill(2)}"
        cuenta.id_cuenta = numero_cuenta
        self.cuentas.append(cuenta)
        self.contador_cuentas += 1
        return cuenta

    def mostrar_info(self):
        print(f"\n------------------------\nUsuario: \n - Nombre: {self.nombre}\n - ID: {self.identificacion}\n - Tipo: {self.tipo_persona.__class__.__name__}\n----------------------")
        for cuenta in self.cuentas:
            print(f"{type(cuenta).__name__}: \n - ID {cuenta.id_cuenta} \n - Saldo {cuenta.saldo}\n------------------------")

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
        self.titular = titular
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
    pass

class CuentaCorriente(Cuenta):
    pass

class CuentaEmpresa(Cuenta):
    pass

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
        tipo = input("Es Persona Natural (N) o Persona Jurídica (J)? ").strip().upper()
        
        if tipo == "N":
            persona = PersonaNatural(identificacion, nombre)
        elif tipo == "J":
            empresa = input("Ingrese el nombre de la empresa: ")
            persona = PersonaJuridica(identificacion, nombre, empresa)
        else:
            print("Tipo de persona no válido.")
            continue

        usuario = Usuario(identificacion, nombre, persona)
        banco.agregar_usuario(usuario)
        print("Usuario agregado con éxito.")
    
    elif opcion == "2":
        id_usuario = input("Ingrese la identificación del usuario: ")
        if id_usuario not in banco.usuarios:
            print("Usuario no encontrado.")
            continue

        tipo_cuenta = input("Ingrese el tipo de cuenta (Ahorro/Corriente/Empresa): ")
        saldo_inicial = float(input("Ingrese el saldo inicial: "))
        
        usuario = banco.usuarios[id_usuario]
        id_cuenta = f"{usuario.identificacion}000{str(usuario.contador_cuentas).zfill(2)}"

        if tipo_cuenta.lower() == "ahorro":
            cuenta = CuentaAhorro(id_cuenta, banco.usuarios[id_usuario], saldo_inicial)
        elif tipo_cuenta.lower() == "corriente":
            cuenta = CuentaCorriente(id_cuenta, banco.usuarios[id_usuario], saldo_inicial)
        elif tipo_cuenta.lower() == "empresa":
            cuenta = CuentaEmpresa(id_cuenta, banco.usuarios[id_usuario], saldo_inicial)
        else:
            print("Tipo de cuenta no válido")
            continue
        
        banco.agregar_cuenta_a_usuario(id_usuario, cuenta)
        # usuario.cuentas.append(cuenta)1
        
        # usuario.contador_cuentas += 1
    
    elif opcion == "3":
        banco.mostrar_usuarios()
    
    elif opcion == "4":
        banco.realizar_transferencia(input("ID cuenta origen: "), input("ID cuenta destino: "), float(input("Monto: ")))
    
    elif opcion == "5":
        banco.realizar_deposito(input("ID cuenta: "), float(input("Monto: ")))
    
    elif opcion == "6":
        banco.realizar_retiro(input("ID cuenta: "), float(input("Monto: ")))
    
    elif opcion == "7":
        print("Saliendo...")
        break
    
    else:
        print("Opción inválida.")
        
#03/03/2025
