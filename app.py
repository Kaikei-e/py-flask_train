from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/title/<title>')

def title(title):
    return render_template('index.html', title=title)

@app.route('/hoge')

def hoge():
    return 'hoge!'