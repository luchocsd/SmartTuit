import time
import random
import os
import math
from frasesClasificadas import resultados
import matplotlib.pyplot as plt


global numGenes,numIndividuos, individuos, valObj, porcFitness,probCrossover, probMutacion
numGenes = 10 #CANT DE CATEGORIAS
numTuits= 6 #CANT DE TUITS POR INDIVIDUO
numIndividuos = 10 #MODIFICAR LUEGO
probCrossover = 0.7
probMutacion = 0.1
numeroGeneraciones = 5
generacion = 0


#Definimos el arreglo de individuos
individuos = [[0 for i in range(numGenes)] for j in range(numIndividuos)] 
tuitsAsociados = [[0 for i in range(numTuits)] for j in range(numIndividuos)] #para guardar los tuits asociados a cada individuo
valObj = [0 for i in range(numIndividuos)]  #para guardar el valor de la func obj de cada individuo 
porcFitness = [0 for i in range(numIndividuos)] #Para guaradar los valores del porcentaje que brinda la fun fitness para cada indiviuo
cantidadTuits =[[0 for i in range(numGenes)] for j in range(numIndividuos)]
cantLikes = [0 for i in range(numIndividuos)] #almacena la cantidad de likes de cada individuo, cada iteracion
cantidadTuitsTabla = [[0 for i in range(numGenes)]for j in range(numeroGeneraciones)] #para poder guardar mucha cantidad ya que no  sabemos le limite


def inicializarPoblacion(): #generamos numIndividuos individuos, con numTuits tuits distribuidos entre numGenes categorias
    global individuos
                                    #REVISAR LA PONDERACION AL AGREGAR MAS CATEGORIAS
    for i in range(numIndividuos):
        for j in range(numGenes):   #[1,1,1,1][2,2,2,2][3,3,3,3][4,4,4,4]   [][]
            if i==j:
                individuos[i][j] = 10  #ponderar una de las categorias en cada tuit distinto
            elif i<numGenes:
                posible = random.randint(0,3)
                if posible == 0:
                    individuos[i][j] = 0
                elif posible == 1:
                    individuos[i][j] = 1
                elif posible == 2:
                    individuos[i][j] = random.randint(0,2)
                elif posible == 3:
                    individuos[i][j] = random.randint(0,3)    
                 #como va a estar con un tuit ponderado, el resto de los tuits se generan con valores menores
            else:
                individuos[i][j] = random.randint(0,10)
    
    #guardarDatosTabla() TODO que es esto?


def asociarTuits(): #asocia los tuits a cada individuo
    global tuitsAsociados, cantidadTuits
    for i in range(numIndividuos):
        partesTotales = sum(individuos[i])  #[0, 1, 3, 1] -> 5 
        
        for j in range(numGenes):
            if partesTotales == 0:
                cantidadTuits[i][j] = 0
            else:  
                cantidadTuits[i][j] = math.ceil((individuos[i][j]/partesTotales)*numTuits)
        
        while(sum(cantidadTuits[i])>numTuits):    #Me aseguro que la suma sea = a numTuits ver si hacer random
            posicion = random.randint(0,numGenes-1) 
            if cantidadTuits[i][posicion]>0:
                cantidadTuits[i][posicion]-=1
        
      
        posTuitAsoc=0
        for k in range(numGenes): #parados en el individuo i recorremos cada una de las 4 categorias j
            for _ in range (cantidadTuits[i][k]): #la cantidad de tuits que tenga para esa categoria
                tuitsAsociados[i][posTuitAsoc] = resultados[k][random.randint(0,len(resultados[k])-1)] #le asocio k tuits de la categoria j
                posTuitAsoc+=1 #para que no sobreescriba sobre los mismo tuits

    for i in range(numIndividuos):
        random.shuffle(tuitsAsociados[i]) #mezcla los tuits asociados a cada individuo
    
def ruleta():
    global individuos
    hijos = [[0 for i in range(numGenes)] for j in range(numIndividuos)] #para guardar los hijos
    porcentajes = [0 for i in range(1000)]  #inicializamos el arreglo de la ruleta
    indAct = 0 #para llevar la cuenta de las posiciones que se van llenando
    
    for i in range(numIndividuos): 
        fit = int(porcFitness[i]*1000)
        for j in range(fit):
            porcentajes[indAct+j] = i
        indAct = indAct + fit
    for i in range(numIndividuos): #numIndividuos veces se hace la ruleta para llenar el resto
        if(indAct == 1000):   #para evitar que el arreglo porcetajes se exceda del limite
            indAct = 999
        num = random.randint(0,indAct) #para no usar 1000 y agregarle posibilidades al ind 0 debido al truncamiento
        aux = porcentajes[num]
        hijos [i] = individuos[aux].copy() #paso por valor a un array hijos los ganadores
    individuos = hijos

def calculoObjetivo():
    totalObj = 0  
    
    for i in range(numIndividuos):  #para cada individuo
        valObj[i] = cantLikes[i] #guarda los valores de la FO de cada individuo respetando su posicion
        totalObj += valObj[i] #acumula la sumatoria de valores de FO

    return totalObj #sumatoria de la funcion objetivo de la generacion

def funcionFitness():     
    total = calculoObjetivo()
    
    for i in range(numIndividuos):
        if(valObj[i]==0):
            porcFitness[i]=0
        else:
            porcFitness[i]=valObj[i]/total #Calcula el porcentaje de fitness de cada individuo 
    


def crossover():
   ind = 0
   for j in range(numIndividuos//2):
        aux=random.randint(1,100)
        if(aux<=probCrossover*100):
            corte = random.randint(1,numGenes-1) #punto de corte
            for i in range(corte,numGenes):
                aux2 = individuos[ind][i]
                individuos[ind][i] = individuos[ind+1][i]
                individuos[ind+1][i] = aux2
        ind+=2


def mutacion():
    for i in range(numIndividuos):
        if(random.randint(0,100)<=probMutacion*100):
            posicion = random.randint(0,numGenes-1)
            accion = random.randint(0,2)
            if individuos[i][posicion] == 10:#validar para que no se pase de 5 ni de 0(limites definidos)
                if accion == 0:
                    individuos[i][posicion] = individuos[i][posicion]-1
                else:
                    individuos[i][posicion] = individuos[i][posicion]

            elif individuos[i][posicion] == 0:
                individuos[i][posicion] = individuos[i][posicion]+1

            else:
                if accion == 0:
                    individuos[i][posicion] = individuos[i][posicion]+1
                elif accion == 1:
                    individuos[i][posicion] = individuos[i][posicion]
                else:
                    individuos[i][posicion] = individuos[i][posicion]-1


def guardarDatosTabla():
    global generacion, cantidadTuitsTabla
    for i in range(numGenes):
        for j in range(numIndividuos):
            cantidadTuitsTabla[generacion-1][i] = cantidadTuits[j][i] + cantidadTuitsTabla[generacion-1][i]
    

def imprimirTabla():
    global cantidadTuitsTabla, generacion, numeroGeneraciones
    
    # Definición de la tabla de datos
    generacion = len(cantidadTuitsTabla)
    numGenes = len(cantidadTuitsTabla[0])
    
    #print(cantidadTuitsTabla)
    for i in range(numGenes):
        plt.plot([j+1 for j in range(generacion)], [cantidadTuitsTabla[j][i] for j in range(generacion)], label=f'Categoría {i+1}')
    
    plt.xlabel('Generación')
    plt.ylabel('Cantidad de Tuits')
    plt.title('Cantidad de Tuits por Categoría a lo Largo de las Generaciones')
    plt.legend()
    plt.grid(True)
    
    # Ajuste de los límites de los ejes
    plt.xlim(0, generacion)
    plt.ylim(0, 60)
    
    plt.show()




#MENU ITERATIVO
os.system('cls')
op= ""
reaccion = ""
print("_"*90)
op = input("   C - Comenzar\n   S - Salir\nIngrese la opcion deseada: ").upper()
while op != "C" and op != "S":
    os.system('cls')   
    print("_"*90)
    print("Opcion no valida")
    op = input("   C - Comenzar\n   S - Salir\nIngrese la opcion deseada: ").upper()

inicializarPoblacion() #se genera la poblacion inicial de individuos
asociarTuits() #se asocian los tuits a cada individuo


while op.upper() =="C": #si el usuario desea comenzar el experimento

    for i in range (numIndividuos): #para cada individuo de la poblacion
        for j in range (numTuits): #para cada tuit del individuo
            if (reaccion !="F"): #si el usuario no desea terminar el experimento
                time.sleep(0.25)
                os.system('cls')
                time.sleep(0.25)

                #muestra datos del tuit (solo en desarrollo, despues sacar) TODO SACAR
                print("Generacion: ", generacion) 
                print("Individuo: ", i)
                print("Likes de este individuo: ", cantLikes[i])
                #muestra el tuit
                print ("\033[92m",tuitsAsociados[i][j],"\033[0m") 
                
                #pide que de Like, No Like o Finalizar
                reaccion = input("   L - Like\n   N - No Like (continuar)\n   F - Finalizar experimento\nIngrese la opcion deseada: ").upper()
                while reaccion != "L" and reaccion != "N" and reaccion != "F":
                    print("Opcion no valida")
                    reaccion= input("   L - Like\n   N - No Like (continuar)\n   F - Finalizar experimento\nIngrese la opcion deseada: ").upper()

                if (reaccion =="L"):
                    cantLikes[i]+=1
            else:
                op="S"
                break

            funcionFitness()

        if (reaccion =="F"):
            break

    generacion+=1
    cantLikes = [0 for i in range(numIndividuos)] #reinicia el array de likes

    ruleta()
    crossover()
    mutacion()
    asociarTuits()
    guardarDatosTabla()
    

imprimirTabla()
print("\n--- Fin del programa ---")