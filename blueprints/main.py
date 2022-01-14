from flask import Blueprint, render_template

main = Blueprint('main', __name__, url_prefix="/main")

@main.route('/')
def main_index():
    return render_template('home_index.html')

@main.route('/shopping')
def shopping_index():
    return render_template('/shoppings/shopping_index.html')