from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)
task = ["乗り越えて見せる", "世俗も", "肉欲も"]

conn = mysql.connector.connect(
    host = "localhost",
    user = "ms",
    password = "",
    database = "todo_app"
)

cursor = conn.cursor()
cursor.execute("SELECT title FROM tasks")

tasks = cursor.fetchall()

conn.close()


@app.route("/")
def index():
    
    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    #app.run(debug=True)
