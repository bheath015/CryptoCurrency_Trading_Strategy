#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 14:55:35 2017

@author: Brian
"""

import threading
from queue import Queue
from Spider import Spider
from domain import get_domain_name


PROJECT_NAME = 'brianheath'
HOMEPAGE = 'brianheath.info'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
