class Persona:
    def __init__(self, identificacion, nombre):
        self.nombre = nombre
        self.identificacion = identificacion

class PersonaNatural(Persona):
    def __init__(self, identificacion, nombre, edad):
        super().__init__(identificacion, nombre)
        self.edad = edad

class PersonaJuridica(Persona):
    def __init__(self, identificacion, nombre, razon_social):
        super().__init__(identificacion, nombre)
        self.razon_social = razon_social

class Usuario(Persona):
    def __init__(self, nombre, identificacion):
        super().__init__(identificacion, nombre)
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    # def mostrar_info(self):
    #     tipo = type(self.tipo_persona).__name__ if self.tipo_persona is not None else "No definido"
    #     print(f"Usuario: {self.nombre} (ID: {self.identificacion}) - Tipo: {tipo} ")
    #     for cuenta in self.cuentas:
    #         print(f"  - Cuenta {type(cuenta).__name__}: Saldo {cuenta.saldo}")

    def obtener_cuenta(self, numero_cuenta):
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                return cuenta
        return None

class Cuenta:
    def __init__(self, numero_cuenta, titular, saldo=00):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"--- Depósito exitoso --- \nNuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor a $1.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"--- Retiro exitoso --- \nNuevo saldo: {self.saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")


class Banco:
    def __init__(self):
        self.usuarios = {}
        self.nombre = nombre
        self.contador_cuentas = 1000

    def registrar_usuario(self, nombre, identificacion):
        if identificacion not in self.usuarios:
            self.usuarios[identificacion] = Usuario(nombre, identificacion)
            print(f"Usuario {nombre} registrado correctamente")
            
        else:
            print("--- El usuario ya esta registrado ---")
            
    def crear_cuenta(self, identificacion):
        if identificacion in self.usuarios:
            usuario = self.usuarios[identificacion]
            cuenta = Cuenta(self.contador_cuentas, usuario.nombre)
            usuario.agregar_cuentas += 1
            usuario.agregar_cuenta(cuenta)
            print(f"--- Cuenta creada con exito --- \n --- Numero de cuenta: {cuenta.numero_cuenta}")
        else:
            print("--- El usuario no se pudo registrar ---")
    #         cuenta.mostrar_info()}}
    #
    
    def mostrar_usuarios(self):
        if self.usuarios:
            print("\n--- Usuarios registrados: ---")
                
            for usuario in self.usuarios.values():
                print(f" - Nombre: {usuario.nombre}\n - Identificacion: {usuario.identificacion}")
                for cuenta in usuario.cuentas:
                    print(f" - Cuenta N° {cuenta.numero_cuenta} \n - Saldo: {cuenta.saldo}")
        
            else:
                print("--- No hay usuarios registrados ---")
                
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
                    print(f"Transferencia exitosa de {usuario_origen.nombre} a {usuario_destino.nombre}. \n - Cantidad: {cantidad}.")
                else:
                    print("--- FOndos insuficientes para la transferencia ---")
            else:
                print("--- Una de las cuentas no se encontro --- ")
        else:
            print(" --- Uno o ambos usuarios no estan registrados --- ")
                    
       
    def realizar_deposito(self, identificacion, num_cuenta, cantidad):
        if identificacion in self.usuarios:
            usuario = self.usuario[identificacion]
            cuenta = usuario.obtener_cuenta(num_cuenta)
            
            if cuenta:
                    cuenta.depositar(cantidad)
            else: 
                print(" --- La cuenta no existe ---")
        else:
            print(" --- El usuario ingresado no existe ---")

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
        print("\n --- Tipo de Persona --- ")
        print("1. Persona Natural")
        print("1. Persona Juridica")
        tipo_persona = input(" --- Selecciona un tipo de persona: ---")
        
        identificacion = input("Ingrese la identificación del usuario: ")
        nombre = input("Ingrese el nombre del usuario: ")
        
        if tipo_persona == "1" or "Natural":
            edad = int(input(" - Ingresa la edad: "))
            usuario = PersonaNatural(identificacion, nombre, edad)
        elif tipo_persona == "2" or tipo_persona == "Juridica":
            razon_social = input("Ingrese la razon social")
            usuario = PersonaJuridica(identificacion, nombre, razon_social)
        else:
            print(" --- Opcion invalida --- \n --- Saliendo al menu ---")
            continue
        
        banco.usuarios[identificacion] = usuario
        print(f" --- Usuario {nombre} registrado correctamente ---")
    
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
