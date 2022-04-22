import random

from flask import *
from flask import redirect, request
import sqlite3
from random import randrange, randint


app = Flask(__name__, template_folder='templates')


@app.route("/")
def base():
    return render_template("index.html")


@app.route("/reg")
def reg():
    return render_template("register.html")


@app.route("/registeruser", methods=["POST"])
def register():
    try:
        password = request.form["pass"]
        cnfpass = request.form["cnfpass"]
        if password == cnfpass:
            name = request.form["name"]
            email = request.form["email"]
            phone = request.form["mob"]
            with sqlite3.connect("movie.db") as c:
                cur = c.cursor()
                cur.execute('''INSERT INTO register(cust_name, cust_phone, cust_email, cust_password) values(?, ?, ?, ?)''', (name, phone, email, password))
                c.commit()
    except Exception:
        c.rollback()
        msg = "Not Registered Successfully"
        return render_template("register.html", msg=msg)
    finally:
        c.close()
        return render_template("ulogin.html")


@app.route("/ulogin")
def ulogin():
    return render_template("ulogin.html")


@app.route("/alogin")
def alogin():

    return render_template("alogin.html")


@app.route("/ologin")
def ologin():
    return render_template("ologin.html")


@app.route("/adlog", methods=["POST"])
def adlog():
    name = request.form["id"]
    pass1 = request.form["pass"]

    if name == "100" and pass1 == "1234":
        with sqlite3.connect("movie.db") as c:
            count = c.execute("select count(mov_id) from movie")
            users = c.execute("select count(cust_phone) from register")
            booking = c.execute("select count(ticket_id) from ticket")
        return render_template("adminhome.html", count=count, users=users, booking=booking)
    else:
        return render_template("incorradmin.html")


@app.route("/uslog", methods=["POST"])
def uslog():
    mob = request.form["mob"]
    pass1 = request.form["pass"]
    c = sqlite3.connect("movie.db")

    data = c.execute("select * from register where cust_phone= ?", (mob,))
    for i in data:
        t = str(i[3])
        if t == pass1:
            with sqlite3.connect("movie.db") as c:
                c.row_factory = sqlite3.Row
                cur = c.cursor()
                cur.execute("select * from movie")
                data = cur.fetchall()

            return render_template("userhome.html", data=data, mob=mob)

    return render_template("incorruser.html")


@app.route("/owlog", methods=["POST"])
def owlog():
    name = request.form["id"]
    pass1 = request.form["pass"]

    if name == "101" and pass1 == "1234":
        with sqlite3.connect("movie.db") as c:
            booking = c.execute("select sum(Count_of_Ticket) from ticket")
        return render_template("ownerhome.html", booking=booking)
    else:
        return render_template("incorrowner.html")


@app.route("/addmovies", methods=["POST"])
def addmovies():
    id1 = request.form["id"]
    name = request.form["mname"]
    lang = request.form["lang"]
    des = request.form["des"]
    price = request.form["price"]
    try:
        with sqlite3.connect("movie.db") as c:
            cur = c.cursor()
            cur.execute('''INSERT INTO movie(mov_id, mov_name, mov_lang, mov_des, price) values(?, ?, ?, ?, ?)''', (id1, name, lang, des, price))
            c.commit()
    except Exception:
        c.rollback()
        return render_template("index.html")
    finally:
        c.close()
        return render_template("addedmov.html")


@app.route("/view")
def view():
    with sqlite3.connect("movie.db") as c:
        c.row_factory = sqlite3.Row
        cur = c.cursor()
        cur.execute("select * from movie")
        data = cur.fetchall()
        return render_template("viewmov.html", rows=data)


@app.route("/add")
def add():
    return render_template("addmov.html")


@app.route("/del1")
def del1():
    return render_template("del1.html")


@app.route("/delmovie", methods=["POST"])
def delmovie():
    id1 = request.form["id"]
    c = sqlite3.connect("movie.db")

    c.execute("delete from movie where mov_id = ?", (id1,))
    c.commit()
    return render_template("movdeleted.html")


@app.route("/showusers")
def showusers():
    with sqlite3.connect("movie.db") as c:
        c.row_factory = sqlite3.Row
        cur = c.cursor()
        cur.execute("select * from register")
        data = cur.fetchall()
        return render_template("viewusers.html", rows=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/update")
def update():
    return render_template("update.html")


@app.route('/updated', methods=["POST"])
def updated():
    e = request.form["email"]
    n = request.form["name"]
    p = request.form["pass"]
    m = request.form["mobile"]

    with sqlite3.connect("movie.db") as con:
        try:
            cur = con.cursor()
            cur.execute("update register set cust_email ='{}',cust_name='{}',cust_password='{}' where cust_phone={}" .format(e, n, p, m))
            msg = "updated successfully"
            con.commit()
        except:
            msg = "wrong registered number"
            return render_template("update.html", msg=msg)
        finally:
            return render_template("update.html", msg=msg)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/seatselection")
def seatview():
    return render_template("seatview.html")


@app.route("/payment", methods=["POST"])
def payment():
    price = request.form["num"]
    ticket = request.form["ticket"]
    return render_template("home.html", price=price, ticket=ticket)


def ran():
    x = random.randint(1000000000, 11999999999)
    return x


@app.route("/confirm", methods=["POST"])
def confirm():
    name = request.form["name"]
    mob = request.form["mob"]
    ticket = request.form["ticket"]
    l1 = []
    y = ran()
    if y in l1:
        confirm()
    else:
        l1.append(y)
        p = l1[len(l1)-1]
        c = sqlite3.connect("movie.db")
        c.execute('''INSERT INTO ticket(ticket_id, Count_of_Ticket, cust_id ) values(?, ?, ?)''', (p, ticket, mob))
        c.commit()
        return render_template("success.html", p=p)


@app.route("/booking")
def show():
    with sqlite3.connect("movie.db") as c:
        c.row_factory = sqlite3.Row
        cur = c.cursor()
        cur.execute("select * from ticket")
        data = cur.fetchall()
    return render_template("/booking.html", data=data)


@app.route("/searchmov", methods=["POST"])
def searchmov():
    search = request.form["search"]
    search.lower()
    with sqlite3.connect("movie.db") as c:

        c.row_factory = sqlite3.Row
        cur = c.cursor()
        cur.execute("select * from movie where lower(mov_name) = ?", (search, ))
        data = cur.fetchall()
        msg = "Searched Movie"
        if len(data) > 0:
            return render_template("searchedmovie.html", msg=msg, data=data)
        else:
            msg = "Movie Not Founnd"
            return render_template("searchedmovie.html", msg=msg)


if __name__ == '__main__':
    app.run(debug=True)
