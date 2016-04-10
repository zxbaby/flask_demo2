from datetime import datetime
import subprocess
import os

def test(text):
    print 'hello %s ,current time is %s' %(text, datetime.now())

def job(dic):
    ip = dic.get('ip') or '127.0.0.1'
    cmd = dic.get('cmd')
    out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res, err = out.communicate()
    print '%s is runing ' % out.pid

