from flask import Flask
import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello!"


@app.route("/now")
def showNow():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@app.route("/add/<a>/<b>")
def add(a, b):
    return "Result = %f" % (float(a) + float(b))


@app.route("/update/<name>/<x>/<y>/<info>")
def updateLoc(name, x, y, info):
    print "Call update api"
    import sqlite3

    conn = sqlite3.connect('Data.db')
    sql = "INSERT INTO LOC (NAME,X,Y,INFO) \
          VALUES ( '%s', %f, %f, '%s' )" % (name, float(x), float(y), info)
    conn.execute(sql)
    conn.commit()
    conn.close()
    return "Data is inserted!!"


@app.route("/list")
def listAll():
    print "Call list api"
    import sqlite3

    conn = sqlite3.connect('Data.db')
    sql = "SELECT * FROM LOC"
    cursor = conn.execute(sql)
    res = ""
    for row in cursor:
        res += str(row)+"<br>"
    conn.close()

    html="""
            <!DOCTYPE html>
            <html>
            <head>

            <meta http-equiv="refresh" content="5" />

            <title>List of LOC</title>
            </head>
            <body>

            <p>%s</p>

            </body>
            </html>
            """ % res
    return html


@app.route("/erease_all")
def eraseAll():
    print "Call erase_all api"
    import sqlite3

    conn = sqlite3.connect('Data.db')
    sql = "DELETE FROM LOC"
    conn.execute(sql)
    conn.commit()
    conn.close()
    return "Done"


@app.route("/kml")
def getKML():
    print "Call kml api"
    import sqlite3
    import simplekml

    kml = simplekml.Kml()

    conn = sqlite3.connect('Data.db')
    sql = "SELECT * FROM LOC"
    cursor = conn.execute(sql)
    for row in cursor:
        kml.newpoint(name=row[1], coords=[(row[2], row[3])])
    conn.close()
    return kml.kml()


if __name__ == "__main__":
    app.run()
