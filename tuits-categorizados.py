# Lista de tuplas con 10 tuits por cada categoría
tweets = [
    # Economía
    ("La inflación afecta a todos los sectores económicos", "economía"),
    ("El mercado bursátil cerró con pérdidas hoy", "economía"),
    ("El dólar sigue subiendo en los mercados internacionales", "economía"),
    ("El gobierno anuncia nuevas reformas fiscales", "economía"),
    ("El desempleo ha disminuido este trimestre", "economía"),
    ("La inversión extranjera en el país ha crecido", "economía"),
    ("Las exportaciones han aumentado en el último año", "economía"),
    ("La economía global enfrenta una recesión", "economía"),
    ("El precio del petróleo ha caído significativamente", "economía"),
    ("Las criptomonedas han ganado popularidad", "economía"),
    
    # Deportes
    ("El equipo ganó el partido en los últimos minutos", "deportes"),
    ("Los Juegos Olímpicos comenzarán el próximo mes", "deportes"),
    ("El fútbol es el deporte más popular del mundo", "deportes"),
    ("El jugador estableció un nuevo récord", "deportes"),
    ("El campeonato de tenis está en su fase final", "deportes"),
    ("La liga de baloncesto ha sido muy competitiva este año", "deportes"),
    ("El maratón atrajo a corredores de todo el mundo", "deportes"),
    ("El ciclismo de montaña es un deporte emocionante", "deportes"),
    ("El equipo nacional se clasificó para el Mundial", "deportes"),
    ("La natación es una excelente forma de ejercicio", "deportes"),
    
    # Animal
    ("Los elefantes son conocidos por su memoria", "animal"),
    ("El tigre es un felino en peligro de extinción", "animal"),
    ("Las aves migratorias recorren largas distancias", "animal"),
    ("El perro es considerado el mejor amigo del hombre", "animal"),
    ("Los gatos son animales muy independientes", "animal"),
    ("El león es conocido como el rey de la selva", "animal"),
    ("Los delfines son animales muy inteligentes", "animal"),
    ("Las abejas juegan un papel crucial en la polinización", "animal"),
    ("El canguro es un símbolo de Australia", "animal"),
    ("Las ballenas son los mamíferos más grandes del mundo", "animal")
]

# Ejemplo de acceso al segundo tuit en la lista
tweet_ejemplo = tweets[1]


print(tweet_ejemplo) # Salida: ('Los Juegos Olímpicos comenzarán el próximo mes', 'deportes')

#twwet_ejemplo[0] Salida: 'Los Juegos Olímpicos comenzarán el próximo mes'
#tweet_ejemplo[1] Salida: 'deportes'