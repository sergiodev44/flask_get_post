from flask import Blueprint, render_template, request, session,redirect, url_for, jsonify

inspector_bp = Blueprint(
    'inspector',
    __name__, 
    template_folder='templates',
    static_folder='static'
    )



@inspector_bp.route('/my_gets')
def my_gets2():
    return render_template('para_gets.html')

@inspector_bp.route('/resumen', methods=['POST'])
def my_gets3():

    if request.method == 'POST':
        resultado = {
            "method" : request.method,
            "args" : request.args,
            "from2" : request.form,
            "files" : request.files,
            "user-agent" : request.headers.get('User-Agent'),
            "remote addr (ip)" : request.remote_addr,
            "url" : request.url
        }
        return render_template('inspector_resultado.html', resultado=resultado)

    