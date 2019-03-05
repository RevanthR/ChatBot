from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello():
	return 'ChatBot on the way bois'

if __name__='__main__':
	app.run(debug=True)
