"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """


import sys
import config
from App import controller
from DISClib.ADT import stack
import timeit
assert config
import model as mod

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________


servicefile = '201801-2-citibike-tripdata.csv'
cont=0
initialStation = None
recursionLimit = 20000

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar informacion")
    print("3- Buscar cantidad de cluster de Viajes")
    print("4- Buscar ruta turistica Circular")
    print("5- Buscar estaciones críticas")
    print("6- Buscar ruta turistica por resistencia")
    print("7- buscar rutas por rango de edades")
    print("8- Buscar ruta de interes turístico")
    print("9- Buscar estaciones para publicidad e identificacion de Bicicletas para mantenimiento")
    print("10- Buscar bicicletas para mantenimiento")
    print("0- Exit")


def optionTwo():
    print("\nCargando información de transporte de singapur ....")
    controller.loadTrips(cont)
    print(cont['stops'])
    numedges = controller.totalConnections(cont)
    numvertex = controller.totalStops(cont)
    print('Numero de vertices: ' + str(numvertex))
    print('Numero de arcos: ' + str(numedges))
    print('El limite de recursion actual: ' + str(sys.getrecursionlimit()))
    sys.setrecursionlimit(recursionLimit)
    print('El limite de recursion se ajusta a: ' + str(recursionLimit))

    

def optionThree():
        v1=input("Ingrese estación 1(id-name)\n")
        v2=input("Ingrese estación 2(id-name)\n")
        controller.conectados_estrictamente(cont['connections'],v1,v2)


def optionFourOne(graph, vertex, initialTime, finalTime):
    routesNumber = controller.findCircularRoutesNumber(graph, vertex, initialTime, finalTime)
    return lt.size(routesNumber)

  
def optionFourTwo(graph, vertex, initialTime, finalTime):
    routesList = controller.findCircularRoutesList(graph, vertex, initialTime, finalTime)
    return routesList



def optionFive(estation,time,graph):
    routesList = controller.rutas_por_min(estation,time,graph)
    return routesList


def optionFive():
    controller.requerimiento3(cont["connections"],cont)


def optionSix():
    None


def optionSeven(graph):
    print("rango de edades\n")
    print("1) 0-10 años\n")
    print("2) 10-20 años\n")
    print("3) 20-30 años\n")
    print("4) 30-40 años\n")
    print("5) 40-50 años\n")
    print("6) 50-60 años\n")
    print("7) +60 años\n")
    edad=input("")
    routesList = controller.ruta_años(graph,edad)
    return routesList



    


def optionEight():
    lat1=float(input("ingrese latitud partida"))
    lon1=float(input("ingrese longitud partida"))
    lat2=float(input("ingrese latitud final"))
    lon2=float(input("ingrese longitud final"))
    controller.requerimiento6(cont["connections"],lat1,lon1,lat2,lon2,cont)


def optionNine():
    None


def optionTen():
    None


"""
Menu principal
"""


while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    
    if int(inputs[0]) == 1:
        print("\nInicializando....")
        cont = controller.init()

        
    elif int(inputs[0]) == 2:
        executiontime = timeit.timeit(optionTwo, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

        
    elif int(inputs[0]) == 3:
        id_1 = input("Ingrese id de estación de partida: ")
        id_2 = input("Ingrese id de estación de llegada: ")
        optionThree(id_1, id_2)
        executiontime = timeit.timeit(optionThree, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

        
    elif int(inputs[0]) == 4:
        print("""Los tiempos presentados se calculan con un estimado de 20 
                minutos que podrá destinar para conocer cada parada""")

        vertex = input('Indique la estación de partida: ')
        initialTime = input('Tiempo mínimo disponible para el recorrido, dado en minutos: ')
        finalTime = input('Tiempo máximo disponible para el recorrido, dado en minutos: ')

        numeroRutas = optionFourOne(cont['connections'], vertex, initialTime, finalTime)
        listaRutas = optionFourTwo(cont['connections'], vertex, initialTime, finalTime)

        print('Se han encontrado ' + numeroRutas + ' rutas.')
        print('Lista de las opciones: \n')
        print(listaRutas)
        
    elif int(inputs[0]) == 5:

        estation=input('Estación de partida: ')
        time=input("tiempo estimado: ")
        lista_rutas=optionFive(estation, time, cont)
        print(lista_rutas)

        optionFive()



    elif int(inputs[0]) == 6:
        None


    elif int(inputs[0]) == 7:

        respuesta=optionSeven(cont)
        print(respuesta)

        None



    elif int(inputs[0]) == 8:
        optionEight()


    elif int(inputs[0]) == 9:
        None

    
    elif int(inputs[0]) == 10:
        None

    else:
        sys.exit(0)
sys.exit(0)

