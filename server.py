from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hola():
    return render_template("index.html", rag = 3)

@app.route('/play')
def play():
    return render_template("index.html", rag = 3)

@app.route('/play/<int:rag>')
def play2(rag):
    return render_template("index.html", rag = rag)

@app.route('/play/<int:rag>/<string:color>')
def play3(rag, color):
    return render_template("index.html", rag = rag, color = color)

if __name__ == "__main__":
    app.run(debug=True)