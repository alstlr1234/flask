from flask import Flask, send_from_directory, render_template

app = Flask(__name__)
openai.api_key = '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'
@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def index():
    return send_from_directory('templates',"index.html")

@app.route('/<path:name>')
def start(name):
    return send_from_directory('templates',name)

@app.route("/post")
def index2():
    return send_from_directory('templates',"index2.html")

@app.route("/post")
def load_index2():
    return render_template("index2.html")

@app.route("/post2")
def index3():
    return send_from_directory('templates',"index3.html")

@app.route("/post2")
def load_index3():
    return render_template("index3.html")

@app.route("/post3")
def index4():
    return send_from_directory('templates',"index4.html")

@app.route("/post3")
def load_index4():
    return render_template("index4.html")
