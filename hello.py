from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello World1'
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',debug=True)
