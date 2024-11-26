from datetime import datetime
import statistics
#se crea la clase experimento con atributos como nombre,fecha experimento, tipo y resultados
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
    
    experimento = Experimento(nombre, fechaExp, tipo, resultados)
    listaExperimentos.append(experimento)
    print("Su Experimento se ha guardado.")
    

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


