import joblib
from entrenador import remove_accents
import os

# Rutas de archivos
save_directory = 'Projecto Investigacion/SmartTuit/ModeloEntrenado'
model_path = os.path.join(save_directory, 'modelo_entrenado.pkl')
vectorizer_path = os.path.join(save_directory, 'vectorizador.pkl')
input_file = 'frases_a_clasificar.txt'
output_file = 'resultados_clasificacion.py'

# Cargar el modelo y el vectorizador
clf = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Leer frases del archivo de entrada
from PorClasificar import frases

# Limpiar y transformar las frases
frasesLimpias = [remove_accents(frase) for frase in frases]


X = vectorizer.transform(frases)

# Obtener las probabilidades y predicciones
predicciones = clf.predict(X)

# Generar el contenido para el archivo .py
resultados_por_categoria = {}
for frase, categoria in zip(frases, predicciones):
    if categoria not in resultados_por_categoria:
        resultados_por_categoria[categoria] = []
    resultados_por_categoria[categoria].append(frase + "["+ categoria +"]" )

# Convertir el diccionario en una lista de listas
resultados = [resultados_por_categoria.get(categoria, []) for categoria in clf.classes_]

# Crear el archivo .py con el arreglo de resultados
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(f"resultados = {resultados}\n")

print(f"Clasificación completada. Resultados guardados en {output_file}")
