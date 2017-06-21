# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 19:36:38 2017

@author: Win7ows
"""

import bottle
import os
import datetime


def p_template(str):
    return bottle.template(str,page=str)

@bottle.route('/')
def index():
    return p_template('index')
    

@bottle.route('/static/<directory>/<filename>')
def server_static(directory, filename):
    root = os.path.join(os.getcwd(), 'static', directory)
    return bottle.static_file(filename, root=root)
    
@bottle.route('/about')
def about():
    return p_template('about')

@bottle.get('/blog')
def blog():
    with get_dao() as data_access_object:
        posts = data_access_object.select()
    return bottle.template('blog', posts=posts, page='blog')

def get_dao():
    import dao
    return dao.MockDataAccessObject()
    

@bottle.get('/post')
def new_entry():
    return p_template('post')

@bottle.post('/blog')
def add_entry():
    
    data=dict()
    data['TITLE']=bottle.request.forms.get('title')
    data['AUTHOR']=bottle.request.forms.get('author')
    data['CONTENT']=bottle.request.forms.get('content')
    data['POST_DATE']=datetime.datetime.now()
    print ("test")
    print(data)
    with get_dao() as data_access_object:
        data_access_object.insert(data)
    return blog()
    




application = bottle.default_app()
application.run()