## Integrating HTML with python

from flask import Flask,render_template

'''
It creates an instance of the flask class 
which will be your WSGI(web server gateway interface) applictaion '''


## WSGI Application 
app=Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index1.html')   ## wrong file name will give you a jinja2.exception.templatesnotfound

@app.route("/index")
def index():
    return "Welcome to the index page"


@app.route('/about')
def about():
    return render_template('about.html')  ## eg 


if __name__=="__main__":
    app.run(debug=True)
    




