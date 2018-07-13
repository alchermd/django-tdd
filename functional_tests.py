from selenium import webdriver

import unittest

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
        self.fail('Unfinished test...')

        # He is invited to enter a task right away.

        # He types "Buy a new laptop"

        # When he hits enter, the page updates, and now the page lists
        # "1. Buy a new laptop" as a new task

        # There is still a text box inviting him to add another task.
        # He enters "Buy a new keyboard"

        # The page updates again, showing both of the tasks

        # John wonders if the site will remember his tasks.
        # Then he sees that the site generated a unique URL for him.
        # Some explanatory text is displayed for that effect.

        # He visits that URL -- the tasks are still there.


if __name__ == '__main__':
    unittest.main()