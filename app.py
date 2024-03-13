from flask import Flask, render_template, request
from dbConnector import UseDatabase

dbconfig = {'host': '127.0.0.1', 'user': 'root', 'password': '97082', 'database': 'oops2'}

app = Flask(__name__)

@app.route('/') #Done
def homepage() -> 'Html page':
    return render_template('homepage.html', activehome='active',css='static/homepagecss.css')   

@app.route('/product')  #Done
def product() -> 'Html Page':
    return render_template('product.html', activeproduct='active',css='static/productcss.css')  

@app.route('/about_us') #Sourish Will Do It
def about_us() -> 'Html Page':

    return render_template('about_us.html', activeabout='active',css='static/about_uscss.css')

@app.route('/webapp') #Not Decided Yet
def webapp() -> 'Html Page':

    return render_template('webapp.html', activewebapp='active',css='static/webappcss.css')

@app.route('/result1', methods=['GET', 'POST']) #Anybody Can Try This Best One Will Be Done
def tool() -> 'Name of Diseases':

    symptom1 = request.form['symptom1']
    symptom2 = request.form['symptom2']
    symptom3 = request.form['symptom3']
    symptom4 = request.form['symptom4']
    symptom5 = request.form['symptom5']

    with UseDatabase(dbconfig) as cursor:
        cmd = "SELECT sympkey FROM symptoms WHERE sympname IN (%s,%s,%s,%s,%s)"
        cursor.execute(cmd,(symptom1, symptom2, symptom3, symptom4, symptom5))
        sympkeys = cursor.fetchall()
        sympkey_tuple = tuple([i[0] for i in sympkeys])


        cmd = "SELECT diskey FROM symptodis WHERE sympkey IN {}".format(sympkey_tuple)
        cursor.execute(cmd)
        diskeys = cursor.fetchall()
        diskey_tuple = tuple([i[0] for i in diskeys])

        count = {}
        for i in diskey_tuple:
            if i not in count:
                count[i] = 1;
            else:
                count[i] = count[i] + 1
        count = {key: val for key, val in sorted(count.items(), key = lambda ele: ele[1], reverse = True)}
        count_tuples = tuple(count.keys())
        cmd = "SELECT disname FROM disease WHERE diskey IN {}".format(count_tuples)
        cursor.execute(cmd)
        disname = cursor.fetchall()
        disname_list = tuple([i[0] for i in disname])

    return str(disname_list)


app.run(debug=True)