from flask import Flask, render_template
import mymysql

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0") 

session=[]

@app.route("/save/<num>")
def up(num):
    session.append(num)
    print(session)
    return render_template("index.html")

@app.route("/save/<num>")
def save_local(num):
    session.append(num)
    print(session)

    conn = pymysql.connect(host='localhost', user='bssmMrchoi', password='q1w2e3', db='study')
    cur = conn.cursor()
    cur.execute("insert into numcount(num) values({0})".format(num))
    conn.commit()
    conn.close()

    return redirect(url_for("index"))