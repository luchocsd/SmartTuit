#########################################################################################################
# ALGORITMO GENETICO
import time
import random
import os
import math

global numGenes,numIndividuos, individuos, valObj, porcFitness,probCrossover, probMutacion, valorMayorGlobal, valorMenorGlobal, menorGlobal, mayorGlobal, corridas, promedioValObjPorCorrida, nombreArchivoExcel
numGenes = 4 #CANT DE CATEGORIAS
numTuits= 10 #CANT DE TUITS POR INDIVIDUO
numIndividuos = 6 #MODIFICAR LUEGO
probCrossover = 0.75
probMutacion = 0.05
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



def inicializarPoblacion(): #generamos numIndividuos individuos, con numTuits tuits distribuidos entre numGenes categorias
    global individuos
    
    for i in range(numIndividuos):
        for j in range(numGenes):
            if i==j:
                individuos[i][j] = 5  #ponderar una de las categorias en cada tuit distinto
            elif i<numGenes:
                individuos[i][j] = random.randint(0,3)  #como va a estar con un tuit ponderado, el resto de los tuits se generan con valores menores
            else:
                individuos[i][j] = random.randint(0,5)


    print("Poblacion inicial: ", individuos)


from tuits_categorizados import tuit_categoria 

def asociarTuits(): #asocia los tuits a cada individuo
    global tuitsAsociados
    for i in range(numIndividuos):
        partes = sum(individuos[i])  #[0, 1, 3, 1] -> 5 ['animal'] * 60 + ['economía'] * 60 + ['tecnología'] * 60 + ['deportes']
        print("##math##")
        animal = math.ceil((individuos[i][0]/partes)*numTuits)
        economia = math.ceil((individuos[i][1]/partes)*numTuits)   #math.ceil para redondear hacia arriba
        tecnologia = math.ceil((individuos[i][2]/partes)*numTuits)
        deportes = math.ceil((individuos[i][3]/partes)*numTuits)

        while(animal+economia+tecnologia+deportes>numTuits):    #Me aseguro que la suma sea = a numTuits
            maximo = max(animal, economia, tecnologia, deportes) 
            if maximo == animal:
                animal-=1
            elif maximo == economia:    
                economia-=1
            elif maximo == tecnologia:
                tecnologia-=1
            else:
                deportes-=1

        for j in range(numTuits):
            if j<animal:
                tuitsAsociados[i][j] = tuit_categoria[0][random.randint(0,9)] #se asocia un tuit de la categoria animal(la posicion 0)
            elif j<animal+economia:
                tuitsAsociados[i][j] = tuit_categoria[1][random.randint(0,9)]
            elif j<animal+economia+tecnologia:
                tuitsAsociados[i][j] = tuit_categoria[2][random.randint(0,9)]
            else:
                tuitsAsociados[i][j] = tuit_categoria[3][random.randint(0,9)]
    
        
    print("Tuits asociados: ", tuitsAsociados)

        
        
            
            


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

inicializarPoblacion() #se genera la poblacion inicial de individuos
asociarTuits() #se asocian los tuits a cada individuo
'''
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

'''