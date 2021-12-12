from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_index():  # put application's code here
    return render_template('index.html')


@app.route('/charts')
def render_charts():  # put application's code here
    return render_template('charts.html')


@app.route('/table')
def render_table():  # put application's code here
    return render_template('table.html')


if __name__ == '__main__':
    app.run()
