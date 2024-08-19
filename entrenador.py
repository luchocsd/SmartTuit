import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import re
import joblib
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
def remove_emojis(text):
    result = re.sub(
        r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF]',
        '',
        text
    )
    return result
                           
data['text'] = [remove_accents(text) for text in data['text']]
data['text'] = [remove_emojis(text) for text in data['text']]



df = pd.DataFrame(data)

# Crear el vectorizador con la lista de stop words en español
vectorizer = CountVectorizer(stop_words=stop_words_spanish, ngram_range=(1, 3))


X = vectorizer.fit_transform(df['text']) # Ajustar y transformar los documentos


print("El total de palabras utilizadas en el entrenamiento: " , len(vectorizer.get_feature_names_out()))


#print(X.toarray())  

'''
block = 100
for i in range(0, len(vectorizer.get_feature_names_out()), block):
    print("Ejemplo de las primeras 100 palabras: ", vectorizer.get_feature_names_out()[i:i+block])
    if i == 7000:  
        break
'''





# Dividir los datos en conjunto de entrenamiento y prueba   # test_size=0.3 , lo q implica que el resto se completa con 0.7 para train.
X_train, X_test, y_train, y_test = train_test_split(X, df['category'], test_size=0.05, random_state=42) # 70% entrenamiento, 30% prueba ya qu ese declaro     https://www.youtube.com/watch?v=BUkqYGPnLZ8&ab_channel=ManifoldAILearning     explicacion de la funcion 
                                                                                                        



# Crear y entrenar el clasificador Naive Bayes
clf = MultinomialNB()
clf.fit(X_train, y_train)


save_directory = 'Projecto Investigacion/SmartTuit/ModeloEntrenado'  # Reemplaza esto con la ruta a tu carpeta

# Crear la carpeta si no existe
os.makedirs(save_directory, exist_ok=True)

# Guardar el modelo entrenado
model_path = os.path.join(save_directory, 'modelo_entrenado.pkl')
joblib.dump(clf, model_path)

# Guardar el vectorizador
vectorizer_path = os.path.join(save_directory, 'vectorizador.pkl')
joblib.dump(vectorizer, vectorizer_path)


