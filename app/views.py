from app import app
from flask import render_template
from app.models import Todo,Student

@app.route('/')
def index():
	todos = Todo.objects.all()
	return render_template("index.html",todos=todos)