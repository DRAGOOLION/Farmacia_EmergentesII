import sqlite3

# Obtener la conexión con la base de datos
def obtener_conexion():
    # Ruta fija al archivo de la base de datos
    conexion = sqlite3.connect('mi_farmacia.db')
    conexion.row_factory = sqlite3.Row  # Para acceder a las columnas por nombre
    return conexion

# Funciones para manejar empleados
def agregar_empleado(nombre, correo, contrasena):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Empleados (nombre, correo, contrasena) VALUES (?, ?, ?)", 
                   (nombre, correo, contrasena))
    conexion.commit()
    conexion.close()

def consultar_empleado(nombre, contrasena):
    try:
        conn = sqlite3.connect("mi_farmacia.db")
        cursor = conn.cursor()

        # Suponiendo que las credenciales de los empleados están en una tabla llamada 'empleados'
        cursor.execute("SELECT * FROM empleados WHERE nombre = ? AND contrasena = ?", (nombre, contrasena))
        empleado = cursor.fetchone()

        conn.close()
        return empleado
    except sqlite3.Error as e:
        print(f"Error al consultar el empleado: {e}")
        return None

# Funciones para manejar pacientes
def consultar_paciente():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, correo, direccion, celular FROM Pacientes")
    pacientes = cursor.fetchall()  # Obtener todos los resultados
    conexion.close()
    return pacientes

def obtener_paciente_por_id(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, correo, direccion, celular FROM Pacientes WHERE id = ?", (id,))
    paciente = cursor.fetchone()  # Obtener el primer resultado
    conexion.close()
    return paciente

def agregar_paciente(nombre, correo, direccion, celular, contrasena):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Pacientes (nombre, correo, direccion, celular, contrasena) VALUES (?, ?, ?, ?, ?, ?)", 
                   (nombre, correo, direccion, celular, contrasena))
    conexion.commit()
    conexion.close()

def eliminar_paciente(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Pacientes WHERE id = ?", (id,))
    conexion.commit()
    conexion.close()

def actualizar_paciente(nombre, correo, direccion, celular, contrasena, id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE Pacientes SET nombre = ?, correo = ?, direccion = ?, celular = ?, contrasena = ? WHERE id = ?", 
                   (nombre, correo, direccion, celular, contrasena, id))
    conexion.commit()
    conexion.close()
    