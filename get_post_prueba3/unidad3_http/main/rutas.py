from flask import Blueprint, render_template, request, session,redirect, url_for, jsonify

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


@main_bp.route('/ejemplo_final')
def ej_final():
    info = {
         "metodo": request.method,
         "parametros_get": request.args,
         "cabeceras": dict(request.headers),
         "user_agent": request.headers.get('User-Agent')

    }
    return jsonify(info)
    