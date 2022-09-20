from flask import Flask, send_from_directory


app = Flask(__name__)

@app.route("/usatic/<path:path>")
def static_dir(path):
    return send_from_directory("usatic", path)

app.run()