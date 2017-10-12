import unittest
from app import app
from app.models import Todo
from werkzeug.exceptions import HTTPException

class TodoUnitTest(unittest.TestCase):
	"""docstring for TodoUnitTest"""
	def setUp(self):
		self.app = app.test_client()

	def tearDown(self):
		todos = Todo.objects.all()
		for todo in todos:
			todo.delete()

	def test_index(self):
		rv = self.app.get('/')
		self.assertIn("awesome-flask-todo", str(rv.data,encoding='utf-8'))

	def test_empty(self):
		rv = self.app.get('/')
		self.assertIn("No todos, please add", str(rv.data,encoding='utf-8'))

	def test_add_todo(self):
		self.app.post("/add", data=dict(content="test add todo"))
		todo = Todo.objects.get_or_404(content="test add todo")
		self.assertIsNotNone(todo)

	def test_none_todo(self):
		try:
			todo = Todo.objects.get_or_404(content='test todo none')
		except HTTPException as e:
			self.assertEqual(e.code, 404)

	def test_done_todo(self):
		todo = Todo(content='test done todo')
		todo.save()
		url = '/done/'+str(todo.id)
		rv = self.app.get(url)
		self.assertIn('/undone/'+str(todo.id), str(rv.data,encoding='utf-8'))

	def test_undone_todo(self):
		todo = Todo(content='test undone todo')
		todo.save()
		url = '/undone/'+str(todo.id)
		rv = self.app.get(url)
		self.assertIn('/done/'+str(todo.id), str(rv.data,encoding='utf-8'))

	def test_delete_todo(self):
		todo = Todo(content='test delete done')
		todo.save()
		url = '/delete/'+str(todo.id)
		rv = self.app.get(url)
		self.assertIn("No todos, please add", str(rv.data,encoding='utf-8'))

	def test_404(self):
		rv = self.app.get('/404test')
		self.assertIn("Not Found", str(rv.data,encoding='utf-8'))