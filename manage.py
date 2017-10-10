# -*- codoing: utf-8 -*-

from flask_script import Manager, Server

from app import app
from app.models import Todo,Student

manager = Manager(app)

manager.add_command("runserver",Server(host='0.0.0.0',port=5000,use_debugger=True))


@manager.command 
def save_todo():
	todo = Todo(content="my First todo")
	todo.save()
	print("Save compelete")
	
@manager.command
def save_student():
	stud = Student(name="houcong",age=26)
	stud.save()
	print("Save student")
if __name__ == '__main__':
	manager.run()