from flask import Flask,url_for,render_template,request
app=Flask(__name__)


@app.route("/")
def home():
    return "Welcome RAM"


if __name__=="__main__":
    app.run(debug=True)
