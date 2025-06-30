from flask import Flask, render_template

# pull request

app = Flask(__name__)

# routing 
@app.route("/")
def index():
    return render_template('top.html')

@app.route("/list")
def list():
    return render_template('list.html')

@app.route("/detail")
def detail():
    return render_template('detail.html')


if __name__ == '__main__':
    app.run()
 