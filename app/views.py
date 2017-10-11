from app import app
from flask import render_template,request,redirect,url_for
from app.models import Todo,Student
import datetime

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

@app.route('/done/<string:todo_id>')
def done(todo_id):
	todo = Todo.objects.get_or_404(id=todo_id)
	todo.status = 1
	todo.time = datetime.datetime.now()
	todo.save()
	return redirect(url_for('index'))

@app.route('/undone/<string:todo_id>')
def undone(todo_id):
	todo = Todo.objects.get_or_404(id=todo_id)
	todo.status = 0
	todo.time = datetime.datetime.now()
	todo.save()
	return redirect(url_for('index'))

@app.route('/delete/<string:todo_id>')
def delete(todo_id):
	todo = Todo.objects.get_or_404(id=todo_id)
	todo.delete()
	todo.save()
	return redirect(url_for('index'))
