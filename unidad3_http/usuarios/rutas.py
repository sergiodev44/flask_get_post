from flask import Blueprint, render_template, request, session, url_for, redirect
from ..db import get_db_connection

usuarios_bp = Blueprint(
    'usuarios',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@usuarios_bp.route('/login', methods=['GET','POST'])
def login():
    mensaje = ""

    if request.method == 'POST':
        usuario = request.form.get('usuario')
        password = request.form.get('password')

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM users WHERE usuario = %s AND password = %s', (usuario, password))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            session['usuario'] = usuario
            return redirect(url_for('usuarios.sesion'))

        mensaje = 'usuario o contraseña errónea'

    return render_template('login.html', mensaje=mensaje)


@usuarios_bp.route('/signin', methods=['GET', 'POST'])
def signin():
    mensaje = ""

    if request.method == 'POST':
        nuevo_usuario = request.form.get('usuario')
        nueva_password = request.form.get('password')

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('SELECT * FROM users WHERE usuario = %s', (nuevo_usuario,))
        if cur.fetchone():
            mensaje = "El usuario ya existe"
            cur.close()
            conn.close()
            return render_template('signin.html', mensaje=mensaje)

        cur.execute('INSERT INTO users (usuario, password) VALUES (%s, %s)',
                     (nuevo_usuario, nueva_password))
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for('usuarios.login'))

    return render_template('signin.html', mensaje=mensaje)


@usuarios_bp.route('/sesion')
def sesion():

    if 'usuario' not in session:
        return redirect(url_for('usuarios.login'))

    return render_template('sesion.html', usuario=session['usuario'])
