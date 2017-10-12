from app import db

import datetime
from flask_mongoengine.wtf import model_form

# 一个class会定义数据库todo_db中的一个集合todo
class Todo(db.Document):
	content = db.StringField(required=True, max_length=200)
	time = db.DateTimeField(default=datetime.datetime.now())
	status = db.IntField(default=0)

TodoForm = model_form(Todo)

# 一个class会定义数据库todo_db中的一个集合student
class Student(db.Document):
	"""docstring for houcong"""
	name = db.StringField(required=True, max_length=20)
	age = db.IntField(default=0)
	time = db.DateTimeField(default=datetime.datetime.now())
	
StudentForm = model_form(Student)