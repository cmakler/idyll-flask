import os
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
POSTS_ROOT = os.path.join(APP_ROOT,'posts')

@app.route('/')
def hello_world():
    return render_template('index.html')

def open_markdown_file(open_file):
    with open(os.path.join(open_file), 'r') as datafile:
    	md = datafile.read().decode('utf-8').strip()
    	return md

@app.route('/posts/<path:path>')
def post(path):
    md = open_markdown_file(os.path.join(POSTS_ROOT, path + '.md'))
    return render_template('idyll.html', title='title', md=md, args=request.args)

if __name__ == '__main__':
    app.run()
