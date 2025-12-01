from flask import Blueprint, render_template, request, session

productos_bp = Blueprint(
    'productos',
    __name__, 
    template_folder='templates',
    static_folder='static'
    )


@productos_bp.route('/buscar')
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

