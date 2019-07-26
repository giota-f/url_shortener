import string
from restapi import mysql

'''class Link(mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key=True)
    original_url = mysql.Column(mysql.String(512))
    short_url = mysql.Column(mysql.String(100), unique=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_link()

    def generate_short_link(self):
        pass'''
