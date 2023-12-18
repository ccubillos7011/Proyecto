import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('usuarios.db')

# Crear la tabla de usuarios si no existe
conn.execute('''CREATE TABLE IF NOT EXISTS usuarios
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT NOT NULL,
             password TEXT NOT NULL);''')

# Función para agregar un usuario a la base de datos
def add_user(username, password):
    conn.execute(f"INSERT INTO usuarios (username, password) VALUES ('{username}', '{password}');")
    conn.commit()

# Agregar un usuario a la base de datos
add_user('usuario1', 'contraseña1')

# Agregar otro usuario a la base de datos
add_user('usuario2', 'contraseña2')

# Función para validar el inicio de sesión de un usuario
def validate_user(username, password):
    cursor = conn.execute(f"SELECT * FROM usuarios WHERE username='{username}' AND password='{password}';")
    return len(cursor.fetchall()) > 0

# Validar el inicio de sesión de un usuario
if validate_user('usuario1', 'contraseña1'):
    print('Inicio de sesión exitoso')
else:
    print('Nombre de usuario o contraseña incorrectos')