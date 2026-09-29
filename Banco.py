lista = [
    # 1. Corriente válida (tus datos base)
    {"titular": "simon navarro", "numero_cuenta": 10021822, "saldo_inicial": 120000, "tipo": "corriente", "limite_giro": ""},
    
    # 2. Ahorro con error de saldo negativo (debe lanzar ValueError y ser descartada)
    {"titular": " aNTONELLa blanc", "numero_cuenta": 10067676, "saldo_inicial": 540000, "tipo": "ahorro", "tasa_interes": 0.7},
    
    # 3. Ahorro válida con nombre desordenado y espacios (debe limpiar a "Maria Jose Perez")
    {"titular": "   mArIA joSe pErez   ", "numero_cuenta": 10034567, "saldo_inicial": 50000, "tipo": " Ahorro ", "tasa_interes": 0.3},
    
    # 4. Cuenta duplicada (mismo número que la 1, debe saltarse con tu 'continue')
    {"titular": "Pedro Castillo", "numero_cuenta": "10021822", "saldo_inicial": 10000, "tipo": "corriente", "limite_giro": 50000},
    
    # 5. Falta campo obligatorio 'titular' (debe descartarse por KeyError)
    {"numero_cuenta": 10045678, "saldo_inicial": 20000, "tipo": "ahorro"},
    
    # 6. Falta campo obligatorio 'numero_cuenta' (debe descartarse por KeyError)
    {"titular": "Luis Silva", "saldo_inicial": 30000, "tipo": "corriente"},
    
    # 7. Tipo de cuenta inválido (debe lanzar ValueError por no ser ahorro ni corriente)
    {"titular": "Ana Gomez", "numero_cuenta": 10056789, "saldo_inicial": 40000, "tipo": "vista"},
    
    # 8. Saldo inicial como texto no numérico (debe lanzar ValueError al convertir a int)
    {"titular": "Carlos Ruiz", "numero_cuenta": 10067890, "saldo_inicial": "cien mil", "tipo": "corriente"},
    
    # 9. Ahorro sin tasa_interes (tu código le asignará 0.5 por defecto)
    {"titular": "Laura Soto", "numero_cuenta": 10078901, "saldo_inicial": 80000, "tipo": "ahorro"},
    
    # 10. Corriente sin limite_giro (tu código le asignará 100000 por defecto)
    {"titular": "Diego Vega", "numero_cuenta": 10089012, "saldo_inicial": 150000, "tipo": "corriente"},
    
    # 11. Ahorro con tasa de interés negativa (tu código le asignará 0.5 por defecto)
    {"titular": "Sofia Castro", "numero_cuenta": 10090123, "saldo_inicial": 60000, "tipo": "ahorro", "tasa_interes": -0.2},
    
    # 12. Corriente con limite_giro de texto (tu código le asignará 100000 por defecto)
    {"titular": "Jorge Toro", "numero_cuenta": 10011234, "saldo_inicial": 75000, "tipo": "corriente", "limite_giro": "ilimitado"},
    
    # 13. Número de cuenta como string con espacios (debe convertirse a int correctamente)
    {"titular": "Camila Diaz", "numero_cuenta": " 10022345 ", "saldo_inicial": 90000, "tipo": "ahorro", "tasa_interes": "0.6"},
    
    # 14. Corriente válida con atributos numéricos correctos
    {"titular": "Matias Lopez", "numero_cuenta": 10033456, "saldo_inicial": 300000, "tipo": "corriente", "limite_giro": 500000},
    
    # 15. Ahorro válida con saldo inicial 0
    {"titular": "Valentina Mora", "numero_cuenta": 10044567, "saldo_inicial": 0, "tipo": "ahorro", "tasa_interes": 0.4},
    
    # 16. Tipo de cuenta en mayúsculas (debe procesarse a minúsculas)
    {"titular": "Rodrigo Pino", "numero_cuenta": 10055678, "saldo_inicial": 45000, "tipo": "CORRIENTE", "limite_giro": 200000},
    
    # 17. Duplicado del registro 14 (debe descartarse)
    {"titular": "Matias Lopez Clon", "numero_cuenta": 10033456, "saldo_inicial": 50000, "tipo": "ahorro"},
    
    # 18. Ahorro con tasa_interes como string convertible
    {"titular": "Fernanda Rios", "numero_cuenta": 10066789, "saldo_inicial": 12000, "tipo": "ahorro", "tasa_interes": "0.8"},
    
    # 19. Saldo inicial negativo (debe lanzar ValueError)
    {"titular": "Esteban Paredes", "numero_cuenta": 10077890, "saldo_inicial": -10000, "tipo": "corriente"},
    
    # 20. Corriente válida final
    {"titular": "Isidora Blanco", "numero_cuenta": 10088901, "saldo_inicial": 250000, "tipo": "corriente", "limite_giro": 150000}
]

def preprocesar_cuentas(lista):

    lista_validaciones = []
    lista_procesadas = []

    for i in lista:

        try:

            #Extraccion de datos del diccionario    
            nombre_titular = (i["titular"])
            numero_de_cuenta = (i["numero_cuenta"])
            saldo_inicial = (i["saldo_inicial"])
            tipo_cuenta = (i["tipo"])

            #Procesamiento del nombre del titular
            nombre_procesado = nombre_titular.strip()
            nombre_procesado = nombre_procesado.title()

            numero_de_cuenta = int(numero_de_cuenta)

            #Procesamiento del numero de cuenta
            if numero_de_cuenta in lista_validaciones:
                continue
            lista_validaciones.append(numero_de_cuenta)

            #Procesamiento del saldo incial
            saldo_inicial = int(saldo_inicial)

            if saldo_inicial < 0:
                raise ValueError("Saldo negativo")
                
            #Procesamiento del tipo de cuenta
            tipo_cuenta = tipo_cuenta.strip()
            tipo_cuenta = tipo_cuenta.lower()

            if tipo_cuenta != "ahorro" and tipo_cuenta != "corriente":
                raise ValueError("Tipo Invalido")

            diccionario_validado = {"titular": nombre_procesado, "numero_cuenta": numero_de_cuenta, "saldo_inicial": saldo_inicial, "tipo": tipo_cuenta}

            if tipo_cuenta == "ahorro":

                valor_tasa = i.get("tasa_interes")
                try: 
                    valor_tasa = float(valor_tasa)
                    if valor_tasa < 0:
                        valor_tasa = 0.5

                except (TypeError, ValueError):
                    valor_tasa = 0.5

                diccionario_validado["tasa_interes"] = valor_tasa


            elif tipo_cuenta == "corriente":

                valor_limite = i.get("limite_giro")
                try:
                    valor_limite = int(valor_limite)
                    if valor_limite < 0:
                        valor_limite = 100000
                except (TypeError, ValueError):
                    valor_limite = 100000

                diccionario_validado["limite_giro"] = valor_limite

            lista_procesadas.append(diccionario_validado)

        except ValueError as error:
            print(f"Se produjo un error de {error}")

        except KeyError as error:
            print(f"Se produjo un error de tipo {error}")

    return lista_procesadas

class Cuenta():
    def __init__(self, titular, numero_cuenta):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.__saldo = 0
        self.tipo_cuenta = ""


    def consultar_saldo(self):

        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo = self.__saldo + monto
        else:
            raise ValueError("Ingreso de monto a depositar no valido.")

        return self.__saldo

    def obtener_informacion_basica(self):
        return f"Titular: {self.titular} \n Numero de cuenta: {self.numero_cuenta} \n Tipo de cuenta: {self.tipo_cuenta} \n Saldo disponible: {self.__saldo}"

    def girar(self, monto):
        if monto > 0 and monto <= self.__saldo:
            self.__saldo = self.__saldo - monto
        if monto > 0 and monto > self.__saldo:
            raise ValueError("El monto supera el saldo disponible.")
        if monto < 0:
            raise ValueError("El monto debe ser mayor a 0.")

class CuentaDeAhorro(Cuenta):
    def __init__(self, titular, numero_cuenta, tasa_interes):
        super().__init__(titular, numero_cuenta)
        self.tasa_interes = tasa_interes
        self.tipo_cuenta = "ahorro"

    def aplicar_interes(self):
        saldo_actual = self.consultar_saldo()
        ganancia = saldo_actual * self.tasa_interes
        self.depositar(ganancia)

    def obtener_informacion_basica(self):
        return f"Titular: {self.titular} \n Numero de cuenta: {self.numero_cuenta} \n Tipo de cuenta: {self.tipo_cuenta} \n Saldo disponible: {self.consultar_saldo()} \n Tasa de interes: {self.tasa_interes}"

class CuentaCorriente(Cuenta):
    def __init__(self, titular, numero_cuenta, limite_giro):
        super().__init__(titular, numero_cuenta)
        self.limite_giro = limite_giro
        self.tipo_cuenta = "corriente"

    def girar(self, monto):
        saldo_actual = self.consultar_saldo()

        if monto <= 0:
            raise ValueError("El monto debe ser mayor a 0.")

        if monto > (saldo_actual + self.limite_giro):
            raise ValueError("El monto supera el saldo disponible y el límite de giro.")
            
        self._Cuenta__saldo = saldo_actual - monto
        return self._Cuenta__saldo

    def obtener_informacion_basica(self):
        return f"Titular: {self.titular} \n Numero de cuenta: {self.numero_cuenta} \n Tipo de cuenta: {self.tipo_cuenta} \n Saldo disponible: {self.consultar_saldo()} \n Limite de giro: {self.limite_giro}"

class Banco():
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []

    def abrir_cuenta(self, cuenta):
        for a in self.cuentas:
            if a.numero_cuenta == cuenta.numero_cuenta:
                print("Ya se encuentra una cuenta con ese numero.")
                return
            
        self.cuentas.append(cuenta)

    def buscar_cuenta(self, numero_cuenta):
        for b in self.cuentas:
            if b.numero_cuenta == numero_cuenta:
                return b  
                
        print("Cuenta no encontrada")
        return None

    def transferir(self, numero_origen, numero_destino, monto):
        cuenta_origen = self.buscar_cuenta(numero_origen)
        cuenta_destino = self.buscar_cuenta(numero_destino)

        if cuenta_origen is None or cuenta_destino is None:
            return
        
        if numero_origen == numero_destino:
            print("No se puede transferir a la cuenta de origen.")
            return

        try:
            cuenta_origen.girar(monto)
            cuenta_destino.depositar(monto)

        except ValueError as e:
            print(e)
        
    def mostrar_cuentas(self):
        # Creamos una función normal que solo devuelve el número de la cuenta
        def obtener_numero(cuenta):
            return cuenta.numero_cuenta
            
        # Ordenamos usando nuestra función normal
        cuentas_ordenadas = sorted(self.cuentas, key=obtener_numero)
        
        for cuenta in cuentas_ordenadas:
            print(cuenta.obtener_informacion_basica())
            print("-" * 30)

# === SCRIPT DE SIMULACIÓN FINAL ===

# 1. Procesar la lista (Asegúrate de expandir tu variable 'lista' arriba hasta 20 registros)
cuentas_validadas = preprocesar_cuentas(lista)

# 2. Crear el objeto Banco
banco_umag = Banco("Banco Simon")

# 3. Crear las cuentas dinámicamente y agregarlas al banco
for dato in cuentas_validadas:
    if dato["tipo"] == "ahorro":
        nueva_cuenta = CuentaDeAhorro(dato["titular"], dato["numero_cuenta"], dato["tasa_interes"])
    elif dato["tipo"] == "corriente":
        nueva_cuenta = CuentaCorriente(dato["titular"], dato["numero_cuenta"], dato["limite_giro"])
    
    # Inyectamos el saldo inicial usando el método oficial
    if dato["saldo_inicial"] > 0:
        nueva_cuenta.depositar(dato["saldo_inicial"])
        
    # Abrimos la cuenta en el banco
    banco_umag.abrir_cuenta(nueva_cuenta)

# 4. Probar los métodos por consola
print("--- ESTADO INICIAL DEL BANCO ---")
banco_umag.mostrar_cuentas()

print("\n--- EJECUTANDO TRANSFERENCIA (10021822 -> 10013741) ---")
banco_umag.transferir(10021822, 10013741, 15000)
banco_umag.transferir(10021822, 10022345, 15000)

print("\n--- ESTADO FINAL DESPUÉS DE LA TRANSFERENCIA ---")
banco_umag.mostrar_cuentas()