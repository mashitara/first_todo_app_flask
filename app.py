from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)
task = ["乗り越えて見せる", "世俗も", "肉欲も"]

@app.route("/")
def index():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "ms",
        password = "",
        database = "todo_app"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")

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

    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = NOT completed WHERE id = (%s)", (task_id,))
    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    #app.run(debug=True)
