from flask import Blueprint, render_template

prueba_bp = Blueprint('prueba', __name__, template_folder='templates', url_prefix='/prueba') 

@prueba_bp.route('/', methods=['GET'])
def index():
    return render_template('prueba.html')