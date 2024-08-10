import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import re
import time
import random
import os

from data import data # Importar los datos de entrenamiento alamacenados en data.py(archivo externo)
from stop_words import stop_words_spanish # Importar la lista de stop words en español desde stop_words.py(archivo externo)




#Filtrado de acentos
def remove_accents(text):
    
    result = re.sub(
        r'[áéíóú]',
        lambda match: {
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'
        }[match.group()],
        text
    )
    return result

data['text'] = [remove_accents(text) for text in data['text']]


df = pd.DataFrame(data)
print(data)
# Crear el vectorizador con la lista de stop words en español
vectorizer = CountVectorizer(stop_words=stop_words_spanish)


X = vectorizer.fit_transform(df['text']) # Ajustar y transformar los documentos


#print(vectorizer.get_feature_names_out())
#print(X.toarray())  



# Dividir los datos en conjunto de entrenamiento y prueba   # test_size=0.3 , lo q implica que el resto se completa con 0.7 para train.
X_train, X_test, y_train, y_test = train_test_split(X, df['category'], test_size=0.1, random_state=42) # 70% entrenamiento, 30% prueba ya qu ese declaro     https://www.youtube.com/watch?v=BUkqYGPnLZ8&ab_channel=ManifoldAILearning     explicacion de la funcion 
                                                                                                        



# Crear y entrenar el clasificador Naive Bayes
clf = MultinomialNB()
clf.fit(X_train, y_train)



# Nuevos textos a clasificar en las categorías existentes
new_texts = [
    ""
    
]
'''''
# Transformar los nuevos textos utilizando el mismo vectorizador
X_new = vectorizer.transform(new_texts)

# Predecir las categorías de los nuevos textos
new_predictions = clf.predict(X_new)
#print(new_predictions)

#categorias = ["animal","tecnologia", "deportes", "economia"]
'''
new_texts = [remove_accents(text) for text in new_texts]

new_X = vectorizer.transform(new_texts)

# Obtener las probabilidades de las categorías
probabilities = clf.predict_proba(new_X)

for i in range(len(new_texts)):

    print("--Elemento ",i,"--")
    category_probabilities = {category: prob for category, prob in zip(clf.classes_, probabilities[i])}

    # Imprimir las probabilidades de cada categoría
    print("Probabilidades de categorías:")
    for category, prob in category_probabilities.items():
        print(f"{category}: {prob * 100:.2f}%")
        
#########################################################################################################
# ALGORITMO GENETICO
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
                break #esto es temporal
            op="S"
        if (reaccion =="F"):
            break
        #calcular y almacenar fitness del individuo
    
    #realizar seleccion, crossover y mutacion
    #guardar datos si es pertinente
    #se genera un nuevo array de individuos y se reinicia el while en una nueva corrida
#mostrar datos del experimento en general
print("\n--- Fin del programa ---")