

from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World! from LU</p> "

    
@app.route("/greet")
def greet():
    return "<p>Hello Everyone,Enjoy coding!</p>"


if __name__=='__main__':

    app.run(debug=True)