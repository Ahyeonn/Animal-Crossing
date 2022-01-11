from flask import Blueprint, render_template

main = Blueprint('main', __name__, url_prefix="/")

@main.route('/')
def main_index():
    return render_template('home_index.html')

@main.route('about_AC')
def about_AC_index():
    return render_template('about_AC_index.html')

