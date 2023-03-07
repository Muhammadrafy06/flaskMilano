from flask import Flask,render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template("index.html")

@app.route('/descrizione', methods=['GET'])
def bye_world():
    return render_template("testo.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)