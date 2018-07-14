import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # John heard about a new task manager app.
        # He checks out its home page.
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_tasks_table('1. Buy a new laptop')

        # There is still a text box inviting him to add another task.
        # He enters "Buy a new keyboard"
        input_box = self.browser.find_element_by_id('new-task')
        input_box.send_keys('Buy a new keyboard')
        input_box.send_keys(Keys.ENTER)

        # The page updates again, showing both of the tasks
        self.wait_for_row_in_tasks_table('1. Buy a new laptop')
        self.wait_for_row_in_tasks_table('2. Buy a new keyboard')

        self.fail('Unfinished test...')

        # John wonders if the site will remember his tasks.
        # Then he sees that the site generated a unique URL for him.
        # Some explanatory text is displayed for that effect.

        # He visits that URL -- the tasks are still there.

    def test_can_start_a_list_for_multiple_users_with_unique_urls(self):
        # John started a new list
        self.browser.get(self.live_server_url)
        input_box = self.browser.find_element_by_id('new-task')
        input_box.send_keys('Buy a new mouse')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_tasks_table('1. Buy a new mouse')

        # He notices a unique URL for his list
        johns_url = self.browser.current_url
        self.assertRegex(johns_url, r'/lists/.+')

        # Joe also wanted his own list!
        #: We use a new browser for Joe -- we don't
        #: want John's browser data to influence Joe's session.
        self.browser.quit()
        self.browser = webdriver.Chrome()

        # Joe visits the home page, John's list wasn't there
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy a new keyboard', page_text)
        self.assertNotIn('Buy a new mouse', page_text)

        # Joe starts a new list by entering a new task
        input_box = self.browser.find_element_by_id('new-task')
        input_box.send_keys('Clean my room')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_tasks_table('1. Clean my room')

        # Joe gets his own unique URL
        joes_url = self.browser.current_url
        self.assertRegex(joes_url, r'/lists/.+')
        self.assertNotEqual(joes_url, johns_url)

        # Still, John's tasks were not there
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy a new keyboard', page_text)
        self.assertNotIn('Buy a new mouse', page_text)

    def wait_for_row_in_tasks_table(self, row_text):
        start_time = time.time()

        while True:
            try:
                table = self.browser.find_element_by_id('tasks-table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
