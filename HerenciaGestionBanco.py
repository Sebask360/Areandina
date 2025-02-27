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
    def __init__(self, identificacion, nombre, tipo_persona=None):
        super().__init__(identificacion, nombre)
        self.tipo_persona = tipo_persona
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def mostrar_info(self):
        tipo = type(self.tipo_persona).__name__ if self.tipo_persona is not None else "No definido"
        print(f"Usuario: {self.nombre} (ID: {self.identificacion}) - Tipo: {tipo} ")
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

    #         cuenta.mostrar_info()
    def mostrar_usuarios(self):
        if not self.usuarios:
            print("\n---No se encontraron usuarios registrados.---")
            return
        cuentas_existentes = False
        
        for id_usuario, usuario in self.usuarios.items():
            if usuario.cuentas:
                print(f"ID: {id_usuario}, Nombre: {usuario.nombre}, Saldo: {usuario.cuenta.saldo}")
                cuentas_existentes = True
        if not cuentas_existentes:
            print(f"\nIdentidicacion: {id_usuario} \nNombre: {usuario.nombre}\nEste usuario no tiene cuentas registradas.\n")
            
        
    def realizar_transferencia(self, id_origen, id_destino, monto):
        if not self.usuarios:
            print("\n---Primero registre un usuario para continuar---")
            return
        
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
        tipo_persona = input("Ingrese el tipo de persona (Natural o Juridica): ")
        if tipo_persona.lower() == "natural":
            persona_tipo = PersonaNatural(identificacion, nombre)
        elif tipo_persona.lower() == "juridica":
            empresa = input("Ingrese el nombre de la empresa: ")
            persona_tipo = PersonaJuridica(identificacion, nombre, empresa)
        else:
            persona_tipo = None
        usuario = Usuario(identificacion, nombre, persona_tipo)
        banco.agregar_usuario(usuario)
        print("Usuario agregado con éxito.")
    
    elif opcion == "2":
        if not banco.usuarios:
            print("\n--- No existen usuarios registrados ---\n--- Registre un usuario para continuar ---")
        else: 
            id_usuario = input("Ingrese la identificación del usuario: ")
            # Se valida que el usuario exista en el banco
            if id_usuario not in banco.usuarios:
                print("Usuario no encontrado.")
                continue
            usuario = banco.usuarios[id_usuario]
            id_cuenta = input("Ingrese el ID de la cuenta: ")
            tipo_cuenta = input("Ingrese el tipo de cuenta (Ahorro/Corriente/Empresa): ")
            saldo_inicial = float(input("Ingrese el saldo inicial: "))
            if tipo_cuenta.lower() == "ahorro":
                cuenta = CuentaAhorro(id_cuenta, usuario, saldo_inicial)
            elif tipo_cuenta.lower() == "corriente":
                cuenta = CuentaCorriente(id_cuenta, usuario, saldo_inicial)
            elif tipo_cuenta.lower() == "empresa":
                cuenta = CuentaEmpresa(id_cuenta, usuario, saldo_inicial)
            else:
                print("Tipo de cuenta no válido")
                continue
            banco.agregar_cuenta_a_usuario(id_usuario, cuenta)
    
    elif opcion == "3":
        if not banco.usuarios:
            print("\n--- No existen usuarios registrados ---\n--- Registre un usuario para continuar ---")
        else:
            banco.mostrar_usuarios()
    
    elif opcion == "4":
        if not banco.usuarios:
            print("\n--- No hay usuarios registrados ---\n--- Registre un usuario para continuar ---")
        else:
            id_origen = input("Ingrese el ID de la cuenta origen: ")
            id_destino = input("Ingrese el ID de la cuenta destino: ")
            monto = float(input("Ingrese el monto a transferir: "))
            banco.realizar_transferencia(id_origen, id_destino, monto)
    
    elif opcion == "5":
        if not banco.usuarios:
            print("\n--- No existen usuarios registrados ---\n--- Registre un usuario para continuar ---")
        else: 
            id_cuenta = input("Ingrese el ID de la cuenta: ")
            monto = float(input("Ingrese el monto a depositar: "))
            banco.realizar_deposito(id_cuenta, monto)
    
    elif opcion == "6":
        if not banco.usuarios:
            print("\n--- No existen usuarios registrados ---\n--- Registre un usuario para continuar ---")
        else: 
            id_cuenta = input("Ingrese el ID de la cuenta: ")
            monto = float(input("Ingrese el monto a retirar: "))
            banco.realizar_retiro(id_cuenta, monto)
    
    elif opcion == "7":
        print("Saliendo del sistema...")
        break
    
    else:
        print("Opción inválida, intente de nuevo.")
