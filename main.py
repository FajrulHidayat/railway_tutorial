from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    hello = __hello()
    world = __world()
    return jsonify(message= hello+world)

def __hello():
    return "Hello"
    

def __world():
    return  "World"

if __name__ == '__main__':
    app.run(debug=True, port=9000)