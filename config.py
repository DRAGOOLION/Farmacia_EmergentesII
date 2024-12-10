import sqlite3

def obtener_conexion():
    try:
        conn = sqlite3.connect('mi_farmacia.db')
        cursor = conn.cursor()

        # Crear las tablas
        cursor.execute('''CREATE TABLE IF NOT EXISTS Categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Productos (
            codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            descripcion TEXT,
            precio REAL,
            stock INTEGER,
            categoria_id INTEGER,
            FOREIGN KEY (categoria_id) REFERENCES Categorias(id)
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Empleados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            correo TEXT,
            contrasena TEXT
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            correo TEXT,
            direccion TEXT,
            contrasena TEXT,
            celular TEXT
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            fecha TEXT,
            total REAL,
            FOREIGN KEY (usuario_id) REFERENCES Pacientes(id)
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS DetalleVentas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            venta_id INTEGER,
            producto_id INTEGER,
            cantidad INTEGER,
            precio REAL,
            FOREIGN KEY (venta_id) REFERENCES Ventas(id),
            FOREIGN KEY (producto_id) REFERENCES Productos(codigo)
        )''')

        # Insertar datos iniciales (si es necesario)
        categorias = [
            ('Medicamentos',), ('Suplementos',), ('Cosméticos',), 
            ('Higiene',), ('Vitamínicos',), ('Limpieza',), 
            ('Alimentos',), ('Cuidado personal',), ('Herbales',), ('Naturales',)
        ]
        cursor.executemany("INSERT INTO Categorias (nombre) VALUES (?)", categorias)

        productos = [
            ('Paracetamol', 'Analgésico', 5.00, 100, 1),
            ('Ibuprofeno', 'Antiinflamatorio', 7.50, 50, 1),
            ('Vitamina C', 'Suplemento alimenticio', 3.00, 200, 2),
            ('Shampoo', 'Producto de higiene', 4.50, 150, 3),
            ('Crema facial', 'Cosmético', 10.00, 75, 4),
            ('Cloro', 'Limpiador', 2.00, 100, 6),
            ('Acelera Heridas', 'Crema para heridas', 12.00, 80, 5),
            ('Aceite de oliva', 'Aceite natural', 15.00, 120, 7),
            ('Gel antibacterial', 'Producto de higiene', 4.00, 200, 8),
            ('Té verde', 'Suplemento natural', 6.00, 50, 9)
        ]
        cursor.executemany("INSERT INTO Productos (nombre, descripcion, precio, stock, categoria_id) VALUES (?, ?, ?, ?, ?)", productos)

        empleados = [
            ('Juan', 'juan.empleado@ejemplo.com', '123'),
            ('Ana', 'ana.empleado@ejemplo.com', '234'),
            ('Carlos', 'carlos.empleado@ejemplo.com', '345'),
            ('Maria', 'maria.empleado@ejemplo.com', '456'),
            ('Pedro', 'pedro.empleado@ejemplo.com', '567'),
            ('Lucia', 'lucia.empleado@ejemplo.com', '678'),
            ('Elena', 'elena.empleado@ejemplo.com', '789'),
            ('Sergio', 'sergio.empleado@ejemplo.com', '890'),
            ('Raul', 'raul.empleado@ejemplo.com', '901'),
            ('Javier', 'javier.empleado@ejemplo.com', '012')
        ]
        cursor.executemany("INSERT INTO Empleados (nombre, correo, contrasena) VALUES (?, ?, ?)", empleados)

        pacientes = [
            ('Luis', 'luis.paciente@ejemplo.com', 'Av. Siempre Viva 123', '321', '1234567890'),
            ('Sofia', 'sofia.paciente@ejemplo.com', 'Calle Falsa 456', '432', '9876543210'),
            ('Hector', 'hector.paciente@ejemplo.com', 'Av. Principal 789', '543', '1122334455'),
            ('Claudia', 'claudia.paciente@ejemplo.com', 'Calle Secundaria 101', '654', '5566778899'),
            ('Miguel', 'miguel.paciente@ejemplo.com', 'Av. Libertador 202', '765', '6677889900'),
            ('Valeria', 'valeria.paciente@ejemplo.com', 'Calle Árbol 303', '876', '7788990011'),
            ('Andres', 'andres.paciente@ejemplo.com', 'Av. Norte 404', '987', '8899001122'),
            ('Daniela', 'daniela.paciente@ejemplo.com', 'Calle Sol 505', '098', '9900112233'),
            ('Fernando', 'fernando.paciente@ejemplo.com', 'Calle Luna 606', '210', '0011223344'),
            ('Adriana', 'adriana.paciente@ejemplo.com', 'Av. Este 707', '321', '2233445566')
        ]
        cursor.executemany("INSERT INTO Pacientes (nombre, correo, direccion, contrasena, celular) VALUES (?, ?, ?, ?, ?)", pacientes)

        conn.commit()
        print("Base de datos creada y datos insertados correctamente.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
        conn.close()

# Al final del archivo config.py agrega lo siguiente:
if __name__ == "__main__":
    obtener_conexion()
