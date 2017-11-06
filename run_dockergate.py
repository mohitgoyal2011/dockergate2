import multiprocessing
from multiprocessing import Pool
import subprocess
import time
import Queue
import logging

def worker(name):
    name = name.strip()
    print 'Analyzing ' + name
    cmd = ['/home/mohit/dockergate2.0/dockergate_start.sh', name]
    #f = open('data/log/'+name.replace('/','_')+'_stdout.log','w')
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT)
    print 'Done Analyzing ' + name


if __name__ == '__main__':
    f = open('image_index','r').readlines()
    p = Pool(4)
    p.map(worker,f)
