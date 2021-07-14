from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<name>", methods=['GET', 'POST'])
def home(name):
    return render_template('homepage.html', name=name)

@app.route("/looping/<int:number>")
def loop(number):
    return render_template('looping.html', number=number)

@app.route('/image', methods=['GET', 'POST'])
def imge():
    return render_template('img.html')


if __name__ == '__main__':
    app.debug=True
    app.run()
