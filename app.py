import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = '0123456789'


@app.route('/', methods=['GET', 'POST'], defaults={'port_num': 0})
@app.route('/<int:port_num>', methods=['GET', 'POST'])
def index(port_num):
    row_span = int(port_num) + 1
    return render_template('index.html', port_num=port_num, row_span=row_span)


if __name__ == '__main__':
    app.run()
