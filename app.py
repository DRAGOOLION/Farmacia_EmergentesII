from flask import Flask, render_template, request, redirect, session
from db_functions import agregar_empleado, consultar_empleado, agregar_paciente, eliminar_paciente, obtener_paciente_por_id, actualizar_paciente, consultar_paciente

app = Flask(__name__)
# Definición de rutas.

@app.route('/')
def index_():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/acercade.html')
def acercade():
    return render_template('acercade.html')

@app.route('/contacto.html')
def contacto():
    return render_template('contacto.html')

@app.route('/productos.html')
def productos():
    return render_template('productos.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/control.html')
def control():
    pacientes = consultar_paciente()  # Usando la función del archivo db_functions.py
    return render_template('control.html', pacientes=pacientes)

@app.route('/register.html')
def register():
    return render_template('register.html')

# Método POST para registro de empleados
@app.route('/registro', methods=["POST"])
def registro():
    nombre = request.form["nombre"]
    correo = request.form["correo"]
    contrasena = request.form["contrasena"]
    agregar_empleado(nombre, correo, contrasena)  # Usando la función del archivo db_functions.py
    return redirect('login.html')

# Método POST para el login de empleados
@app.route('/controluser', methods=["GET", "POST"])
def controluser():
    if request.method == "POST":
        nombre = request.form["nombre"]
        contrasena = request.form["contrasena"]
        
        empleado = consultar_empleado(nombre, contrasena)  # Usando la función del archivo db_functions.py
        
        if empleado:
            session['nombre'] = nombre  # Guardar nombre en sesión si es necesario
            return redirect('/control')  # Redirigir a la página de control, que sería gestionada por una ruta de Flask
        else:
            return "Credenciales incorrectas", 401  # Si no se encuentran las credenciales
    
    return render_template("login.html")  # Mostrar el formulario de login

# Guardar paciente (POST)
@app.route("/guardar_paciente", methods=["POST"])
def guardar_paciente():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    correo = request.form["correo"]
    direccion = request.form["direccion"]
    celular = request.form["celular"]
    agregar_paciente(nombre, apellido, correo, direccion, celular, request.form["contrasena"])  # Usando la función del archivo db_functions.py
    return redirect("/control.html")

# Eliminar paciente (POST)
@app.route("/eliminar_paciente", methods=["POST"])
def eliminar_paciente_route():
    eliminar_paciente(request.form["id"])  # Esta es la función que interactúa con la base de datos
    return redirect("/control.html")

# Editar paciente (GET)
@app.route("/editar_paciente/<int:id>")
def editar_paciente(id):
    paciente = obtener_paciente_por_id(id)  # Usando la función del archivo db_functions.py
    return render_template("editarpaciente.html", paciente=paciente)

# Actualizar paciente (POST)
@app.route("/actualizar_paciente", methods=["POST"])
def actualizar_paciente():
    id = request.form["id"]
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    correo = request.form["correo"]
    direccion = request.form["direccion"]
    celular = request.form["celular"]
    contrasena = request.form["contrasena"]
    actualizar_paciente(nombre, apellido, correo, direccion, celular, contrasena, id)  # Usando la función del archivo db_functions.py
    return redirect("/control.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
