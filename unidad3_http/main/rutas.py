from flask import Blueprint, render_template, request, session,redirect, url_for, jsonify, make_response
from datetime import datetime, timedelta
import time

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

@main_bp.route('/prueba')
def prueba_get():
    a = request.args.get('name')
    navegador = request.headers.get("User-Agent")
    idioma = request.headers.get("Accept-Language")
    ip = request.remote_addr
    return f"""
        el método {a} es {request.method}<br>
        {request.args.get('name')}<br>
        {request.path}<br>
        {request.url}<br>
        {request.full_path}<br>
        {navegador}<br>
        {idioma}<br>
        {ip}
        """

@main_bp.route('/prueba_req/', methods=['GET', 'POST'] )
def prueba_req():
        message = None

        tema = request.cookies.get("tema")
        name = request.form.get('name')

        if name == 'myles':
            message = 'yesssirr'
            return render_template('prueba_req.html', message=message, tema=tema)
        
        message = 'wrong name soldier'
        return render_template('prueba_req.html', message=message, tema=tema)


# probar with curl en la terminal
# curl -X POST  http://127.0.0.1:5000/prueba_post/ -H "Content-Type: application/json" -d '{"name":"myles"}'

@main_bp.route('/prueba_post/', methods=['POST'])
def prueba_json():
        if not request.method == 'POST':
             return {"error": "JSON required"}, 400
        
        data = request.get_json()
        name = data.get("name")

        if name == "myles":
             return {"message" : "spartan"}, 200
        else:
             return {"message" : "athenians"}, 200
        

@main_bp.route('/prueba_img/', methods=['GET','POST'])
def prueba_img():
        
        archivo = request.files.get("file")
        ok=None
        if archivo:
            archivo.save("./flask_get_post/get_post_prueba3/unidad3_http/static/img/ttesosanibfibv.png")
            ok="yes"

        return render_template('/prueba_img.html', ok=ok)


# http://127.0.0.1:5000/ejemplo_final?curso=DWES&tema=Flask
@main_bp.route('/ejemplo_final')
def ej_final():
    info = {
         "metodo": request.method,
         "parametros_get": request.args,
         "cabeceras": dict(request.headers),
         "user_agent": request.headers.get('User-Agent')

    }
    return jsonify(info)

# pruebas de cookies
@main_bp.route('/ver-cookies')
def cook_prefs0():
    tema = request.cookies.get('tema','claro')
    return f"tu tema actual es: {tema}"

@main_bp.route('/set-cookies')
def set_cookie():
     res = make_response("Cookie established")
     res.set_cookie("tema", "oscuro")
    #  res.set_cookie("tema", "oscuro", max_age=60*60*24)
    #  expires = datatime.now() + timedelta(days=7)
    #  res.set_cookie("tema", "oscuro", expires=expires)
     return res

# @main_bp.route('/seguridad')
# def set_cookie2():
#      res2 = make_response("seguridad establecidad")
#      res2.set_cookie(
#           "token", "123abc",
#           httponly=True,
#           secure=True,
#           samesite='Lax'
#      )

@main_bp.route('/borrar')
def borrar_cookie():
     resp = make_response("Cookie eliminado")
     resp.delete_cookie("tema")
     resp.delete_cookie("usuario")
     return resp



@main_bp.route('/elegir-tema')
def elegir_tema():
    return render_template('elegir_tema.html')

@main_bp.route('/guardar-tema', methods=["POST"])
def guardar_cookies():
    # version 1
    value = request.form.get("tema", "claro")
    res = make_response(redirect(url_for("usuarios.login")))
    res.set_cookie("tema", value, max_age=60*60*24)
    return res


    # # version 2 
    # value = request.form.get("tema")
    # res = make_response(f"cookies guardadas | {value}")
    # res.set_cookie("tema", value)

    # # opcion que yo hice con el redirect a /
    # time.sleep(4)
    # res.headers["Location"] = url_for("main.home")
    # res.status_code = 302



# ejercicios de cookies
@main_bp.route('/preferencias')
def cook_prefs():
    return render_template('preferencias.html')

@main_bp.route('/guardar-preferencias', methods=['POST'])
def cook_prefs2():
    tema = request.form.get("tema", "claro")
    font = request.form.get("font", "mediano")
    lang = request.form.get("lang", "es")

    res = make_response(redirect(url_for("main.home")))
    res.set_cookie("tema", tema)
    res.set_cookie("font", font)
    res.set_cookie("lang", lang)
    res.set_cookie(
          "token", "123abc",
          httponly=True,
          secure=True,
          samesite='Lax'
     )

    return res
    