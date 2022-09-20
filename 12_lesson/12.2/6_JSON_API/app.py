# from flask import Flask, jsonify
#
# app = Flask(__name__)
#
# # Чтобы заработала кириллица
# app.config['JSON_AS_ASCII'] = False
#
#
# @app.route("/")
# def get_json():
#     data = {"name": "Алиса"}
#     return jsonify(data)
#     # return data
#
# app.run()


from flask import Flask, jsonify

app = Flask(__name__)

# Чтобы заработала кириллица
app.config['JSON_AS_ASCII'] = False

list_of_words = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]


@app.route("/")
def get_json():
    return jsonify(list_of_words)

app.run()