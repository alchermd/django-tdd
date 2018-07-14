import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # John heard about a new task manager app.
        # He checks out its home page.
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mentions about tasks.
        self.assertIn('Task', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Task Manager', header_text)

        # He is invited to enter a task right away.
        input_box = self.browser.find_element_by_id('new-task')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a new task'
        )

        # He types "Buy a new laptop"
        input_box.send_keys('Buy a new laptop')

        # When he hits enter, the page updates, and now the page lists
        # "1. Buy a new laptop" as a new task
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_tasks_table('1. Buy a new laptop')

        # There is still a text box inviting him to add another task.
        # He enters "Buy a new keyboard"
        input_box = self.browser.find_element_by_id('new-task')
        input_box.send_keys('Buy a new keyboard')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, showing both of the tasks
        self.check_for_row_in_tasks_table('1. Buy a new laptop')
        self.check_for_row_in_tasks_table('2. Buy a new keyboard')

        self.fail('Unfinished test...')

        # John wonders if the site will remember his tasks.
        # Then he sees that the site generated a unique URL for him.
        # Some explanatory text is displayed for that effect.

        # He visits that URL -- the tasks are still there.

    def check_for_row_in_tasks_table(self, row_text):
        table = self.browser.find_element_by_id('tasks-table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


if __name__ == '__main__':
    unittest.main()
