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
        
