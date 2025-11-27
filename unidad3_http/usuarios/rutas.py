from flask import Blueprint, render_template, request, session, url_for, redirect

usuarios_bp = Blueprint(
    'usuarios',
    __name__, 
    template_folder='templates',
    static_folder='static'
    )

# para sustituir después con proper db
usuarios = [
    {"usuario": "jack", "password": "1234"},
    {"usuario": "admin", "password": "admin123"},
    {"usuario": "maria", "password": "qwerty"}
]

@usuarios_bp.route('/login', methods=['GET','POST'])
def login():

    mensaje = ""

    if request.method == 'POST':
        usuario = request.form.get('usuario')
        password = request.form.get('password')

    
        for u in usuarios:
            if u["usuario"] == usuario and u["password"] == password:
                # la parte de la session
                session['usuario'] = usuario
                
                return redirect(url_for('usuarios.sesion'))
                # return render_template('sesion.html')
            

        mensaje = 'usuario o contraseña errónea'
        
    return render_template('login.html', mensaje=mensaje)
    


@usuarios_bp.route('/signin', methods=['GET', 'POST'])
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
        return redirect(url_for('usuarios.login'))
    
    return render_template('signin.html', mensaje=mensaje)


@usuarios_bp.route('/sesion')
def sesion():

    if 'usuario' not in session:
        return redirect(url_for('usuarios.login'))

    return render_template('sesion.html', usuario=session['usuario'])



# Esto es para los ejemplos de prueba

products = [
    {"name": "Fender Stratocaster", "category": "Electric Guitar", "price": 1299.99},
    {"name": "Gibson Les Paul Standard", "category": "Electric Guitar", "price": 2499.00},
    {"name": "Boss DS-1 Distortion", "category": "Effects Pedal", "price": 59.99},
    {"name": "Line 6 Spider V 60 MkII", "category": "Amplifier", "price": 299.99},
    {"name": "Ernie Ball Regular Slinky", "category": "Guitar Strings", "price": 6.99}
]


# test : http://localhost:5000/buscar2?producto=Fender Stratocaster&categoria=Electric Guitar
@usuarios_bp.route('/buscar2')
def buscar2():
    producto = request.args.get('producto')
    categoria = request.args.get('categoria')
    return f"Buscando {producto} en {categoria}"


@usuarios_bp.route('/procesar', methods=['POST'])
def procesar():
    producto = request.form.get('producto')
    categoria = request.form.get('categoria')
    precio = request.form.get('precio')
    # producto = request.form['producto']

    return f"Su nuevo producto '{producto.upper()}' se ha registrado!"
