#!/bin/bash

basepath=$(cd `dirname $0`; pwd);
venvpath=$basepath/venv;

virtualenv --python=python3.7 $venvpath;
source $venvpath/bin/activate
cd $basepath
pip install -r requirements.txt;

# echo "vincent" | sudo ps -ea|grep gunicorn|awk '{print "sudo kill -9 " $1}'|/bin/sh
gunicorn -c gunicorn.conf app:app;
