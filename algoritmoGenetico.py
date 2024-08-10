#########################################################################################################
# ALGORITMO GENETICO
import time
import random
import os

global numGenes,numIndividuos, individuos, valObj, porcFitness,probCrossover, probMutacion, valorMayorGlobal, valorMenorGlobal, menorGlobal, mayorGlobal, corridas, promedioValObjPorCorrida, nombreArchivoExcel
numGenes = 4 #CANT DE CATEGORIAS
numTuits= 5 #CANT DE TUITS POR INDIVIDUO
numIndividuos = 5 #MODIFICAR LUEGO
probCrossover = 0.75
probMutacion = 0.05
valorMenorGlobal = 99999 ################ PARA GUARDAR DATOS POR CORRIDA, NO LOS USAMOS AUN
valorMayorGlobal = 0 #####################
menorGlobal = [0]*numGenes #######
mayorGlobal = [0]*numGenes #######
corridas = 0 # DIRIA QUE TRABAJEMOS CON CORRIDAS HASTA QUE EL USUARIO LAS CORTE, NADA HARDCODEADO

#Definimos el arreglo de individuos
individuos = [[0 for i in range(numGenes)] for j in range(numIndividuos)] 
valObj = [0 for i in range(numIndividuos)]  #para guardar el valor de la func obj de cada individuo 
porcFitness = [0 for i in range(numIndividuos)] #Para guaradar los valores del porcentaje que brinda la fun fitness para cada indiviuo

#Incializar los valores que dependen de las corridas
def inicializarValoresCorridas():
    global minimoFo, maximoFo, cromosomasMaximos, cromosomasMinimos, promedioValObjPorCorrida, corridas, acumCorridas
    
    acumCorridas = 0
    minimoFo = [0 for _ in range(corridas)]
    maximoFo = [0 for _ in range(corridas)]
    cromosomasMaximos = [0 for _ in range(corridas)]
    cromosomasMinimos = [0 for _ in range(corridas)]
    promedioValObjPorCorrida = [0 for _ in range(corridas)]

def inicializarPoblacion(): #generamos numIndividuos individuos, con numTuits tuits distribuidos entre numGenes categorias
    global individuos
    aux=0 #cant tuits
    for i in range(numIndividuos):
        for j in range(numGenes):
           while(aux<numTuits):
            aux2= random.randint(0,numTuits-aux)
            individuos[i][j] = aux2
            aux+=aux2

op= ""
reaccion = ""
print("_"*90)
op = input("   C - Comenzar\n   S - Salir\nIngrese la opcion deseada: ").upper()
while op != "C" and op != "S":
    print("Opcion no valida")
    op = input("   C - Comenzar\n   S - Salir\nIngrese la opcion deseada: ").upper()


'''
habria que generar un array de tuits (o rescatarlos de un csv, no se, cada uno catalogado con su categoría)
luego se generan al azar los individuos (arreglos como [0, 1, 3, 1]) con inicializarPoblacion()
luego se traen los tuits de esas categorías (no se si conviene hacerlo secuencialmente para evitar mostrar tuits repetidos? pero haría que 
todas las corridas que hagamos sean iguales)
Se debería generar un fitness del tamaño numIndividuos que almacene el fitness de cada ind al final de cada uno
Luego se hacen selec, cross y mut y se repite
''' 
inicializarValoresCorridas() #no se si nos va a servir esto
inicializarPoblacion() #se genera la poblacion inicial de individuos

while op.upper() =="C": #si el usuario desea comenzar el experimento
    for i in range (numIndividuos): #para cada individuo de la poblacion
        likes=0
        for j in range (numTuits): #para cada tuit del individuo
            if (reaccion !="F"): #si el usuario no desea terminar el experimento
                time.sleep(0.5)
                os.system('cls')
                time.sleep(0.5)
                print("individuo: ", i, "tuit: ", j, "likes de este individuo: ", likes) #muestra datos del tuit (solo en desarrollo, despues sacar)
                
                print (" \033[92mtuit gracioso o interesante lalalala\033[0m") #muestra el tuit y pide que de Like, No Like o Finalizar
                
                reaccion= input("   L - Like\n   N - No Like (continuar)\n   F - Finalizar experimento\nIngrese la opcion deseada: ").upper()
                while reaccion != "L" and reaccion != "N" and reaccion != "F":
                    print("Opcion no valida")
                    reaccion= input("   L - Like\n   N - No Like (continuar)\n   F - Finalizar experimento\nIngrese la opcion deseada: ").upper()
                if (reaccion =="L"):
                    likes+=1
                elif(reaccion =="F"): #pregunta para ver si no fue un typo, si quiere terminar, dejarlo, si no modificar reaccion
                    reaccion= input("esta seguro que desea terminar el experimento? F - finalizar /N - no finalizar").upper() #validar
            else: #si desea finalizar
                break 
            op="S"
        if (reaccion =="F"):
            break


        
        #calcular y almacenar fitness del individuo
    
    #realizar seleccion, crossover y mutacion
    #guardar datos si es pertinente
    #se genera un nuevo array de individuos y se reinicia el while en una nueva corrida
#mostrar datos del experimento en general
print("\n--- Fin del programa ---")