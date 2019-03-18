from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_load_poll(self):
		self.browser.get('http://localhost:3000')
		self.assertIn('Polls', self.browser.title)
		self.fail('Finish Tests')

if __name__ =='__main__':
	unittest.main(warnings='ignore')