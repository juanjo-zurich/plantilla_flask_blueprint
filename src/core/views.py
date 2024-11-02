
from flask import Blueprint, render_template

core_bp = Blueprint('core',__name__, template_folder='templates', url_prefix='/')

@core_bp.route('/', methods=['GET'])
def index():
    return render_template('core.html')