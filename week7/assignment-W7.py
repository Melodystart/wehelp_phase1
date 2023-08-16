from flask import *
import mysql.connector
from mysql.connector import pooling

app = Flask(
  __name__,
  static_folder="public",
  static_url_path="/"
  )
app.secret_key="This is my secret"

conPool = pooling.MySQLConnectionPool(user='root', password='password', host='localhost', database='website', pool_name='websiteConPool', pool_size=2)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/signup",methods=['POST'])
def singup():
  name = request.form['name']
  username = request.form['username']
  password = request.form['password']

  con = conPool.get_connection()
  cursor = con.cursor()

  cursor.execute("SELECT username FROM member WHERE username=%s",(username,))
  data = cursor.fetchone()

  if data != None:
    return redirect("/error?message=帳號已經被註冊")
  else:
    cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)",(name, username, password))
    con.commit()
    return redirect("/")

  cursor.close()
  con.close()

@app.route("/signin",methods=['POST'])
def singin():
  username = request.form['username']
  password = request.form['password']

  con = conPool.get_connection()
  cursor = con.cursor()

  cursor.execute("SELECT id, name FROM member WHERE username=%s AND password=%s",(username, password))
  data = cursor.fetchone()

  cursor.close()
  con.close()

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
  try:
    if (session["SIGNED-IN"] == True):
      userId = session["userId"]
      name = session["name"]
      username = session["username"]

      con = conPool.get_connection()
      cursor = con.cursor()

      cursor.execute("SELECT member.name, message.content, message.time, message.member_id, message.id, member.username FROM message LEFT JOIN member on message.member_id = member.id ORDER BY time desc")
      data = cursor.fetchall()
      
      cursor.close()
      con.close()

      return render_template("member.html", name = name, data=data, userId=userId, username=username)
    else:
      return redirect("/")
  except:
    return redirect("/")

@app.route("/createMessage",methods=['POST'])
def createMessage():
  userId = session["userId"]
  content = request.form['content']

  con = conPool.get_connection()
  cursor = con.cursor()  

  cursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)",(userId, content))
  con.commit()

  cursor.close()
  con.close()

  return redirect("/member")

@app.route("/deleteMessage",methods=['POST'])
def deleteMessage():
  messageId = request.form['messageId']

  con = conPool.get_connection()
  cursor = con.cursor()

  cursor.execute("DELETE FROM message WHERE id=%s",(int(messageId),))
  con.commit()

  cursor.close()
  con.close()

  return redirect("/member")

@app.route("/error")
def error():
  message = request.args.get("message", "")
  return render_template("error.html", message=message)

@app.route("/signout")
def signout():
  session.clear()
  return redirect("/")

# 查詢會員資料的 API
@app.route("/api/member",methods=['GET'])
def getApi():
  result = {}
  try:
    if (session["SIGNED-IN"] == True):  
      username = request.args.get("username", "")

      con = conPool.get_connection()
      cursor = con.cursor()

      cursor.execute("SELECT id, name, username FROM member WHERE username=%s",(username, ))
      data = cursor.fetchone()

      cursor.close()
      con.close()

      ans ={}
      ans["id"] = data[0]
      ans["name"] = data[1]    
      ans["username"] = data[2]
      result["data"] = ans
      return result
    else:
      result["data"] = None
      return result  
  except:
    result["data"] = None
    return result    

# 修改會員姓名的 API
@app.route("/api/member",methods=['PATCH'])
def patchApi():
  result = {}
  try:
    if (session["SIGNED-IN"] == True):
      updateData = request.get_json()

      con = conPool.get_connection()
      cursor = con.cursor()

      cursor.execute("UPDATE member SET name = %s WHERE id = %s",(updateData["name"], session["userId"]))
      con.commit()

      cursor.close()
      con.close()

      session["name"] = updateData["name"]
      result["ok"] = True
      return result
    else:
      result["error"] = True
      return result       
  except:
    result["error"] = True
    return result    

app.run(port=3000)

