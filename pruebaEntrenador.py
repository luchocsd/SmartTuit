import joblib 
from entrenador import remove_accents
import os

save_directory = 'Projecto Investigacion/SmartTuit/ModeloEntrenado'  # Reemplaza esto con la ruta a tu carpeta

# Crear la carpeta si no existe
os.makedirs(save_directory, exist_ok=True)

# Guardar el modelo entrenado
model_path = os.path.join(save_directory, 'modelo_entrenado.pkl')
vectorizer_path = os.path.join(save_directory, 'vectorizador.pkl')

clf = joblib.load(model_path)

# Cargar el vectorizador
vectorizer = joblib.load(vectorizer_path)


# Nuevos textos a clasificar en las categorías existentes
new_texts = [
"esta semana los valores han disminuido en la bolsa de valores",
"Dólar Blue bajó 0,37% y cerró el día a $1.345,00. La brecha con el Dólar Oficial desciende al 36,9%",
"Sería: LANZARON... en plural, presimiente. En todo caso, ud y su recua,aman el decrecimiento económico. Por algo se ha encargado de ahorcar fiscal y regulatoriamente a los empresarios y ha acabado con la inversión privada porque no entiende que es ella, la que mueve la economía",
"Dólar hoy: el blue toca el valor más bajo desde junio y el Merval acumula en dos semanas un alza del 22 en dólares",
"dólar único, nominalmente estable, realista en valor real. Un sólo golpe inflacionario adicional (si por ej. se unificara en $1.500 o $ 2.000).  Menem estabilizó en $650, falló, y terminó estabilizando en $10,000.  Quince veces más!!!!!   No habría que dramatizar si se lograra unificación al doble que el oficial (ó  50% más que el CCL).Eficiencia: por otro carril.",
"Los niños y niñas de la escuela primaria de la localidad de El Cóndor, en Viedma, Río",
"La provincia decidio que los maestros de escuelas publicas no pueden hacer paro",
#Si no le pongo escuelas publicas, el porcentaje de que sea de educacion es mucho mas bajo
"El jueves se estrena en cartelera del cine DeadPool 3",
"La pelicula Deadpool vs Wolverine es de las mas taquilleras del año",#No tiene buen porcentaje de entretenimiento
"el otro dia me cocine un plato al horno con papas y me quedo riquisimo",
"la adminisitracion de milei esta siendo muy criticada por la oposicion",

]

new_texts = [remove_accents(text) for text in new_texts]

new_X = vectorizer.transform(new_texts)

# Obtener las probabilidades de las categorías
probabilities = clf.predict_proba(new_X)
prediccion =clf.predict(new_X)

for i in range(len(new_texts)):

    print("--Elemento ",i,"--")
    print("\033[92m",new_texts[i],"\033[0m")
    category_probabilities = {category: prob for category, prob in zip(clf.classes_, probabilities[i])}

    # Imprimir las probabilidades de cada categoría
    print("Probabilidades de categorías:")
    for category, prob in category_probabilities.items():
        print(f"{category}: {prob * 100:.2f}%")
    print("\033[91m",prediccion[i],"\033[0m")
    