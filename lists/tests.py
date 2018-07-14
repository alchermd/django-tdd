from django.test import TestCase

from .models import Task


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'title': 'A new task item'})
        self.assertIn('A new task item', response.content.decode())
        self.assertTemplateUsed(response, 'lists/home.html')


class TaskModelTest(TestCase):
    
    def test_saving_and_retrieving_tasks(self):
        first_task = Task()
        first_task.title = 'My first task'
        first_task.save()
        
        second_task = Task()
        second_task.title = 'My second task'
        second_task.save()

        saved_tasks = Task.objects.all()
        self.assertEqual(saved_tasks.count(), 2)

        self.assertEqual(saved_tasks[0].title, 'My first task')
        self.assertEqual(saved_tasks[1].title, 'My second task')



