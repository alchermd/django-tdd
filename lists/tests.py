from django.test import TestCase

from .models import Task, List


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'title': 'A new task item'})

        self.assertEqual(1, Task.objects.count())
        new_task = Task.objects.first()
        self.assertIn('A new task item', new_task.title)


class ListViewTest(TestCase):

    def test_displays_all_tasks_for_that_list(self):
        list_ = List.objects.create()
        Task.objects.create(title='Task 1', list=list_)
        Task.objects.create(title='Task 2', list=list_)

        another_list = List.objects.create()
        Task.objects.create(title='Task 1 for another list', list=another_list)
        Task.objects.create(title='Task 2 for another list', list=another_list)

        response = self.client.get(f'/lists/{list_.id}')

        self.assertContains(response, 'Task 1')
        self.assertContains(response, 'Task 1')
        self.assertNotContains(response, 'Task 1 for another list')
        self.assertNotContains(response, 'Task 2 for another list')

    def test_uses_list_template(self):
        list_ = List.objects.create()
        response = self.client.get(f'/lists/{list_.id}')
        self.assertTemplateUsed(response, 'lists/lists_show.html')


class NewListTest(TestCase):

    def test_can_save_a_POST_request(self):
        self.client.post('/', data={'title': 'A new task'})
        self.assertEqual(Task.objects.count(), 1)

        new_task = Task.objects.first()
        self.assertEqual(new_task.title, 'A new task')

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'title': 'A new task'})
        new_list = List.objects.first()
        self.assertRedirects(response, f'/lists/{new_list.id}')


class NewTaskTest(TestCase):

    def test_can_save_a_POST_request_to_an_existing_list(self):
        correct_list = List.objects.create()
        other_list = List.objects.create()

        self.client.post(
            f'/lists/{correct_list.id}/add_task',
            data={'title': 'New task for existing list'}
        )

        self.assertEqual(Task.objects.count(), 1)
        new_task = Task.objects.first()
        self.assertEqual(new_task.title, 'New task for existing list')
        self.assertEqual(new_task.list, correct_list)

    def test_redirects_to_list_view(self):
        correct_list = List.objects.create()

        response = self.client.post(
            f'/lists/{correct_list.id}/add_task',
            data={'title': 'New task for existing list'}
        )

        self.assertRedirects(response, f'/lists/{correct_list.id}')


class TaskModelTest(TestCase):

    def test_saving_and_retrieving_tasks(self):
        list_ = List.objects.create()

        first_task = Task.objects.create(title='My first task', list=list_)
        second_task = Task.objects.create(title='My second task', list=list_)

        saved_tasks = Task.objects.all()
        self.assertEqual(saved_tasks.count(), 2)

        self.assertEqual(saved_tasks[0].title, 'My first task')
        self.assertEqual(saved_tasks[1].title, 'My second task')


class ListModelTest(TestCase):

    def test_saving_and_retrieving_lists(self):
        list_ = List.objects.create()

        first_task = Task(title='The first task', list=list_)
        second_task = Task(title='The second task', list=list_)

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)
        self.assertEqual(first_task.list, list_)
        self.assertEqual(second_task.list, list_)
