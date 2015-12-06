#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import json
import requests
from urlparse import urljoin, urlparse
from bs4 import BeautifulSoup


def get_script_links(response, bsObj):
	src_lists = set()
	script_relative_links = bsObj.findAll('script')
	for s in script_relative_links:
		if s.get('src') is not None:
			src_lists.add(urljoin(response.url, s.get('src')))
	return src_lists

def get_css_links(response, bsObj):
	css_lists = set()
	css_relative_links = bsObj.findAll('link')
	for css in css_relative_links:
		if css.get('src') is not None:
			css_lists.add(urljoin(response.url, css.get('src')))
	return css_lists

def get_img_links(response, bsObj):
	img_lists = set()
	img_ralative_links = bsObj.findAll('img')
	for img in img_ralative_links:
		if img.get('src') is not None:
			img_lists.add(urljoin(response.url, img.get('src')))

	return img_lists


def main():
	try:
		response = requests.get('http://www.huxiu.com')
		bsObj = BeautifulSoup(response.content, 'html.parser')
	except Exception, e:
		raise e
	else:
		src_lists = get_script_links(response, bsObj)
		css_lists = get_css_links(response, bsObj)
		img_lists = get_img_links(response, bsObj)
	
	try:
		parseResult = urlparse('http://www.huxiu.com')
		netloc = parseResult.netloc
		name = netloc.split('.')[-2]
		path = os.path.join(os.getcwd(), name)
		os.mkdir(path)
		os.chdir(path)
	except Exception, e:
		raise e

	for link in src_lists:
		path = urlparse(link).path
		name = path.split('/')[-1]
		try:
			r = requests.get(link)
			f = open(name, 'w+')
			f.write(r.content)
			f.close()
		except Exception, e:
			raise e

	for link in css_lists:
		path = urlparse(link).path
		name = path.split('/')[-1]
		try:
			r = requests.get(link)
			f = open(name, 'w+')
			f.write(r.content)
			f.close()
		except Exception, e:
			raise e

	for link in img_lists:
		path = urlparse(link).path
		name = path.split('/')[-1]
		try:
			r = requests.get(link)
			f = open(name, 'w+')
			f.write(r.content)
			f.close()
		except Exception, e:
			raise e

if __name__ == '__main__':
	main()


