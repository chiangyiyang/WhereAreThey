from flask import Flask
import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Yiyang!"


@app.route("/now")
def showNow():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@app.route("/add/<a>/<b>")
def add(a, b):
    return "Result = %f" % (float(a) + float(b))


@app.route("/update/<name>/<x>/<y>/<info>")
def updateLoc(name, x, y, info):
    import sqlite3

    conn = sqlite3.connect('Data.db')
    print "Opened database successfully";
    sql = "INSERT INTO LOC (NAME,X,Y,INFO) \
          VALUES ( '%s', %f, %f, '%s' )" % (name, float(x), float(y), info)
    conn.execute(sql)
    conn.commit()
    conn.close()
    return "Data is inserted!!"


@app.route("/list")
def listAll():
    import sqlite3

    conn = sqlite3.connect('Data.db')
    print "Opened database successfully";
    sql = "SELECT * FROM LOC"
    cursor = conn.execute(sql)
    res = ""
    for row in cursor:
        res += str(row)
    conn.close()

    return res


if __name__ == "__main__":
    app.run()
