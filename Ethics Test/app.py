#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from flask import Flask, request, render_template

# Creates an instance of the Flask class, which is the WSGI application.
app = Flask(__name__)

# Decorates the index function to be called when the root URL ("/") is accessed with either a GET or POST request
@app.route("/",methods = ["GET","POST"])

def index():  # handling requests to the root URL ("/").

    
    return(render_template("index.html"))

if __name__ =="__main__":
    app.run()


# In[ ]:




