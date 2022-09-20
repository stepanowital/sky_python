# # catalog / views.py
#
# # Сперва импорттируем класс блюпринта
# from flask import Blueprint
#
# # Затем создаем новый блюпринт, выбираем для него имя
# catalog_blueprint = Blueprint('catalog_blueprint', __name__)
#
#
# # Создаем вьюшку, используя в декораторе блюпринт вместо app
# @catalog_blueprint.route('/catalog')
# def profile_page():
#     return "Я главная каталога"
#
#
# # Создаем вьюшку, используя в декораторе блюпринт вместо app
# @catalog_blueprint.route('/catalog/<cat>')
# def category_page(cat):
#     return f"Я страничка каталога категории {cat}"


# catalog/views.py

# Добавим импорт шаблонизатора
from flask import render_template, Blueprint

# Добавим настройку папки с шаблонами
catalog_blueprint = Blueprint(
    'catalog_blueprint',
    __name__,
    template_folder='templates')


# Добавим render_template
@catalog_blueprint.route('/catalog')
def catalog_page():
    return render_template("main.html")


# Добавим render_template
@catalog_blueprint.route('/catalog/<cat>')
def category_page(cat):
    return render_template("category.html", cat=cat)


# Добавим render_template
@catalog_blueprint.route('/catalog/<cat>/<int:item>')
def item_page(cat, item):
    return render_template("item.html", cat=cat, item=item)
