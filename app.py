from flask import Flask, request, render_template
import datetime
import sqlite3
from flask import Markup

# Creates an instance of the Flask class, which is the WSGI application.
app = Flask(__name__)
name = ''
name_flag = 0

# Decorates the index function to be called when the root URL ("/") is accessed with either a GET or POST request
@app.route("/",methods = ["GET","POST"])
def index():  # handling requests to the root URL ("/").
    return(render_template("index.html"))


@app.route("/main",methods = ["GET","POST"])
def main():  
    global name,name_flag
    if name_flag == 0:
        name = request.form.get("name")
        name_flag = 1
        conn = sqlite3.connect('log.db')
        c = conn.cursor()
        timestamp = datetime.datetime.now()
        c.execute("insert into employee (name, timestamp) values (?, ?)", (name,timestamp))
        conn.commit()
        conn.close()
    return(render_template("main.html",name=name))

@app.route("/ethical_test",methods = ["GET","POST"])
def ethnical_test():  
    return(render_template("ethical_test.html"))


@app.route("/query",methods = ["GET","POST"])
def query():  
    conn = sqlite3.connect('log.db')
    c = conn.execute("select * from employee")
    r = ''
    for row in c:
        r = r+str(row)+"<br>"
    print(r)
    r = Markup(r)
    c.close()
    conn.close()
    return(render_template("query.html",r = r))

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
