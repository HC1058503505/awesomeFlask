from app import app
from flask import render_template,request,redirect,url_for
from app.models import Todo,Student,TodoForm,StudentForm
import datetime

@app.errorhandler(404)
def not_found(e):
	return render_template('404.html'), 404

@app.route('/')
def index():
	form = TodoForm()
	todos = Todo.objects.order_by('content')
	return render_template("index.html",todos=todos,forms=form)

@app.route('/add',methods=['POST',])
def add():
	form = TodoForm(request.form)
	if form.validate():
		content = form.content.data
		todo = Todo(content=content)
		todo.save()
		return redirect(url_for("index",forms=form))
	else:
		todos = Todo.objects.all()
		return render_template("index.html",todos=todos, forms=form)
	

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
