from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "test_secret_key"
task = ["乗り越えて見せる", "世俗も", "肉欲も"]

@app.route("/")
def index():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "ms",
        password = "",
        database = "todo_app"
    )
    sort = request.args.get("sort", "new")

    if sort == "new":
        sql = "SELECT * FROM tasks ORDER BY id DESC"
    else:
        sql = "SELECT * FROM tasks ORDER BY id ASC"

    cursor = conn.cursor()
    cursor.execute(sql)

    tasks = cursor.fetchall()

    conn.close()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():

    conn = mysql.connector.connect(
        host = "localhost",
        user = "ms",
        password = "",
        database = "todo_app"
    )

    cursor = conn.cursor()

    title = request.form["title"]
    cursor.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))

    conn.commit()
    conn.close()
    
    return redirect("/")

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    conn = mysql.connector.connect(
        host = "localhost",
        user = "ms",
        password = "",
        database = "todo_app"
    )

    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = (%s)", (task_id,))

    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/edit/<int:task_id>")
def edit(task_id):
    conn = mysql.connector.connect(
        host = "localhost",
        user = "ms",
        password = "",
        db = "todo_app"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = (%s) ", (task_id,))
    task = cursor.fetchone()

    return render_template("edit.html", task=task)

@app.route("/update/<int:task_id>", methods=["POST"])
def update(task_id):
    conn = mysql.connector.connect(
        host = "localhost",
        user = "ms",
        password = "",
        db = "todo_app"
    )

    title = request.form["title"]
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET title = (%s) WHERE id = (%s) ", (title, task_id,))

    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/toggle/<int:task_id>")
def toggle(task_id):
    conn = mysql.connector.connect(
        host = "localhost",
        user = "ms",
        password = "",
        db = "todo_app"
    )

    sort = request.args.get("sort", "new")

    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = NOT completed WHERE id = (%s)", (task_id,))
    conn.commit()
    conn.close()

    return redirect(url_for("index", sort=sort))

@app.route("/register", methods=["GET", "POST"])
def register():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "ms",
        password = "",
        db = "todo_app"
    )

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password,))

        conn.commit()
        conn.close()
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "ms",
        password = "",
        db = "todo_app"
    )

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = (%s)", (username,))

        user = cursor.fetchone()

        if user and user[2] == password:
            session["user_id"] = user[0]
            session["username"] = user[1]
            return redirect(url_for("index"))

    return "ログイン失敗"



    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    #app.run(debug=True)
