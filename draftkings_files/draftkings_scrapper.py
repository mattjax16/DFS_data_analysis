"""
draftkings_scrapper.py

this file is to scrape draft kings mlb data

"""


import psycopg2
import pandas as pd
import sys
from configparser import ConfigParser
from requests_html import HTMLSession
import bs4





class DkScrapper():
    '''
    This is a class to scrape date from draft kings
    '''
    def __init__(self):
        self.mlb_cat_urls = {'50/50':'https://www.draftkings.com/lobby#/MLB/0/IsFiftyfifty'}
        self.con = self.config()



    def config(self,filename='draftkings_scrapper.ini', section='login'):
        '''
        This is a function to read the ini file and use the info to login into draftkings
        :param filename:
        :param section:
        :return:
        '''
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)

        # get section,
        con = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                con[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return con


    def get_response(self,url):
        '''

        :param url (string): a url of a webpage
        :return:
        '''
        session = HTMLSession()
        response = session.get(url)

        print(f'Response: {response.status_code}')
        return response

    def get_div_html(self,response,div):
        '''

        :param response (response object):
        :param tag (string): tag to find:
        :return:
        '''
        div_html = response.html.find(f'div.{div}')
        return div_html




'''
The main function used to test functions from this python script
'''


def main():
    scrapper = DkScrapper()

    c = scrapper.config()

    test_url = scrapper.mlb_cat_urls['50/50']
    r = scrapper.get_response(test_url)

    grid_canvas_tag = 'grid-canvas'
    grid_canvas_html = scrapper.get_div_html(r,grid_canvas_tag)

    print('Done Maine()')

if __name__ == '__main__':
    main()