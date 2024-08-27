import time
import random
import os
import math
from tuits_categorizados import tuit_categoria 


global numGenes,numIndividuos, individuos, valObj, porcFitness,probCrossover, probMutacion, valorMayorGlobal, valorMenorGlobal, menorGlobal, mayorGlobal, corridas, promedioValObjPorCorrida, nombreArchivoExcel
numGenes = 10 #CANT DE CATEGORIAS
numTuits= 10 #CANT DE TUITS POR INDIVIDUO
numIndividuos = 10 #MODIFICAR LUEGO
probCrossover = 0.75
probMutacion = 0.25
valorMenorGlobal = 99999 ################ PARA GUARDAR DATOS POR CORRIDA, NO LOS USAMOS AUN
valorMayorGlobal = 0 #####################
menorGlobal = [0]*numGenes #######
mayorGlobal = [0]*numGenes #######
corridas = 0 # DIRIA QUE TRABAJEMOS CON CORRIDAS HASTA QUE EL USUARIO LAS CORTE, NADA HARDCODEADO



#Definimos el arreglo de individuos
individuos = [[0 for i in range(numGenes)] for j in range(numIndividuos)] 
tuitsAsociados = [[0 for i in range(numTuits)] for j in range(numIndividuos)] #para guardar los tuits asociados a cada individuo
valObj = [0 for i in range(numIndividuos)]  #para guardar el valor de la func obj de cada individuo 
porcFitness = [0 for i in range(numIndividuos)] #Para guaradar los valores del porcentaje que brinda la fun fitness para cada indiviuo
cantidadTuits =[[0 for i in range(numGenes)] for j in range(numIndividuos)]
cantLikes = [0 for i in range(numIndividuos)] #almacena la cantidad de likes de cada individuo, cada iteracion


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


    print("Poblacion inicial: ", cantidadTuits)




def asociarTuits(): #asocia los tuits a cada individuo
    global tuitsAsociados, cantidadTuits
    for i in range(numIndividuos):
        partes = sum(individuos[i])  #[0, 1, 3, 1] -> 5 
        print("##math##")
        for j in range(numGenes):
            cantidadTuits[i][j] = math.ceil((individuos[i][j]/partes)*numTuits)
        
        while(sum(cantidadTuits[i])>numTuits):    #Me aseguro que la suma sea = a numTuits ver si hacer random
            posicion = random.randint(0,numGenes-1) 
            if cantidadTuits[i][posicion]>0:
                cantidadTuits[i][posicion]-=1
        
      
        posTuitAsoc=0
        for j in range(numGenes): #parados en el individuo i recorremos cada una de las 4 categorias j
            for k in range (cantidadTuits[i][j]): #la cantidad de tuits que tenga para esa categoria
                tuitsAsociados[i][posTuitAsoc] = tuit_categoria[j][random.randint(0,9)] #le asocio k tuits de la categoria j
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
            accion = random.randint(0,1)
            if individuos[i][posicion] == 10:  #validar para que no se pase de 5 ni de 0(limites definidos)
                individuos[i][posicion] = individuos[i][posicion]-1
            elif individuos[i][posicion] == 0:
                individuos[i][posicion] = individuos[i][posicion]+1
            else:
                if accion == 0:
                    individuos[i][posicion] = individuos[i][posicion]-1
                else:
                    individuos[i][posicion] = individuos[i][posicion]+1




    
'''
habria que generar un array de tuits (o rescatarlos de un csv, no se, cada uno catalogado con su categoría)
luego se generan al azar los individuos (arreglos como [0, 1, 3, 1]) con inicializarPoblacion()
luego se traen los tuits de esas categorías (no se si conviene hacerlo secuencialmente para evitar mostrar tuits repetidos? pero haría que 
todas las corridas que hagamos sean iguales)
Se debería generar un fitness del tamaño numIndividuos que almacene el fitness de cada ind al final de cada uno
Luego se hacen selec, cross y mut y se repite
''' 
op= ""
reaccion = ""
print("_"*90)
op = input("   C - Comenzar\n   S - Salir\nIngrese la opcion deseada: ").upper()
while op != "C" and op != "S":
    print("Opcion no valida")
    op = input("   C - Comenzar\n   S - Salir\nIngrese la opcion deseada: ").upper()

inicializarPoblacion() #se genera la poblacion inicial de individuos
asociarTuits() #se asocian los tuits a cada individuo

generacion = 0
iteracion = 0
while op.upper() =="C": #si el usuario desea comenzar el experimento
    for i in range (numIndividuos): #para cada individuo de la poblacion
        for j in range (numTuits): #para cada tuit del individuo
            if (reaccion !="F"): #si el usuario no desea terminar el experimento
                #time.sleep(0.5)
                os.system('cls')
                #time.sleep(0.5)
                print("iteracion: ",iteracion, "individuo: ", i, "likes de este individuo: ", cantLikes[i],  "\ntuit: ", j, "GEN: ", generacion) #muestra datos del tuit (solo en desarrollo, despues sacar)
                
                print ("\033[92m",tuitsAsociados[i][j],"\033[0m") #muestra el tuit y pide que de Like, No Like o Finalizar
                
                reaccion= input("   L - Like\n   N - No Like (continuar)\n   F - Finalizar experimento\nIngrese la opcion deseada: ").upper()
                while reaccion != "L" and reaccion != "N" and reaccion != "F":
                    print("Opcion no valida")
                    reaccion= input("   L - Like\n   N - No Like (continuar)\n   F - Finalizar experimento\nIngrese la opcion deseada: ").upper()
               
                if (reaccion =="L"):
                    cantLikes[i]+=1
                elif(reaccion =="F"): #pregunta para ver si no fue un typo, si quiere terminar, dejarlo, si no modificar reaccion
                    #time.sleep(0.5)
                    os.system('cls')
                    #time.sleep(0.5)
                    reaccion= input("esta seguro que desea terminar el experimento? \nF - finalizar \nN - no finalizar").upper()
                    while reaccion != "F" and reaccion != "N":
                        print("Opcion no valida")
                        reaccion= input("Esta seguro que desea terminar el experimento? \nF - finalizar \nN - no finalizar").upper()
                    if (reaccion=="N"):
                        j-=1 #esto puede estar re feo
                # print('FITNESS')
                # print(calculoObjetivo())
                # print('PORCENTAJE FITNESS')
                funcionFitness()
                # print(porcFitness[i])
            else: #si desea finalizar
                break 
            op="S"
        # print(porcFitness)
        if (reaccion =="F"):
            break

    op = input("   C - Continuar\n   S - Salir\nIngrese la opcion deseada: ").upper()
    while op != "C" and op != "S":
        print("Opcion no valida")
        op = input("   C - Continuar\n   S - Salir\nIngrese la opcion deseada: ").upper()
    generacion+=1
    
    print("\ncantidad de likes por individuo")
    print(cantLikes)
    print(cantidadTuits)
    cantLikes = [0 for i in range(numIndividuos)] #reinicia el array de likes
    print(porcFitness)
    print("poblacion antes de ruleta: ", individuos)
    ruleta()
    print("poblacion despues de ruleta: ", individuos)
    crossover()
    print("poblacion despues de crossover: ", individuos)
    mutacion()
    print("poblacion despues de mutacion: ", individuos)
    print("Datos del experimento")
    input()
    asociarTuits()
print("\n--- Fin del programa ---")


  
  
        #calcular y almacenar fitness del individuo
    
    #realizar seleccion, crossover y mutacion
    #guardar datos si es pertinente
    #se genera un nuevo array de individuos y se reinicia el while en una nueva corrida
    #se reinicia el array de likes
#mostrar datos del experimento en general