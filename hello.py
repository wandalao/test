from flask import Flask
import os
app = Flask(__name__)
@app.route('/')
def index():
    return '<div style="color:red;">Hello World1</div>'

def writePid():
    pid = str(os.getpid())
    f = open('athena.pid', 'w')
    f.write(pid)
    f.close()
if __name__ == '__main__':
    app.debug = True
    writePid()
    app.run(host='0.0.0.0',debug=True)
