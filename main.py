from flask import Flask, request, jsonify

from database import Country, State, Sight, Session

import dataset


app=Flask(__name__)

@app.route('/greeting')
def greeting():
	return jsonify({

		"messenge": "greeting"
		})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
	return "it's work"

def main():
	app.run(port=5000, debug=True)

if __name__ == '__main__':
	main()