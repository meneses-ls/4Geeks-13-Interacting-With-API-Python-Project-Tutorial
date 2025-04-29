# - Importación de librerías:

import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# - Carga de variables de entorno:

load_dotenv()

# - Obtención de credenciales desde .env:

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# - Autenticación con la API de Spotify:

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# - Extracción de Canciones Populares del Artista:

artist_id = "6XyY86QOPPrYVGvF9ch6wz"
results = sp.artist_top_tracks(artist_id)

# - Procesamiento de Datos:

tracks = []
for track in results['tracks']:
    tracks.append({
        'name': track['name'],
        'popularity': track['popularity'],
        'duration_min': track['duration_ms'] / 60000
    })

# - Conversión a DataFrame:

df = pd.DataFrame(tracks)

# - Parámetros de graficación:

plt.scatter(df['duration_min'], df['popularity'])
plt.xlabel("Duración (minutos)")
plt.ylabel("Popularidad")
plt.title("Relación entre Duración y Popularidad")
plt.grid(True)

# - Visualización de gráfico:

plt.show()