from flask import *
import mysql.connector

app = Flask(
  __name__,
  static_folder="public",
  static_url_path="/"
  )
app.secret_key="This is my secret"

con = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database= 'website'
)
cursor = con.cursor()


@app.route("/")
def index():
  return render_template("index.html")

@app.route("/signup",methods=['POST'])
def singup():
  name = request.form['name']
  username = request.form['username']
  password = request.form['password']

  cursor.execute("SELECT username FROM member WHERE username=%s",(username,))
  data = cursor.fetchone()

  if data != None:
    return redirect("/error?message=帳號已經被註冊")
  else:
    cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)",(name, username, password))
    con.commit()
    return redirect("/")

@app.route("/signin",methods=['POST'])
def singin():
  username = request.form['username']
  password = request.form['password']

  cursor.execute("SELECT id, name FROM member WHERE username=%s AND password=%s",(username, password))
  data = cursor.fetchone()

  if ( data == None):
    return redirect("/error?message=帳號或密碼輸入錯誤")
  else:
    session["SIGNED-IN"] = True
    session["userId"] = data[0]
    session["username"] = username
    session["name"] = data[1]
    return redirect("/member")

@app.route("/member")
def member():
  # try:
    if (session["SIGNED-IN"] == True):
      userId = session["userId"]
      name = session["name"]
      cursor.execute("SELECT member.name, message.content, message.time, message.member_id, message.id FROM message LEFT JOIN member on message.member_id = member.id ORDER BY time desc")
      data = cursor.fetchall()
      return render_template("member.html", name = name, data=data, userId=userId)
    else:
      return redirect("/")
  # except:
  #   return redirect("/")

@app.route("/createMessage",methods=['POST'])
def createMessage():
  userId = session["userId"]
  content = request.form['content']
  cursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)",(userId, content))
  con.commit()
  return redirect("/member")

@app.route("/deleteMessage",methods=['POST'])
def deleteMessage():
  messageId = request.form['messageId']
  cursor.execute("DELETE FROM message WHERE id=%s",(int(messageId),))
  con.commit()
  return redirect("/member")

@app.route("/error")
def error():
  message = request.args.get("message", "")
  return render_template("error.html", message=message)

@app.route("/signout")
def signout():
  session.clear()
  return redirect("/")

app.run(port=3000)

con.close()