from utils import *
from flask import Flask


DATA_SOURCE = "candidates.json"

candidates = load_candidates(DATA_SOURCE)

app = Flask(__name__)


@app.route("/")
def page_test():
	return get_all(candidates)


@app.route("/candidates/<int:uid>")
def page_profile(uid):
	return get_by_pk(candidates, uid)


@app.route("/skills/<skill>")
def page_skills(skill):
	return get_by_skill(candidates, skill)


app.run(debug=True)
