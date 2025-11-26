from django.test import TestCase
from django.urls import reverse
from .models import Todo
from datetime import date, timedelta

class TodoModelTest(TestCase):
    def test_create_todo(self):
        todo = Todo.objects.create(
            title="Test TODO",
            description="Test Description"
        )
        self.assertEqual(todo.title, "Test TODO")
        self.assertEqual(todo.description, "Test Description")
        self.assertFalse(todo.resolved)
        self.assertIsNotNone(todo.created_at)
    
    def test_todo_string_representation(self):
        todo = Todo.objects.create(title="My Task")
        self.assertEqual(str(todo), "My Task")
    
    def test_todo_with_due_date(self):
        due_date = date.today() + timedelta(days=7)
        todo = Todo.objects.create(
            title="Task with deadline",
            due_date=due_date
        )
        self.assertEqual(todo.due_date, due_date)
    
    def test_toggle_resolved(self):
        todo = Todo.objects.create(title="Test")
        self.assertFalse(todo.resolved)
        
        todo.resolved = True
        todo.save()
        self.assertTrue(todo.resolved)

class TodoViewTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_create_todo(self):
        response = self.client.post(reverse('create_todo'), {
            'title': 'New Task',
            'description': 'Task description',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.first().title, 'New Task')
    
    def test_delete_todo(self):
        todo = Todo.objects.create(title="To be deleted")
        response = self.client.post(reverse('delete_todo', args=[todo.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), 0)
    
    def test_toggle_resolved_view(self):
        todo = Todo.objects.create(title="Test", resolved=False)
        response = self.client.post(reverse('toggle_resolved', args=[todo.id]))
        self.assertEqual(response.status_code, 302)
        todo.refresh_from_db()
        self.assertTrue(todo.resolved)