from flask import Blueprint, render_template, request, session
from psycopg2.extras import RealDictCursor
from ..db import get_db_connection

productos_bp = Blueprint(
    'productos',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@productos_bp.route('/buscar')
def buscar():
    producto_query = request.args.get('producto', '')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
        'SELECT id, name, category, price FROM products WHERE name ILIKE %s',
        (f'%{producto_query}%',)
    )

    resultados = cur.fetchall()
    cur.close()
    conn.close()

    return render_template(
        'buscar.html',
        producto_query=producto_query,
        resultados=resultados,
        usuario=session.get('usuario', 'default_user')
    )
