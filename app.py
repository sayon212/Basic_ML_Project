from flask import Flask

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def test():
    return "Hello World. This line is added in next deployment"

if __name__==("__main__"):
    app.run()