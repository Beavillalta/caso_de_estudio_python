"""
Mi Aplicación de Seguimiento de Gastos

Esta aplicación te permite llevar un seguimiento de tus ingresos y gastos personales.
Puedes registrar nuevas transacciones, listarlas y calcular tu balance financiero.

Instrucciones de Ejecución:
1. Asegúrate de tener Python 3 instalado en tu sistema.
2. Clona este repositorio en tu máquina local.
3. Instala las dependencias necesarias ejecutando `pip install -r requirements.txt`.
4. Ejecuta la aplicación ejecutando `python main.py` desde la línea de comandos.

Ejemplos de Uso:
- Registrar una nueva transacción:
    1. Selecciona la opción "Agregar transacción" del menú.
    2. Ingresa el monto, fecha, descripción y tipo de transacción cuando se te solicite.

- Listar transacciones:
    1. Selecciona la opción "Listar transacciones" del menú.

- Calcular balance:
    1. Selecciona la opción "Calcular balance" del menú.

- Editar transacción:
    1. Selecciona la opción "Editar transacción" del menú y sigue las instrucciones.

- Eliminar transacción:
    1. Selecciona la opción "Eliminar transacción" del menú y sigue las instrucciones.

- Generar informe:
    1. Selecciona la opción "Generar informe" del menú para obtener un informe detallado sobre tus gastos e ingresos.

- Generar gráfico:
    1. Selecciona la opción "Generar gráfico" del menú para visualizar gráficamente tus gastos e ingresos.

- Autenticar usuario:
    1. Selecciona la opción "Autenticar usuario" del menú para iniciar sesión y proteger tus datos financieros.

Casos de Prueba:
- Casos de Prueba Positivos:
    1. Registrar una nueva transacción con datos válidos.
    2. Listar transacciones después de agregar algunas transacciones.
    3. Calcular balance después de agregar algunas transacciones.
    4. Editar una transacción existente.
    5. Eliminar una transacción existente.
    6. Generar un informe detallado.
    7. Generar un gráfico visual.
    8. Autenticar un usuario correctamente.

- Casos de Prueba Negativos:
    1. Intentar agregar una transacción con datos inválidos (monto no numérico, fecha inválida, etc.).
    2. Intentar listar transacciones cuando no hay transacciones registradas.
    3. Intentar cargar datos desde un archivo inexistente.
"""

from transaction import Transaction
import pickle

# Lista para almacenar las transacciones
transacciones = []

# Definición de la clase Transaction
class Transaction:
    """Representa una transacción financiera."""

    def __init__(self, amount, date, description, transaction_type):
        """Inicializa una nueva instancia de Transaction.

        Args:
            amount (float): El monto de la transacción.
            date (str): La fecha de la transacción en formato YYYY-MM-DD.
            description (str): La descripción de la transacción.
            transaction_type (str): El tipo de transacción (ingreso/gasto).
        """
        self.amount = amount
        self.date = date
        self.description = description
        self.transaction_type = transaction_type

    def __str__(self):
        """Devuelve una representación en cadena de la transacción."""
        return f"{self.date}: {self.description} ({self.amount} {self.transaction_type})"

# Funciones para agregar, listar transacciones, calcular balance, guardar y cargar datos
def agregar_transaccion():
    """Permite al usuario agregar una nueva transacción."""
    try:
        amount = float(input("Ingrese el monto de la transacción: "))
        date = input("Ingrese la fecha de la transacción (YYYY-MM-DD): ")
        description = input("Ingrese la descripción de la transacción: ")
        transaction_type = input("Ingrese el tipo de transacción (ingreso/gasto): ")

        # Validar el tipo de transacción
        if transaction_type not in ["ingreso", "gasto"]:
            raise ValueError("El tipo de transacción debe ser 'ingreso' o 'gasto'.")

        transaccion = Transaction(amount, date, description, transaction_type)
        transacciones.append(transaccion)
        print("Transacción agregada exitosamente.")
        guardar_datos()  # Llamar a la función para guardar los datos después de agregar una transacción
    except ValueError as e:
        print(f"Error: {e}. Por favor, ingrese datos válidos.")

def listar_transacciones():
    """Muestra una lista de todas las transacciones registradas."""
    if transacciones:
        print("Lista de transacciones:")
        for i, transaccion in enumerate(transacciones, start=1):
            print(f"{i}. {transaccion}")
    else:
        print("No hay transacciones registradas.")

def calcular_balance():
    """Calcula el balance financiero actual (ingresos, gastos, capacidad de ahorro)."""
    ingresos = sum(transaccion.amount for transaccion in transacciones if transaccion.transaction_type == "ingreso")
    gastos = sum(transaccion.amount for transaccion in transacciones if transaccion.transaction_type == "gasto")
    capacidad_ahorro = ingresos - gastos
    print(f"Ingresos totales: {ingresos}")
    print(f"Gastos totales: {gastos}")
    print(f"Capacidad de ahorro: {capacidad_ahorro}")

def guardar_datos():
    """Guarda la lista de transacciones en un archivo utilizando el módulo pickle."""
    try:
        with open('datos_financieros.pkl', 'wb') as archivo:
            pickle.dump(transacciones, archivo)
        print("Datos guardados correctamente.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def cargar_datos():
    """Intenta cargar los datos previos de transacciones desde un archivo utilizando pickle."""
    try:
        with open('datos_financieros.pkl', 'rb') as archivo:
            transacciones.extend(pickle.load(archivo))
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("No se encontró el archivo de datos. Inicializando en un estado vacío.")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")

# Nuevas funciones agregadas para mejorar la interfaz de usuario
def editar_transaccion():
    """Permite al usuario editar una transacción existente."""
    listar_transacciones()
    try:
        indice = int(input("Ingrese el número de la transacción que desea editar: ")) - 1
        transaccion = transacciones[indice]
        print(f"Editar transacción: {transaccion}")
        amount = float(input("Ingrese el monto de la transacción: "))
        date = input("Ingrese la fecha de la transacción (YYYY-MM-DD): ")
        description = input("Ingrese la descripción de la transacción: ")
        transaction_type = input("Ingrese el tipo de transacción (ingreso/gasto): ")

        # Validar el tipo de transacción
        if transaction_type not in ["ingreso", "gasto"]:
            raise ValueError("El tipo de transacción debe ser 'ingreso' o 'gasto'.")

        nueva_transaccion = Transaction(amount, date, description, transaction_type)
        transacciones[indice] = nueva_transaccion  # Actualizar la transacción en la lista
        print("Transacción editada exitosamente.")
        guardar_datos()  # Guardar los cambios después de editar la transacción
    except IndexError:
        print("El número de transacción ingresado no es válido.")
    except ValueError as e:
        print(f"Error: {e}. Por favor, ingrese datos válidos.")

def eliminar_transaccion():
    """Permite al usuario eliminar una transacción existente."""
    listar_transacciones()
    try:
        indice = int(input("Ingrese el número de la transacción que desea eliminar: ")) - 1
        transaccion = transacciones.pop(indice)
        print(f"Transacción eliminada: {transaccion}")
        guardar_datos()  # Guardar los cambios después de eliminar la transacción
    except IndexError:
        print("El número de transacción ingresado no es válido.")
    except ValueError:
        print("Ingrese un número válido para seleccionar la transacción.")

def generar_informe():
    """Genera un informe detallado sobre los gastos e ingresos."""
    # Aquí puedes implementar la lógica para generar el informe
    

def generar_grafico():
    """Genera un gráfico visual sobre los gastos e ingresos."""
    # Aquí puedes implementar la lógica para generar el gráfico
    pass

def autenticar_usuario():
    """Autentica al usuario antes de acceder a la aplicación."""
    # Aquí puedes implementar la lógica para autenticar al usuario
    pass

# Función principal para ejecutar la aplicación
def main():
    """Función principal para ejecutar la aplicación."""
    cargar_datos()  # Llamar a la función para cargar los datos al iniciar la aplicación
    
    while True:
        print("\nMenú:")
        print("1. Agregar transacción")
        print("2. Listar transacciones")
        print("3. Calcular balance")
        print("4. Editar transacción")
        print("5. Eliminar transacción")
        print("6. Generar informe")
        print("7. Generar gráfico")
        print("8. Autenticar usuario")
        print("9. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_transaccion()
        elif opcion == "2":
            listar_transacciones()
        elif opcion == "3":
            calcular_balance()
        elif opcion == "4":
            editar_transaccion()
        elif opcion == "5":
            eliminar_transaccion()
        elif opcion == "6":
            generar_informe()
        elif opcion == "7":
            generar_grafico()
        elif opcion == "8":
            autenticar_usuario()
        elif opcion == "9":
            print("¡Hasta luego!")
            guardar_datos()  # Llamar a la función para guardar los datos antes de salir
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
