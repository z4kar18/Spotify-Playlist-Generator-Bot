import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Configuración de la API de Spotify
SPOTIPY_CLIENT_ID = "b890cab76f124cfa874f12305434a9e4"
SPOTIPY_CLIENT_SECRET = "08b75047705d4799b0f7a535ad9a0164"
SPOTIPY_REDIRECT_URI = "http://localhost:8888/callback"
SCOPE = "playlist-modify-public playlist-read-private"

# Autenticación
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=SCOPE
))

def search_artist_by_name(artist_name):
    """Busca artistas por nombre y permite seleccionar uno."""
    results = sp.search(q=f"artist:{artist_name}", type="artist", limit=10)
    artists = results['artists']['items']

    if not artists:
        print(f"No se encontraron artistas con el nombre: {artist_name}")
        return None

    print("\nArtistas encontrados:")
    for idx, artist in enumerate(artists):
        print(f"{idx + 1}. {artist['name']} (Género: {', '.join(artist['genres'])})")

    choice = input("\nSelecciona el número del artista correcto: ")
    try:
        selected_index = int(choice) - 1
        return artists[selected_index]
    except (ValueError, IndexError):
        print("Selección inválida. Por favor, intenta de nuevo.")
        return search_artist_by_name(artist_name)

def list_user_playlists():
    """Lista las playlists del usuario y permite seleccionar una."""
    playlists = sp.current_user_playlists()
    playlist_options = []

    print("\nTus playlists:")
    for idx, playlist in enumerate(playlists['items']):
        print(f"{idx + 1}. {playlist['name']} (ID: {playlist['id']})")
        playlist_options.append(playlist)

    choice = input("\nSelecciona el número de la playlist: ")
    try:
        selected_index = int(choice) - 1
        return playlist_options[selected_index]
    except (ValueError, IndexError):
        print("Selección inválida. Por favor, intenta de nuevo.")
        return list_user_playlists()

def get_tracks_by_artist_from_playlist(playlist_id, artist_name):
    """Obtiene las canciones de un artista específico dentro de una playlist."""
    tracks = sp.playlist_tracks(playlist_id)
    artist_tracks = []

    for idx, item in enumerate(tracks['items']):
        track = item['track']
        if any(artist_name.lower() in artist['name'].lower() for artist in track['artists']):
            artist_tracks.append({
                'index': idx + 1,
                'track_id': track['id'],
                'name': track['name'],
                'artist': ', '.join([artist['name'] for artist in track['artists']])
            })

    return artist_tracks

def remove_tracks_from_playlist(playlist_id, track_ids):
    """Elimina canciones de una playlist."""
    sp.playlist_remove_all_occurrences_of_items(playlist_id, track_ids)
    print("Canciones eliminadas con éxito.")

def select_tracks_to_remove(tracks):
    """Permite seleccionar qué canciones eliminar."""
    print("\nCanciones del artista encontradas en la playlist:")
    for track in tracks:
        print(f"{track['index']}. {track['name']} - {track['artist']}")

    print("\nOpciones:")
    print("1. Escribe 'todas' para eliminar todas las canciones.")
    print("2. Escribe un rango (ejemplo: 2-5) para eliminar canciones entre esas posiciones.")
    print("3. Escribe números específicos separados por espacios (ejemplo: 1 3 4).")

    choice = input("\nSelecciona qué canciones eliminar: ").strip().lower()

    if choice == "todas":
        return [track['track_id'] for track in tracks]
    elif "-" in choice:
        try:
            start, end = map(int, choice.split('-'))
            return [tracks[i - 1]['track_id'] for i in range(start, end + 1)]
        except (ValueError, IndexError):
            print("Rango inválido. Intenta de nuevo.")
            return select_tracks_to_remove(tracks)
    else:
        try:
            indices = list(map(int, choice.split()))
            return [tracks[i - 1]['track_id'] for i in indices]
        except (ValueError, IndexError):
            print("Selección inválida. Intenta de nuevo.")
            return select_tracks_to_remove(tracks)

def get_artist_tracks(artist_id):
    """Obtiene todas las canciones de un artista usando su ID."""
    tracks = []
    results = sp.artist_top_tracks(artist_id)
    tracks.extend([track['id'] for track in results['tracks']])

    # Busca álbumes y recupera canciones
    albums = sp.artist_albums(artist_id, album_type='album,single', limit=50)
    album_ids = [album['id'] for album in albums['items']]
    
    for album_id in album_ids:
        album_tracks = sp.album_tracks(album_id)
        tracks.extend([track['id'] for track in album_tracks['items']])

    return list(set(tracks))  # Evita duplicados

def add_tracks_to_playlist(playlist_id, track_ids):
    """Agrega canciones a una playlist en bloques de 100."""
    for i in range(0, len(track_ids), 100):
        batch = track_ids[i:i + 100]
        sp.playlist_add_items(playlist_id=playlist_id, items=batch)
    print("Canciones añadidas a la playlist.")

def main():
    print("¿Qué acción deseas realizar?")
    print("1. Añadir canciones de un artista a una playlist.")
    print("2. Eliminar canciones de un artista de una playlist.")

    choice = input("\nSelecciona una opción (1 o 2): ").strip()

    if choice == "1":
        # Añadir canciones de un artista
        artist_name = input("Ingresa el nombre del artista: ")
        selected_artist = search_artist_by_name(artist_name)
        if not selected_artist:
            return

        artist_id = selected_artist['id']
        playlist = list_user_playlists()
        playlist_id = playlist['id']

        track_ids = get_artist_tracks(artist_id)
        if not track_ids:
            print(f"No se encontraron canciones para el artista: {selected_artist['name']}")
            return

        add_tracks_to_playlist(playlist_id, track_ids)

    elif choice == "2":
        # Eliminar canciones de un artista
        playlist = list_user_playlists()
        playlist_id = playlist['id']
        artist_name = input("Ingresa el nombre del artista: ")
        selected_artist = search_artist_by_name(artist_name)
        if not selected_artist:
            return

        artist_name = selected_artist['name']
        tracks = get_tracks_by_artist_from_playlist(playlist_id, artist_name)

        if not tracks:
            print(f"No se encontraron canciones de {artist_name} en la playlist.")
            return

        track_ids_to_remove = select_tracks_to_remove(tracks)
        if not track_ids_to_remove:
            print("No se seleccionaron canciones para eliminar.")
            return

        remove_tracks_from_playlist(playlist_id, track_ids_to_remove)

    else:
        print("Opción inválida. Por favor, selecciona 1 o 2.")
        main()

if __name__ == "__main__":
    main()
