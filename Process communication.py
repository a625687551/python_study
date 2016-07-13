#!usr/bin/env python3
# -*- coding: utf-8 -*-

'process communication'

_author_='wangjianfeng'

from multiprocessing import Process,Queue
import os,time,random

#写数据进程代码
def write(q):
    print('process to write :%s'%os.getpid())
    for value in ['A','B','C']:
        print('put %s to queue...'%value)
        q.put(value)
        time.sleep(random.random())

#读取数据进程执行的代码
def read(q):
    print('process to read :%s'%os.getpid())
    while True:
        value=q.get(True)
        print('get %s from queue.'%value)

if __name__=='__main__':
    #父进程创建Queue,并且传给各个子进程？：
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    #启动pw子进程，写入
    pw.start()
    #启动PR子进程，读取
    pr.start()
    #等待PW结束
    pw.join()
    #pr是死循环，无法等待期结束，只能强行结束
    pr.terminate()