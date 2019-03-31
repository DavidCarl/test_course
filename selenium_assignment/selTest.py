import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class TestMariosPizza(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def tearDown(self):
        self.driver.close()
        
    def test_index(self):
        self.driver.get('http://localhost:5000')
        table = WebDriverWait(self.driver, 10).until(
        lambda x: x.find_element_by_id("Annanas"))
        table_children = table.find_elements_by_tag_name('td')
        
        self.assertEqual(table_children[0].get_attribute('innerHTML'), '1')
        self.assertEqual(table_children[1].get_attribute('innerHTML'), 'Annanas')
        self.assertEqual(table_children[2].get_attribute('innerHTML'), '1000')

    def test_order(self):
        self.driver.get('http://localhost:5000')
        WebDriverWait(self.driver, 10).until(
        lambda x: x.find_element_by_id("Annanas"))

        name = self.driver.find_element_by_id('cust')
        name.send_keys('blin')

        pizza = self.driver.find_element_by_id('pizza')
        pizza.send_keys('1')

        self.driver.find_element_by_id('sendOrder').click()
        time.sleep(0.5)


    def test_view_orders(self):
        self.driver.get('http://localhost:5000/orders')
        table = WebDriverWait(self.driver, 10).until(
        lambda x: x.find_element_by_id("orderTable"))
        table_children = table.find_elements_by_tag_name('td')
        
        name = self.driver.find_element_by_id('name')

        self.assertEqual(name.get_attribute('innerHTML'), 'blin')
        self.assertEqual(table_children[0].get_attribute('innerHTML'), '1')
        self.assertEqual(table_children[1].get_attribute('innerHTML'), 'Annanas')
        self.assertEqual(table_children[2].get_attribute('innerHTML'), '1000')



if __name__ == "__main__":
    unittest.main()