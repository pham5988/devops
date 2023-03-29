#!/usr/bin/python3

import os

path = "/tmp/pysys"

if os.path.isdir(path):
  print('It is a directory')
elif os.path.isfile(path):
  print ("it is a file")
else:
  print ("file or dir does not exists")
