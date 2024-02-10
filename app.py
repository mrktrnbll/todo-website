# from flask import Flask, render_template, request, jsonify
# import sqlite3
#
# app = Flask(__name__)
#
#
# # Initialize the database
# def init_db():
#     with sqlite3.connect("todos.db") as conn:
#         cursor = conn.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS todos (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 text TEXT NOT NULL,
#                 completed BOOLEAN DEFAULT 0
#             )
#         """)
#         conn.commit()
#
#
# # Home route
# @app.route("/")
# def index():
#     init_db()
#     return render_template("/to-do.html")

#
# # API endpoint to add a todo
# @app.route("/add_todo", methods=["POST"])
# def add_todo():
#     try:
#         todo_text = request.json["todo_text"]
#         with sqlite3.connect("todos.db") as conn:
#             cursor = conn.cursor()
#             cursor.execute("INSERT INTO todos (text) VALUES (?)", (todo_text,))
#             conn.commit()
#
#             # Get the last inserted row id
#             todo_id = cursor.lastrowid
#
#         return jsonify({"success": True, "todo": {"id": todo_id, "text": todo_text, "completed": False}}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#
#
# # API endpoint to get all todos
# @app.route("/get_todos", methods=["GET"])
# def get_todos():
#     with sqlite3.connect("todos.db") as conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM todos")
#         todos = [{"id": row[0], "text": row[1], "completed": bool(row[2])} for row in cursor.fetchall()]
#
#     return jsonify({"todos": todos})
#
# @app.route("/delete_all_todos", methods=["DELETE"])
# def delete_all_todos():
#     try:
#         with sqlite3.connect("todos.db") as conn:
#             cursor = conn.cursor()
#             cursor.execute("DELETE FROM todos")
#             conn.commit()
#
#         return jsonify({"success": True}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#
# @app.route("/add_todo", methods=["POST"])
# def add_todo():
#     try:
#         todo_text = request.json["todo_text"]
#         container = request.json.get("container", "default")  # Default to 'default' if not provided
#
#         with sqlite3.connect("todos.db") as conn:
#             cursor = conn.cursor()
#             cursor.execute("INSERT INTO todos (text, container) VALUES (?, ?)", (todo_text, container))
#             conn.commit()
#
#             # Get the last inserted row id
#             todo_id = cursor.lastrowid
#
#         return jsonify({"success": True, "todo": {"id": todo_id, "text": todo_text, "completed": False, "container": container}}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#
# @app.route("/get_todos", methods=["GET"])
# def get_todos():
#     with sqlite3.connect("todos.db") as conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM todos WHERE container = 'default'")
#         todos = [{"id": row[0], "text": row[1], "completed": bool(row[2]), "container": row[3]} for row in cursor.fetchall()]
#
#     return jsonify({"todos": todos})
#
# @app.route("/get_todos_pink", methods=["GET"])
# def get_todos_pink():
#     with sqlite3.connect("todos.db") as conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM todos WHERE container = 'pink'")
#         todos = [{"id": row[0], "text": row[1], "completed": bool(row[2]), "container": row[3]} for row in cursor.fetchall()]
#
#     return jsonify({"todos": todos})
#
# @app.route("/delete_all_todos_pink", methods=["DELETE"])
# def delete_all_todos_pink():
#     try:
#         with sqlite3.connect("todos.db") as conn:
#             cursor = conn.cursor()
#             cursor.execute("DELETE FROM todos WHERE container = 'pink'")
#             conn.commit()
#
#         return jsonify({"success": True}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#
#
# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    try:
        with sqlite3.connect("todos.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS todos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL,
                    completed INTEGER DEFAULT 0,
                    container TEXT DEFAULT 'default'
                );
            """)
            conn.commit()
    except Exception as e:
        print(f"Error initializing database: {e}")


# Add this route to serve the HTML page
@app.route("/")
def index():
    init_db()
    return render_template("to-do.html")


# Add these routes to handle pink todos
@app.route("/add_todo_pink", methods=["POST"])
def add_todo_pink():
    try:
        todo_text = request.json["todo_text"]

        with sqlite3.connect("todos.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO todos (text, container) VALUES (?, ?)", (todo_text, 'pink'))
            conn.commit()

            # Get the last inserted row id
            todo_id = cursor.lastrowid

        return jsonify({"success": True, "todo": {"id": todo_id, "text": todo_text, "completed": False, "container": 'pink'}}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/get_todos_pink", methods=["GET"])
def get_todos_pink():
    with sqlite3.connect("todos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM todos WHERE container = 'pink'")
        todos = [{"id": row[0], "text": row[1], "completed": bool(row[2]), "container": row[3]} for row in cursor.fetchall()]

    return jsonify({"todos": todos})


@app.route("/delete_all_todos_pink", methods=["DELETE"])
def delete_all_todos_pink():
    try:
        with sqlite3.connect("todos.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM todos WHERE container = 'pink'")
            conn.commit()

        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Add these routes to handle blue todos
@app.route("/add_todo_blue", methods=["POST"])
def add_todo_blue():
    try:
        todo_text = request.json["todo_text"]

        with sqlite3.connect("todos.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO todos (text, container) VALUES (?, ?)", (todo_text, 'blue'))
            conn.commit()

            # Get the last inserted row id
            todo_id = cursor.lastrowid

        return jsonify({"success": True, "todo": {"id": todo_id, "text": todo_text, "completed": False, "container": 'blue'}}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/get_todos_blue", methods=["GET"])
def get_todos_blue():
    with sqlite3.connect("todos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM todos WHERE container = 'blue'")
        todos = [{"id": row[0], "text": row[1], "completed": bool(row[2]), "container": row[3]} for row in cursor.fetchall()]

    return jsonify({"todos": todos})


@app.route("/delete_all_todos_blue", methods=["DELETE"])
def delete_all_todos_blue():
    try:
        with sqlite3.connect("todos.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM todos WHERE container = 'blue'")
            conn.commit()

        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/update_todo", methods=["PUT"])
def update_todo():
    try:
        todo_id = request.json["todo_id"]
        completed = request.json["completed"]

        with sqlite3.connect("todos.db") as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE todos SET completed = ? WHERE id = ?", (completed, todo_id))
            conn.commit()

        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)