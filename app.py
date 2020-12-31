from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))

@app.route("/")
def index():  
    todo_list = Todo.query.all()
    return render_template("index.html", todo_list = todo_list)

@app.route("/add",methods = ["POST"])
def add():
    title  = request.form.get("title")
    new_todo = Todo(title = title)
    db.session.add(new_todo)
    db.session.commit()
    return redirect (url_for("index"))


@app.route("/update/<int:todo_id>",methods=["POST","GET"])
def update(todo_id):
    todo = Todo.query.filter_by(id = todo_id).first()
    if request.method == 'POST':
        todo.title  = request.form.get("title")
        try:
            db.session.commit()
            return redirect("/")
        except:
            return "There was a Problem"
    else:
        return render_template("update.html", todo = todo)

    

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id = todo_id).first()
    todo.complete = not todo.complete
    db.session.delete(todo)
    db.session.commit()
    return redirect (url_for("index")) 
    
if __name__ == "__main__":
    db.create_all()
    app.run(debug  = True)