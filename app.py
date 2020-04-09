from flask import render_template,request
from flask import Flask
app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/index',methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        pass_ = request.form['psw']
        if pass_ == "vish":
            return render_template('index.html')
        else:
            return render_template('login.html', message="wrong password")
    else:
        return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)