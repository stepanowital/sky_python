from flask import Flask, request


app = Flask(__name__)

# Ограничиваем размер файла здесь
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024


@app.route('/')
def page_form():
    """ Эта вьюшка показывает форму, которая отправляет файлы"""
    form_content = """
    <form action="/upload" method="post" enctype="multipart/form-data">
    <input type="file" name="picture">
    <input type="submit" value="Отправить">
    </form>
    """
    return form_content


@app.route('/upload', methods=['POST'])
def page_upload():
    """ Эта вьюшка обрабатывает форму"""

    # Получаем объект картинки из формы
    picture = request.files.get("picture")

    # Получаем имя файла у загруженного фала
    filename = picture.filename

    # Сохраняем картинку под родным именем в папку uploads
    picture.save(f"/Uploads/{filename}")

    return f"Загружен и сохранен файл"

@app.errorhandler(413)
def page_not_found(e):
    return "<h1>Файл большеват</h1><p>Поищите поменьше, плиз!</p>", 413

app.run(host='192.168.1.115', port=5000)



# ПРОВЕРКА КОРРЕКТНОСТИ ФАЙЛОВ

# # Создаем множество расширений
#
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
#
# def is_filename_allowed(filename):
# 	extension = filename.split(".")[-1]
# 	if extension in ALLOWED_EXTENSIONS:
# 		return True
# 	return False
#
#
# # Получаем файл
# picture = request.files.get("picture")
#
# # Получаем имя файла у загруженного файла
# filename = picture.filename
#
# # Проверяем допустимость имени файла
# if is_filename_allowed(filename):
#
# 	picture.save(f"./uploads/{filename}")
#
# 	return "Файл сохранен"
#
# else:
#   extension = filename.split(".")[-1]
# 	return f"Тип файлов {extension} не поддерживается"
