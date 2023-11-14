from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
@app.route("/")
def hallo():
     s=3
     print (s)
     m = "/static/1.jpg"
     s=input('s=')

     return render_template('index.html',s=s,m=m, j=hallo())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5006)