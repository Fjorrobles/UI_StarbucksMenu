"""
Test the data module.
Author: Wolf Paulus (wolf@paulus.com) Modified by Fjor Robles
"""
from unittest import TestCase
from data2 import web_scraper
from os.path import exists, join
from os import remove


class Test(TestCase):
    def test_data_acquisition(self):
        """
            fetching new data and pooking around a little
        """
        path_to_data_file = join("app", "data", "menu.json")
        if exists(path_to_data_file):
            remove(path_to_data_file)
        assert False == exists(path_to_data_file)
        menu = web_scraper()
        assert exists(path_to_data_file)
      
