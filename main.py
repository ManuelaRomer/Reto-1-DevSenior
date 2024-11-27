from datetime import datetime
import statistics
#Se crea la clase experimento con atributos como nombre,fecha experimento, tipo y resultados
class Experimento:
    def __init__(self, nombre, fechaExp, tipo, resultados):
        self.nombre = nombre
        self.fechaExp = fechaExp
        self.tipo = tipo
        self.resultados = resultados
# esta funcion agregar experimentos me permite guardar en una lista los
# experimentos que se estan creando y adiciconar con la funcion appened
def agregarExperimento(listaExperimentos):
    nombre = input("Ingrese el nombre del experimento: ")
    fechaExp_str = input("Ingrese la fecha del experimento (DD/MM/YYYY): ")
    try:
        fechaExp = datetime.strptime(fechaExp_str, "%d/%m/%Y")
    except ValueError:
        print("Fecha no válida.")
        return
    
    tipo = input("Ingrese el tipo de experimento (Quimico, Fisico, Biologico, otras): ")
    while tipo not in ["Quimico", "Fisico", "Biologico", "otras"]:
        print("Tipo de experimento no válido. Intente de nuevo.")
        tipo = input("Ingrese el tipo de experimento (Quimico, Fisico, Biologico, otras): ")

    resultados_str = input("Por favor ingrese los resultados experimentales, separados por comas: ")
    
    try:
        resultados = list(map(float, resultados_str.split(",")))
    except ValueError:
        print("Resultados no válidos.")
        return
    
# se crea el objeto y se agrega a lista de experimentos
    experimento = Experimento(nombre, fechaExp, tipo, resultados)
    listaExperimentos.append(experimento)
    print("Su Experimento se ha guardado.")

# con esta funcionpodemos visaulizar el experimento con todos sus atributos
def visualizarExperimento(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos registrados.")
        return
    for i, experimento in enumerate(listaExperimentos, start=1):
        print(f"\nExperimento {i}")
        print(f"Nombre: {experimento.nombre}")
        print(f"Fecha: {experimento.fechaExp.strftime('%d/%m/%Y')}")
        print(f"Tipo: {experimento.tipo}")
        print(f"Resultados: {experimento.resultados}")

# con esta funcion podremos eliminar un experimento
def eliminarExperimento(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos registrados, no se puede eliminar nada")
        return
    
    nombre = input("Ingrese el nombre del experimento a eliminar:")
# buscamos el experimento por el nombre para saber cual eliminar
    for i, experimento in enumerate(listaExperimentos):
        if experimento.nombre == nombre: 
            comprobar = input(f"¿Desea eliminar el experimento '{nombre}'? R: si o no: ").strip().lower()
            if comprobar == "si":
                listaExperimentos.pop(i)
                print(f"El experimento '{nombre}' se elimino correctamente")
                return 
            else:
                print("El experimento no fue eliminado")
                return
    print(f"El experimento '{nombre}' no fue encontrado")
    

# funcion para analizar los experimentos 
def analizarExperimentos(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos registrados.")
        return
    for experimento in listaExperimentos:
        promedio = statistics.mean(experimento.resultados)
        maximo = max(experimento.resultados)
        minimo = min(experimento.resultados)
        print(f"\nAnálisis de {experimento.nombre}")
        print(f"Promedio de resultados: {promedio}")
        print(f"Máximo de  resultados: {maximo}")
        print(f"Mínimo de resultados: {minimo}")

# función para comparar los experimentos 
def compararExperimentos(listaExperimentos):
    if len(listaExperimentos) < 2: 
        print("Deben de haber como minimo 2 experimentos")
        return
    print("Experimentos registrados:")
    for i, Experimento in enumerate(listaExperimentos):
        print(f"{i+1}. {Experimento.nombre}")
        
    try:
        # selecionamos los experimentos a comparar
        primer1 = int(input("Seleccione el número del primer experimento a comparar: ")) - 1
        segundo2 = int(input("Seleccione el número del segundo experimento a comparar: ")) - 1
        
        if primer1 < 0 or primer1 >= len(listaExperimentos) or segundo2 < 0 or segundo2 >= len(listaExperimentos):
            print("Numero no valido porfavor ingresa uno correcto")
            return
        #creamos las variables que tendran las referencias de la lista
        experimento1 = listaExperimentos[primer1]
        experimento2 = listaExperimentos[segundo2]
        
        # calculamos los promedios
        promedio1 = statistics.mean(experimento1.resultados)
        promedio2 = statistics.mean(experimento2.resultados)
        
        # Mostrar resultados de comparación
        print(f"\nComparación entre {experimento1.nombre} y {experimento2.nombre}:")
        print(f"{experimento1.nombre} - Promedio: {promedio1}")
        print(f"{experimento2.nombre} - Promedio: {promedio2}")
        
        if promedio1 > promedio2:
            print(f"El experimento '{experimento1.nombre}' tiene un promedio mayor.")
        elif promedio1 < promedio2:
            print(f"El experimento '{experimento2.nombre}' tiene un promedio mayor.")
        else:
            print(f"los dos experimentos tienen el mismo promedio.")
    
    except ValueError:
        print("Respuesta no valida")
        
    

# funcion para generar un informe de todos los experimentos 
def generarInforme(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos registrados")
        return
    
    # abrimos un archivo de texto para realizar el informe 
    with open("informe_experimento.txt", "w") as archivo:
        #escribimos los detalles que queremos que contenga
        for experimento in listaExperimentos:
            archivo.write(f"Nombre: {experimento.nombre}\n")
            archivo.write(f"Fecha experimento: {experimento.fechaExp.strftime("%d/%m/%Y")}\n")
            archivo.write(f"Tipo: {experimento.tipo}\n")
            archivo.write(f"Resultados: {experimento.resultados}\n")
            archivo.write("\n")
    print("Informe generado como 'informe_experimento.txt'")

# funcion para el menu de interaccion
def menu():
    listaExperimentos = []
    while True:
        print("\nMENU DE OPCIONES:")
        print("1. Agregar Experimentos")
        print("2. Visualizar Experimentos")
        print("3. Eliminar experimento")
        print("4. Analizar Experimento")
        print("5. Comparar Experimentos")
        print("6. Generar Informe")
        print("7. Salir")
        
        opcion = input("Seleccione la opción: ")
        
        if opcion == "1":
            agregarExperimento(listaExperimentos)
        elif opcion == "2":
            visualizarExperimento(listaExperimentos)
        elif opcion == "3":
            eliminarExperimento(listaExperimentos)
        elif opcion == "4":
            analizarExperimentos(listaExperimentos)
        elif opcion == "5":
            compararExperimentos(listaExperimentos)
        elif opcion == "6":
            generarInforme(listaExperimentos)
        elif opcion == "7":
            print("Saliendo")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()

