from flask import Flask, request, render_template

# Creates an instance of the Flask class, which is the WSGI application.
app = Flask(__name__)

# Decorates the index function to be called when the root URL ("/") is accessed with either a GET or POST request
@app.route("/",methods = ["GET","POST"])
def index():  # handling requests to the root URL ("/").
    return(render_template("index.html"))


@app.route("/main",methods = ["GET","POST"])
def main():  
    name = request.form.get("name")
    return(render_template("main.html",name=name))

@app.route("/ethical_test",methods = ["GET","POST"])
def ethnical_test():  
    return(render_template("ethical_test.html"))

@app.route("/answer",methods = ["GET","POST"])
def answer():
    ans = request.form["options"]  
    if ans =="true":
        return(render_template("correct.html"))
    else:
        return(render_template("wrong.html"))

@app.route("/end",methods = ["GET","POST"])
def end():  
    return(render_template("end.html"))

if __name__ =="__main__":
    app.run()
