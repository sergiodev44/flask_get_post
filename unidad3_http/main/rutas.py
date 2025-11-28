from flask import Blueprint, render_template, request, session

main_bp = Blueprint(
    'main',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@main_bp.route('/')
def home():
    return render_template('index.html')
