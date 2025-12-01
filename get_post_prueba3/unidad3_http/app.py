# select intrerprete de python i seleccionamos nuestro entorno virtual

# flask 
from flask import Flask, render_template,jsonify, send_from_directory, request, redirect, url_for,session
# blueprints
from productos.rutas import productos_bp
from usuarios.rutas import usuarios_bp
from main.rutas import main_bp
# .env config.py
from dotenv import load_dotenv
load_dotenv()
from config import Config, ProdConfig, DevConfig
import os

app = Flask(__name__)
# para session
app.secret_key = "key_sesion"
# blueprints II
app.register_blueprint(productos_bp,url_prefix='/productos')
app.register_blueprint(usuarios_bp)
app.register_blueprint(main_bp)
# config II
app.config.from_object(Config)


# .env + config.py III
entorno = os.getenv("FLASK_ENV", "development")
print("FLASK_ENV:", entorno)

if entorno == "production":
    app.config.from_object(ProdConfig)
    print("production")
else:
    app.config.from_object(DevConfig)
    print("development")

if not app.config.get("SECRET_KEY"):
    raise RuntimeError("El SECRET KEY no aparece")



if __name__ == '__main__':
    app.run(debug=True)
