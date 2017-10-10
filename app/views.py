from app import app
from flask import render_template,request,redirect,url_for
from app.models import Todo,Student

@app.route('/')
def index():
	todos = Todo.objects.all()
	return render_template("index.html",todos=todos)

@app.route('/add',methods=['POST',])
def add():
	content = request.form.get("content")
	errormsg = None
	if content == "":
		errormsg="please input content!"
	else:
		todo = Todo(content=content)
		todo.save()
	return redirect(url_for('index'))
