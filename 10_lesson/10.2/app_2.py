from flask import Flask

app = Flask(__name__)


@app.route("/")
def page_test():
	return "Моё первое приложение"


app.run()
