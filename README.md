Intro
=====
Searchme is a basic searching webapp using CherryPy framework and Xapian search engine.

Requirements
============

* Xapian 1.2.19
* CherryPy 3.6
* Python >= 2.4

Overview
========
Searchme is a useless webapp. It's more like an example of using basics of xapian engine for searching and cherrypy as web framework. 

Searchme allows you to:

* upload your file on the server
* search among all uploaded files
* download a file matchig your query

Get Started
===========

* Install Xapain:

`$ sudo apt-get install python-xapian`

`$ sudo apt-get install libxapian-dev`
* Install CherryPy with pip:

`$ sudo pip install cherrypy`

* Start the server:

`$ python server.py`

* Go to http://localhost:8080 and try doing something

Storing the files
=================

For every uploaded file an md5 hash of file contents is calculated and the file gets name of that md5 hash and goes to /root/lib/hash[:2]/hash[2:4]/hash.txt 

Example: md5 is 22db87278adec2c2b961e75e0faae593, file goes to /root/lib/22/db/22db87278adec2c2b961e75e0faae593.txt