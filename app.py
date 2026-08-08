from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


# Database setup function
def init_db():
  conn = sqlite3.connect("users.db")
  cursor = conn.cursor()
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
  conn.commit()
  conn.close()


@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    name = request.form["name"]
    email = request.form["email"]

    # Database me data save karna
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO customers (name, email) VALUES (?, ?)", (name, email)
    )
    conn.commit()
    conn.close()
    return "Data successfully save ho gaya hai!"

  return render_template("index.html")


if __name__ == "__main__":
  init_db()
  app.run(debug=True)

