from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
app=Flask(__name__)

# @app.route("/a/<int:a>")
# def demo(a):
#     return render_template("login.html",a=a)


# @app.route("/a/<name>/<int:age>")
# def run(name,age):
#     if age>18:
#         return render_template("login.html",name=name,age=age)

#     else:
#         return render_template("home.html")


# @app.route("/raina")
# def suresh():
#     return"welcome"
# @app.route("/praveen")
# def kumar():
#     # return redirect(url_for("suresh"))mainly used to url_forr
#      return redirect("/raina")


# @app.route("/calculator/<int:num1>/<int:num2>")
# def calculator (num1,num2):
#     return render_template("calculator.html",num1=num1,num2=num2)
# @app.route("/sub/<int:num1>/<int:num2>")
# def calculators(num1,num2):
#     return f"{num1-num2}"



# @app.route("/")
# def table():
#     conn=mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="root",
#         database="kumars"
#     )
#     cur=conn.cursor()
#     cur.execute("create table if not exists students(id int auto_increment primary key,name varchar(100))")
#     conn.commit()
#     conn.close()
#     return "table"
















if __name__=="__main__":
    app.run(debug=True)
