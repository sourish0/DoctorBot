from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage() -> 'Html page':
    return render_template('homepage.html', activehome='active')

@app.route('/product')
def product() -> 'Html Page':

    return render_template('product.html', activeproduct='active')

@app.route('/about_us')
def about_us() -> 'Html Page':

    return render_template('about_us.html', activeabout='active')

@app.route('/webapp')
def webapp() -> 'Html Page':

    return render_template('webapp.html', activewebapp='active')

app.run(debug=True)