from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello world</h1><a href="/sida1">Sida 1</a> <a href="/sida2">Sida 2</a>'

@app.route('/sida1')
def sida1():
	return '<h1>Sida 1</h1><a href="/">Hello world</a> <a href="/sida2">Sida 2</a>'

@app.route('/sida2')
def sida2():
	return '<h1>Sida 2</h1><a href="/">Hello world</a> <a href="/sida1">Sida 1</a>"'

if __name__ == "__main__":
	app.run(debug=True)