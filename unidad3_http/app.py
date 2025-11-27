# select intrerprete de python i seleccionamos nuestro entorno virtual
from flask import Flask, render_template,jsonify, send_from_directory, request, redirect, url_for,session

# # .env + config.py I
# load_dotenv()

app = Flask(__name__)
app.secret_key = "key_sesion"
# app.config.from_object(Config)


# # .env + config.py II
# entorno = os.getenv("FLASK_ENV", "development")
# print("FLASK_ENV:", entorno)

# if entorno == "production":
#     app.config.from_object(ProdConfig)
#     print("production")
# else:
#     app.config.from_object(DevConfig)
#     print("development")

# if not app.config.get("SECRET_KEY"):
#     raise RuntimeError("El SECRET KEY no aparece")



@app.route('/')
def home():
    # return "¡Hola, mundo! Sergio LM y esta  es mi primera aplicación Flask."
   return render_template('index.html')


products = [
    {"name": "Fender Stratocaster", "category": "Electric Guitar", "price": 1299.99},
    {"name": "Gibson Les Paul Standard", "category": "Electric Guitar", "price": 2499.00},
    {"name": "Boss DS-1 Distortion", "category": "Effects Pedal", "price": 59.99},
    {"name": "Line 6 Spider V 60 MkII", "category": "Amplifier", "price": 299.99},
    {"name": "Ernie Ball Regular Slinky", "category": "Guitar Strings", "price": 6.99}
]


# test : http://localhost:5000/buscar2?producto=Fender Stratocaster&categoria=Electric Guitar
@app.route('/buscar2')
def buscar2():
    producto = request.args.get('producto')
    categoria = request.args.get('categoria')
    return f"Buscando {producto} en {categoria}"


@app.route('/procesar', methods=['POST'])
def procesar():
    producto = request.form.get('producto')
    categoria = request.form.get('categoria')
    precio = request.form.get('precio')
    # producto = request.form['producto']

    return f"Su nuevo producto '{producto.upper()}' se ha registrado!"



usuarios = [
    {"usuario": "jack", "password": "1234"},
    {"usuario": "admin", "password": "admin123"},
    {"usuario": "maria", "password": "qwerty"}
]

@app.route('/login', methods=['GET','POST'])
def login():

    mensaje = ""

    if request.method == 'POST':
        usuario = request.form.get('usuario')
        password = request.form.get('password')

    
        for u in usuarios:
            if u["usuario"] == usuario and u["password"] == password:
                # la parte de la session
                session['usuario'] = usuario
                
                return redirect(url_for('sesion'))
                # return render_template('sesion.html')
            

        mensaje = 'usuario o contraseña errónea'
        
    return render_template('login.html', mensaje=mensaje)
    


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    mensaje = ""

    if request.method == 'POST':
        nuevo_usuario = request.form.get('usuario')
        nueva_password = request.form.get('password')

    
        for u in usuarios:
            if u["usuario"] == nuevo_usuario:
                mensaje = "El usuario ya existe"
                return render_template('signin.html', mensaje=mensaje)
        
        usuarios.append({
            "usuario" : nuevo_usuario,
            "password": nueva_password
        })

        mensaje = "el usuario se registró correctamente. "
        return redirect(url_for('login'))
    
    return render_template('signin.html', mensaje=mensaje)



@app.route('/sesion')
def sesion():

    if 'usuario' not in session:
        return redirect(url_for(login))

    return render_template('sesion.html', usuario=session['usuario'])


@app.route('/buscar')
def buscar():
    producto_query = request.args.get('producto', '')

    resultados = []

    products = [
        {"id": 1, "name": "Fender Stratocaster", "category": "Electric Guitar", "price": 1299.99},
        {"id": 2, "name": "Gibson Les Paul", "category": "Electric Guitar", "price": 2499.00},
        {"id": 3, "name": "Boss DS-1 Distortion", "category": "Effects Pedal", "price": 59.99}
    ]

    for p in products:
        if producto_query.lower() in p["name"].lower():
            resultados.append(p)

    return render_template('buscar.html', producto_query=producto_query, resultados=resultados, usuario=session['usuario'])


# usuarios = [
#     {"id": 1, "nombre": "Ana"},
#     {"id": 2, "nombre": "Carlos"},
#     {"id": 3, "nombre": "Lucía"}
# ]


# @app.route('/usuarios')
# def listar_usuarios():
#     return jsonify(usuarios)


# @app.route('/usuarios/<int:id>')
# def obtener_usuario(id):
#     usuario = next((u for u in usuarios if u["id"] == id), None)
#     if usuario:
#         return jsonify(usuario)
#     return jsonify({"error": "Usuario no encontrado"}), 404

# @app.route('/home')
# def home():
#     rutas = [
#         ('HTML simple', '/html'),
#         ('Página personalizada', '/pagina'),
#         ('HTML con nombre', '/html/TuNombre'),
#         ('Producto con ID', '/producto/15'),
#         ('JSON simple', '/json'),
#         ('API Info', '/api/info'),
#         ('Acerca de', '/about'),
#         ('Lista de usuarios', '/usuarios'),
#         ('Usuario con ID', '/usuarios/1'),
#     ]
#     return render_template('home.html', rutas=rutas)


if __name__ == '__main__':
    app.run(debug=True)
