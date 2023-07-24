import pymongo
import math

from flask import *
app = Flask(
  __name__,
  static_folder="public",
  static_url_path="/"
  )

app.secret_key="This is my secret"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/signin",methods=['POST'])
def singin():
  account = request.form['account']
  password = request.form['password']

  if ( account == "" or password == ""):
    return redirect("/error?message=請輸入帳號及密碼")

  if ( account == "test" and password == "test"):
    session["SIGNED-IN"] = True
    return redirect("/member")
  else:
    return redirect("/error?message=帳號或密碼錯誤")

@app.route("/member")
def member():
  if (session["SIGNED-IN"] == True):
    return render_template("member.html")
  else:
    return redirect("/")

@app.route("/error")
def error():
  message = request.args.get("message", "")
  return render_template("error.html", message=message)

@app.route("/signout")
def signout():
  session["SIGNED-IN"] = False
  return redirect("/")

@app.route("/square",methods=['POST'])
def square():
  number = request.form['number']
  return redirect("/square/" + number)

@app.route("/square/<int:number>")
def square_number(number):
  number = number**2
  return render_template("number.html", number=number)

app.run(port=3000)