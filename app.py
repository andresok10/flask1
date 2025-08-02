from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "hola mundo 10 20"

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5001, debug=True)
    app.run(debug=True)
 