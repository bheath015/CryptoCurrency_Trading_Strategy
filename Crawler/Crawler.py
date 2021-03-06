#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 14:21:18 2017

@author: Brian
"""

import os


# Each website you crawl is a separate project(folder)

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating project ' + directory) 
        os.makedirs(directory)

create_project_dir('brianheath')
# create  queue and crawled files(if not created)

def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')
        
# create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
    
create_data_files('brianheath', 'brianheath.info')

# add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
        
# delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass #do nothing
        
# file to set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

#iterate through a set, each item in set is new line in file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)