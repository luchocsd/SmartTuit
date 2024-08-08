import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import re
import time

data = {
    'text': [
        # Animal
        "El ágil zorro se deslizó entre los arbustos",
        "La tortuga avanzó lentamente hacia el mar",
        "El gorila se golpeó el pecho con fuerza",
        "Las mariposas revolotean en el jardín",
        "El búho ululaba en lo alto del árbol",
        "Las serpientes se esconden entre las rocas",
        "El delfín saltó fuera del agua",
        "Los caballos galopan en el campo abierto",
        "El lobo aullaba a la luna llena",
        "El camaleón cambia de color para camuflarse",

        # Economía
        "El mercado inmobiliario está en auge",
        "Los ingresos fiscales han aumentado este trimestre",
        "Las exportaciones de bienes agrícolas han crecido",
        "El sector tecnológico está impulsando la economía",
        "Los inversores están preocupados por la volatilidad",
        "La deuda pública ha alcanzado un nuevo récord",
        "El comercio internacional se ha desacelerado",
        "Las empresas están optimizando sus cadenas de suministro",
        "La industria automotriz está experimentando cambios",
        "Las políticas monetarias afectan a las pequeñas empresas",
        "el dinero cada vez vale menos que antes",

        # Tecnología
        "El coche autónomo se ha convertido en una realidad",
        "La criptomoneda sigue ganando popularidad",
        "El software de reconocimiento facial es controvertido",
        "Los dispositivos de IoT están interconectados",
        "La ciberseguridad es crucial en la era digital",
        "El aprendizaje automático mejora con datos masivos",
        "El metaverso ofrece nuevas oportunidades sociales",
        "La computación cuántica promete revolucionar la ciencia",
        "Las impresoras 3D están cambiando la fabricación",
        "La tecnología blockchain asegura las transacciones",

        # Deportes
        "El maratón de la ciudad atrajo a miles de corredores",
        "El boxeador ganó el título mundial en un combate épico",
        "El equipo de baloncesto dominó el campeonato",
        "El surfista montó una ola gigantesca",
        "La ciclista rompió el récord de velocidad",
        "El nadador estableció una nueva marca olímpica",
        "El gimnasta realizó una rutina perfecta en el anillo",
        "El jugador de rugby anotó un try espectacular",
        "El esquiador descendió la montaña a gran velocidad",
        "El arquero hizo una parada impresionante"
    ],
    'category': [
        'animal', 'animal', 'animal', 'animal', 'animal', 'animal', 'animal', 'animal', 'animal', 'animal',
        'economía', 'economía', 'economía', 'economía', 'economía', 'economía', 'economía', 'economía','economía', 'economía', 'economía',
        'tecnología', 'tecnología', 'tecnología', 'tecnología', 'tecnología', 'tecnología', 'tecnología', 'tecnología', 'tecnología', 'tecnología',
        'deportes', 'deportes', 'deportes', 'deportes', 'deportes', 'deportes', 'deportes', 'deportes', 'deportes', 'deportes'
    ]
}


df = pd.DataFrame(data)




# Lista de stop words en español
stop_words_spanish = [
    'de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 'se', 'las', 'por', 'un', 
    'para', 'con', 'no', 'una', 'su', 'al', 'lo', 'como', 'más', 'pero', 'sus', 'le', 
    'ya', 'o', 'fue', 'este', 'ha', 'sí', 'porque', 'esta', 'son', 'entre', 'cuando', 
    'muy', 'sin', 'sobre', 'también', 'me', 'hasta', 'hay', 'donde', 'quien', 'desde', 
    'todo', 'nos', 'durante', 'todos', 'uno', 'les', 'ni', 'contra', 'otros', 'ese', 
    'eso', 'ante', 'ellos', 'e', 'esto', 'mí', 'antes', 'algunos', 'qué', 'unos', 'yo', 
    'otro', 'otras', 'otra', 'él', 'tanto', 'esa', 'estos', 'mucho', 'quienes', 'nada', 
    'muchos', 'cual', 'poco', 'ella', 'estar', 'estas', 'algunas', 'algo', 'nosotros', 
    'mi', 'mis', 'tú', 'te', 'ti', 'tu', 'tus', 'ellas', 'nosotras', 'vosotros', 
    'vosotras', 'os', 'mío', 'mía', 'míos', 'mías', 'tuyo', 'tuya', 'tuyos', 'tuyas', 
    'suyo', 'suya', 'suyos', 'suyas', 'nuestro', 'nuestra', 'nuestros', 'nuestras', 
    'vuestro', 'vuestra', 'vuestros', 'vuestras', 'esos', 'esas', 'estoy', 'estás', 
    'está', 'estamos', 'estáis', 'están', 'esté', 'estés', 'estemos', 'estéis', 'estén', 
    'estaré', 'estarás', 'estará', 'estaremos', 'estaréis', 'estarán', 'estaría', 
    'estarías', 'estaríamos', 'estaríais', 'estarían', 'estaba', 'estabas', 'estábamos', 
    'estabais', 'estaban', 'estuve', 'estuviste', 'estuvo', 'estuvimos', 'estuvisteis', 
    'estuvieron', 'estuviera', 'estuvieras', 'estuviéramos', 'estuvierais', 'estuvieran', 
    'estuviese', 'estuvieses', 'estuviésemos', 'estuvieseis', 'estuviesen', 'estando', 
    'estado', 'estada', 'estados', 'estadas', 'estad'
]
def remove_accents(text):
    
    result = re.sub(
        r'[áéíóúÁÉÍÓÚ]',
        lambda match: {
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
            'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'
        }[match.group()],
        text
    )

    return result

data['text'] = [remove_accents(text) for text in data['text']]

print(data)
# Crear el vectorizador con la lista de stop words en español
vectorizer = CountVectorizer(stop_words=stop_words_spanish)


X = vectorizer.fit_transform(df['text']) # Ajustar y transformar los documentos


#print(vectorizer.get_feature_names_out())
#print(X.toarray())  



# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, df['category'], test_size=0.1, random_state=42) # 70% entrenamiento, 30% prueba ya qu ese declaro     https://www.youtube.com/watch?v=BUkqYGPnLZ8&ab_channel=ManifoldAILearning     explicacion de la funcion 
                                                                                                        # test_size=0.3 , lo q implica que el resto se completa con 0.7 para train.



# Crear y entrenar el clasificador Naive Bayes
clf = MultinomialNB()
clf.fit(X_train, y_train)



# Nuevos textos a clasificar en las categorías existentes
new_texts = [
    "El super auto azul explota contra una mesada",
    "Actualmente el costo de los lobo a aumentado en valor de dinero y de lo  delfín en el agua",
    "el mercado esta sangrando"
]
'''''
# Transformar los nuevos textos utilizando el mismo vectorizador
X_new = vectorizer.transform(new_texts)

# Predecir las categorías de los nuevos textos
new_predictions = clf.predict(X_new)
#print(new_predictions)

#categorias = ["animal","tecnologia", "deportes", "economia"]
'''


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
        

