from flask import Flask

'''
It creates an instance of the flask class 
which will be your WSGI(web server gateway interface) applictaion '''


## WSGI Application 
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Flask and python with it "

@app.route("/index")
def index():
    return "Welcome to the index page"

if __name__=="__main__":
    app.run(debug=True)    ## debug any change automatically and update the data on web 
    

