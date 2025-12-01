from flask import Blueprint, render_template, request, session,redirect, url_for

main_bp = Blueprint(
    'main',
    __name__, 
    template_folder='templates',
    static_folder='static'
    )


@main_bp.route('/')
def home():
    # return "¡Hola, mundo! Sergio LM y esta  es mi primera aplicación Flask."
   return render_template('index.html')

@main_bp.route('/ir_home')
def ir_home():
    # return "¡Hola, mundo! Sergio LM y esta  es mi primera aplicación Flask."
   return redirect(url_for('main.home'))

@main_bp.route('/sheesh')
def boom():
    return 1 / 0  