from flask import Flask, render_template
from dbConnector import UseDatabase

dbconfig = {'host': '127.0.0.1', 'user': 'root', 'password': '97082', 'database': 'oops'}

app = Flask(__name__)

@app.route('/')
def homepage() -> 'Html page':
    return render_template('homepage.html', activehome='active',css='static/homepagecss.css')

@app.route('/product')
def product() -> 'Html Page':
    return render_template('product.html', activeproduct='active',css='static/productcss.css')

@app.route('/about_us')
def about_us() -> 'Html Page':

    return render_template('about_us.html', activeabout='active')

@app.route('/webapp')
def webapp() -> 'Html Page':

    return render_template('webapp.html', activewebapp='active')

@app.route('/tool')
def tool() -> 'Name of Diseases':

    return render_template('webapp.html', activewebapp='active')


app.run(debug=True)