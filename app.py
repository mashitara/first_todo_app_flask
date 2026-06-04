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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    #app.run(debug=True)
