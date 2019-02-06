from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def get_stream():
    message = "Quarto Benjamin"
    return render_template('stream.html', message=message)


if __name__ == "__main__":  
    app.run(debug=True)