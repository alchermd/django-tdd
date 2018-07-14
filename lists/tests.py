from django.test import TestCase

from .models import Task


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'title': 'A new task item'})

        self.assertEqual(1, Task.objects.count())
        new_task = Task.objects.first()
        self.assertIn('A new task item', new_task.title)

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'title': 'A new task item'})

        self.assertEqual(302, response.status_code)
        self.assertEqual(response['location'], '/lists/foobar')


class ListViewTest(TestCase):

    def test_displays_all_tasks(self):
        Task.objects.create(title='Task 1')
        Task.objects.create(title='Task 2')

        response = self.client.get('/lists/foobar')

        self.assertContains(response, 'Task 1')
        self.assertContains(response, 'Task 1')

    def test_uses_list_template(self):
        response = self.client.get('/lists/foobar')
        self.assertTemplateUsed(response, 'lists/lists_show.html')


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
