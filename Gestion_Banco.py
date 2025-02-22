class Usuario:
    def __init__(self, identificacion, nombre):
        # Inicializa un usuario con su identificación y nombre
        self.identificacion = identificacion
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        # Agrega una cuenta a la lista de cuentas del usuario
        self.cuentas.append(cuenta)

    def mostrar_info(self):
        # Muestra la información del usuario y sus cuentas
        print(f"\nUsuario: {self.nombre} (ID: {self.identificacion})")
        if not self.cuentas:
            print("Este usuario no tiene cuentas asociadas.")
        for cuenta in self.cuentas:
            cuenta.mostrar_info()


class Cuenta:
    def __init__(self, id_cuenta, tipo_cuenta, saldo=0.0):
        # Inicializa una cuenta bancaria con un ID, tipo y saldo inicial
        self.id_cuenta = id_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = saldo

    def mostrar_info(self):
        # Muestra la información de la cuenta
        print(f"Cuenta {self.tipo_cuenta} - ID: {self.id_cuenta}, Saldo: ${self.saldo:.2f}")

    def depositar(self, monto):
        # Realiza un depósito en la cuenta
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de ${monto:.2f} realizado con éxito.")
        else:
            print("El monto del depósito debe ser positivo.")

    def retirar(self, monto):
        # Realiza un retiro de la cuenta si hay saldo suficiente
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de ${monto:.2f} realizado con éxito.")
        else:
            print("Fondos insuficientes o monto inválido.")


class Banco:
    def __init__(self, nombre):
        # Inicializa el banco con un nombre y una lista de usuarios
        self.nombre = nombre
        self.usuarios = {}

    def agregar_usuario(self, usuario):
        # Agrega un usuario al banco
        self.usuarios[usuario.identificacion] = usuario

    def realizar_transferencia(self, id_origen, id_destino, monto):
        # Realiza una transferencia entre cuentas del banco
        cuenta_origen = self.encontrar_cuenta(id_origen)
        cuenta_destino = self.encontrar_cuenta(id_destino)

        if cuenta_origen and cuenta_destino and cuenta_origen.saldo >= monto:
            cuenta_origen.retirar(monto)
            cuenta_destino.depositar(monto)
            print("Transferencia realizada con éxito.")
        else:
            print("Error en la transferencia: cuentas no encontradas o saldo insuficiente.")

    def encontrar_cuenta(self, id_cuenta):
        # Busca una cuenta por ID en todos los usuarios
        for usuario in self.usuarios.values():
            for cuenta in usuario.cuentas:
                if cuenta.id_cuenta == id_cuenta:
                    return cuenta
        return None

    def mostrar_usuarios(self):
        # Muestra la información de todos los usuarios
        if not self.usuarios:
            print("No hay ningún usuario registrado. Por favor, registre usuarios primero.")
            return
        for usuario in self.usuarios.values():
            usuario.mostrar_info()

    def agregar_cuenta_a_usuario(self, id_usuario):
        # Permite agregar una nueva cuenta a un usuario existente
        usuario = self.usuarios.get(id_usuario)
        if usuario:
            tipo_cuenta = ""
            while tipo_cuenta not in ["Ahorro", "Corriente", "Crédito"]:
                tipo_cuenta = input("Ingrese el tipo de cuenta (Ahorro, Corriente, Crédito): ").capitalize()
                if tipo_cuenta not in ["Ahorro", "Corriente", "Crédito"]:
                    print("Tipo de cuenta inválido. Intente de nuevo.")

            saldo = -1
            while saldo < 0:
                try:
                    saldo = float(input("Ingrese el saldo inicial: "))
                    if saldo < 0:
                        print("El saldo no puede ser negativo.")
                except ValueError:
                    print("Entrada inválida. Ingrese un número válido.")

            id_cuenta = f"{id_usuario}-{len(usuario.cuentas) + 1}"
            nueva_cuenta = Cuenta(id_cuenta, tipo_cuenta, saldo)
            usuario.agregar_cuenta(nueva_cuenta)
            print(f"Cuenta creada con éxito. ID de cuenta: {id_cuenta}")
        else:
            print("Usuario no encontrado. Registre un usuario antes de agregar una cuenta.")

    def realizar_retiro(self, id_cuenta, monto):
        # Permite a un usuario retirar dinero de su cuenta
        cuenta = self.encontrar_cuenta(id_cuenta)
        if cuenta:
            cuenta.retirar(monto)
        else:
            print("Cuenta no encontrada.")

    def realizar_deposito(self, id_cuenta, monto):
        # Permite a un usuario depositar dinero en su cuenta
        cuenta = self.encontrar_cuenta(id_cuenta)
        if cuenta:
            cuenta.depositar(monto)
        else:
            print("Cuenta no encontrada.")