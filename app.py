from flask import Flask, render_template, redirect
import traceback

app = Flask(__name__)

##########################################################
# home
##########################################################
@app.route('/')
def home():
    try:
        print "home Input Data :"

        return redirect('/welcome')

    except:
        for x in traceback.format_exception(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]):
            print x;

##########################################################
@app.route('/welcome')
def welcome():

    try:
        return render_template("welcome.html")


    except:
        for x in traceback.format_exception(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]):
            print x


##########################################################
## Flask Main service.py
##########################################################

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8080)

