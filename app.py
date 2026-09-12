from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/o-que-e")
def o_que_e():
    return render_template("o_que_e.html")

@app.route("/banner")
def banner():
    return render_template("banner.html")

@app.route("/videos")
def videos():
    return render_template("videos.html")

@app.route("/fotos")
def fotos():
    return render_template("fotos.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
