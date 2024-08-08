from sklearn.feature_extraction.text import CountVectorizer

# Lista de stop words en español (palabras que en un articulo/tweet no tendrian valor para determinar el tipo)
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
    'estado', 'estada', 'estados', 'estadas', 'estad', 'detrás', 'delante', 'encima',
]


documents = [
    "El mercado de valores es un mercado de capitales en el que se negocian los valores de renta variable y fija de una forma estructurada, a través de la compraventa de valores, que son activos financieros que representan una parte alícuota del capital social de una empresa o una deuda.",
    
    "El equipo de futbol argentino logro vencer a su rival en la final de la copa Libertadores, donde logro una hazana al ganar el partido en los ultimos minutos.",
    
    "El actor de la serie de televisión logro ganar un premio por su actuación en la serie, donde se destaco por su actuación en la serie.",
    
    "El presidente de la nación anuncio que se llevara a cabo un plan de vacunación masiva en todo el país, donde se espera que se vacune a la mayor cantidad de personas posibles.",
]

#Crear un objeto de la clase CountVectorizer
vectorizer = CountVectorizer(stop_words=stop_words_spanish)

# Ajustar y transformar los documentos
X = vectorizer.fit_transform(documents)

# Mostrar las palabras que tienen valor y determinan el tipo del tweet
print(vectorizer.get_feature_names_out())
#Mostrar la matriz de frecuencia de palabras que tienen validez en cada tweet.
print(X.toarray())  