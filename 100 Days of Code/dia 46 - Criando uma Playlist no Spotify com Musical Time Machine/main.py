import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# URL da Billboard Hot 100.
URL = "https://www.billboard.com/charts/hot-100/"

# Solicita ao usuário uma data no formando AAAA-MM-DD.
date = input("Para qual ano você quer viajar? Digite a data neste formato [AAAA-MM-DD]: ")

# Envia uma solicitação para a URL da Billboard Hot 1000 com a data inserida.
response = requests.get(URL + date)

# Analisa o conteúdo da página usando BeautifulSoup.
soup = BeautifulSoup(response.text, "html.parser")

# Extrai a lista de músicas da página, limpando espaços em branco e tabulações.
musics = [data.string.replace("\n", "").replace("\t", "") for data in soup.select(selector="li h3") if data.string]

# Define o endpoint da API do Spotify e as credenciais de cliente.
SPOTIFY_ENDPOINT = "https://api.spotify.com/v1"
CLIENT_ID = "YOUR CLIENT ID"
CLIENT_SECRET = "YOUR CLIENT SECRET"

# Autentica o aplicativo Spotify e identifica o usuário atual.
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

# Armazena o ID do usuário.
user_id = sp.current_user()["id"]

# Contador de músicas não encontradas.
not_found_musics = 0
# Lista com os URI das músicas.
music_links = list()
# Loop para cada música na lista de músicas.
for music in musics:
    try:
        # Pesquisa a música correspondente no Spotify.
        search = sp.search(q=f"track:{music} year:{date[0:4]}", limit=1, type="track")
        # Adiciona o link da música à lista de links.
        music_links.append(search["tracks"]["items"][0]["uri"].replace("spotify:track:", ""))
    except IndexError:
        # Incrementa o contador de músicas não encontradas.
        not_found_musics += 1
        continue
else:
    # Imprime o número de músicas não encontradas.
    print(f"{not_found_musics} Música(s) Não Encontrada(s)!\n")

# Cria uma playlist vazia no Spotify.
playlist = sp.user_playlist_create(user=user_id, name=f"100 Melhores Músicas de {date}", public=False)
# Adiciona as músicas na playlist.
sp.playlist_add_items(playlist_id=playlist["id"], items=music_links)




