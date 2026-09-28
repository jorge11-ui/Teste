from flask import Flask, render_template
from livro import livros

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html", livros=livros)


if __name__ == "__main__":
    app.run(debug=True)