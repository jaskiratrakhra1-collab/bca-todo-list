import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "todo-project-key"

# Tasks are kept in memory using the same Python list idea as the original program.
tasks = []


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.errorhandler(404)
def page_not_found(error):
    flash("Invalid task operation or page.", "error")
    return redirect(url_for("index"))


@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task", "").strip()

    if not task:
        flash("Please enter a task.", "error")
        return redirect(url_for("index"))

    tasks.append(task)
    flash("Task added successfully!", "success")
    return redirect(url_for("index"))


@app.route("/update/<int:task_no>", methods=["POST"])
def update_task(task_no):
    new_task = request.form.get("task", "").strip()

    if not new_task:
        flash("Task cannot be empty.", "error")
        return redirect(url_for("index"))

    if task_no < 1 or task_no > len(tasks):
        flash("Invalid task number.", "error")
        return redirect(url_for("index"))

    tasks[task_no - 1] = new_task
    flash("Task updated successfully!", "success")
    return redirect(url_for("index"))


@app.route("/delete/<int:task_no>", methods=["POST"])
def delete_task(task_no):
    if task_no < 1 or task_no > len(tasks):
        flash("Invalid task number.", "error")
        return redirect(url_for("index"))

    removed = tasks.pop(task_no - 1)
    flash(f'"{removed}" deleted successfully!', "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
