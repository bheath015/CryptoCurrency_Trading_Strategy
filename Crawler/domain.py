#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 14:46:33 2017

@author: Brian
"""

from urllib.parse import urlparse

# Get actual domain (example.com)
def get_domain_name(url):
    try:
        results = get_subdomain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''
        

# Get sub domain naim (name.example.com)
def get_subdomain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''