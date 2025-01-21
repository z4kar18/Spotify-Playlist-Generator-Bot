# Spotify Playlist Bot

## Descripción

El **Spotify Playlist Bot** es un script de Python que interactúa con la API de Spotify para gestionar playlists. Este bot permite:

1. **Añadir canciones de un artista específico a una playlist**.
2. **Eliminar canciones de un artista específico de una playlist**, con opciones para seleccionar canciones específicas, un rango, o todas las canciones del artista.

Es una herramienta ideal para automatizar la gestión de playlists y personalizar tu experiencia en Spotify.

---

## Características

### Añadir Canciones
- Busca canciones de un artista en Spotify.
- Muestra una lista de artistas coincidentes para seleccionar el correcto.
- Recupera todas las canciones del artista (incluyendo álbumes y sencillos).
- Permite agregar estas canciones a una playlist existente o crear una nueva.

### Eliminar Canciones
- Busca canciones de un artista dentro de una playlist.
- Lista las canciones encontradas para que puedas:
  - Eliminar todas.
  - Seleccionar un rango.
  - Elegir canciones específicas.

### Selección de Artistas
- Al buscar un artista, el bot muestra una lista con:
  - Nombres de los artistas.
  - Géneros asociados.
- Permite seleccionar el artista correcto para evitar confusiones.

---

## Requisitos

### Python
- **Python 3.7 o superior**.

### Bibliotecas
- `spotipy`

Instala las dependencias ejecutando:
```bash
pip install spotipy
```

---

## Configuración

1. **Crea una aplicación en el [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)**:
   - Obtén tu `Client ID` y `Client Secret`.
   - Configura `http://localhost:8888/callback` como Redirect URI.

2. **Configura las credenciales en el script**:
   - Reemplaza las siguientes variables con tus credenciales:
     ```python
     SPOTIPY_CLIENT_ID = "TU_CLIENT_ID"
     SPOTIPY_CLIENT_SECRET = "TU_CLIENT_SECRET"
     SPOTIPY_REDIRECT_URI = "http://localhost:8888/callback"
     ```

3. **Permisos Necesarios (Scopes)**:
   - El bot requiere los siguientes permisos:
     - `playlist-modify-public`
     - `playlist-read-private`

---

## Uso

Ejecuta el script:
```bash
python nombre_del_script.py
```

### Menú Principal
1. **Añadir canciones de un artista**.
2. **Eliminar canciones de un artista de una playlist**.

### Flujo de Uso
#### Añadir Canciones
- Ingresa el nombre del artista.
- Selecciona el artista correcto de la lista mostrada.
- Elige una playlist existente o crea una nueva.
- Las canciones del artista se agregarán a la playlist seleccionada.

#### Eliminar Canciones
- Selecciona una playlist.
- Ingresa el nombre del artista.
- Selecciona el artista correcto de la lista mostrada.
- Elige las canciones a eliminar:
  - Todas las canciones del artista.
  - Un rango de canciones.
  - Canciones específicas.

---

## Ejemplo

### Añadir canciones:
```
¿Qué acción deseas realizar?
1. Añadir canciones de un artista a una playlist.
2. Eliminar canciones de un artista de una playlist.

Selecciona una opción (1 o 2): 1
Ingresa el nombre del artista: Coldplay
Artistas encontrados:
1. Coldplay (Género: alternative rock, pop rock)
2. Coldrain (Género: metalcore, post-hardcore)
Selecciona el número del artista correcto: 1
Tus playlists:
1. Playlist de Ejemplo (ID: 123456)
2. Mi Playlist Favorita (ID: 654321)
Selecciona el número de la playlist: 1
Canciones añadidas a la playlist.
```

### Eliminar canciones:
```
¿Qué acción deseas realizar?
1. Añadir canciones de un artista a una playlist.
2. Eliminar canciones de un artista de una playlist.

Selecciona una opción (1 o 2): 2
Tus playlists:
1. Playlist de Ejemplo (ID: 123456)
2. Mi Playlist Favorita (ID: 654321)
Selecciona el número de la playlist: 1
Ingresa el nombre del artista: Coldplay
Artistas encontrados:
1. Coldplay (Género: alternative rock, pop rock)
2. Coldrain (Género: metalcore, post-hardcore)
Selecciona el número del artista correcto: 1
Canciones del artista encontradas en la playlist:
1. Yellow - Coldplay
2. Fix You - Coldplay
3. Viva La Vida - Coldplay

Opciones:
1. Escribe 'todas' para eliminar todas las canciones.
2. Escribe un rango (ejemplo: 2-3) para eliminar canciones entre esas posiciones.
3. Escribe números específicos separados por espacios (ejemplo: 1 3).

Selecciona qué canciones eliminar: 1 3
Canciones eliminadas con éxito.
```

---

## Contribuciones

Si deseas contribuir al proyecto, puedes:
- Reportar errores.
- Proponer nuevas funcionalidades.
- Mejorar la documentación.

---

## Licencia
Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

