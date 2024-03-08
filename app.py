#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, render_template
'''
Flask is the web framework used to create the application.
request is used to handle HTTP requests.
render_template is used to render HTML templates.
'''
# Creates an instance of the Flask class, which is the WSGI application.
app = Flask(__name__)

# Decorates the index function to be called when the root URL ("/") is accessed with either a GET or POST request
@app.route("/",methods = ["GET","POST"])

def index():  # handling requests to the root URL ("/").

    if request.method =="POST":
        rate = float(request.form.get("rate"))
        print(rate)
        # it renders the "index.html" template and passes a variable result with the value "ML model not read".
        return(render_template("index.html",result = 90.2 + (-50.6*rate)))
    else:

        return(render_template("index.html",result = "waitting for exchange rate......"))

if __name__ =="__main__":
    app.run()


# In[ ]:




