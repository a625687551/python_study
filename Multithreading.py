# import _thread
import threading
from time import ctime,sleep

##base test
# def loop0():
#     print('start loop0 at ',ctime())
#     sleep(4)
#     print('loop0 done at ',ctime())
# def loop1():
#     print('start loop1 at ',ctime())
#     sleep(2)
#     print('loop0 done at ',ctime())
# def main():
#     print('starting at ',ctime())
#     _thread.start_new_thread(loop0(),())
#     _thread.start_new_thread(loop1(),())
#     # loop0()
#     # loop1()
#     sleep(6)
#     print('all done at ',ctime())
# if __name__=='__main__':
#     main()

#threading
# loops=[4,2]
# def loop(nloop,nesc):
#     print('start loop at ',ctime())
#     sleep(nesc)
#     print('loop',nloop,'done at',ctime())
#
# def main():
#     print('starting at:', ctime())
#     threads = []
#     nloops = range(len(loops))
#     for i in nloops:
#         t=threading.Thread(target=loop,args=(i,loops[i]))
#         threads.append(t)
#     for i in nloops: #start threads
#         threads[i].start()
#     for i in nloops: #wait for all
#         threads[i].join() #threads finish
#     print('all done at ',ctime())
# if __name__=='__main__':
#     main()

#threading class more object-oriented
# loops=[4,2]
# class ThreadFunc(object):
#     def __init__(self,func,args,name=''):
#         self.name=name
#         self.func=func
#         self.args=args
#     def __call__(self):
#         self.func(*self.args)
# def loop(nloop,nesc):
#     print('start loop at ',ctime())
#     sleep(nesc)
#     print('loop',nloop,'done at',ctime())
#
# def main():
#     print('starting at:', ctime())
#     threads = []
#     nloops = range(len(loops))
#     for i in nloops:
#         t=threading.Thread(
#             target=ThreadFunc(loop,(i,loops[i]),loop.__name__))
#         threads.append(t)
#     for i in nloops: #start threads
#         threads[i].start()
#     for i in nloops: #wait for all
#         threads[i].join() #threads finish
#     print('all done at ',ctime())
# if __name__=='__main__':
#     main()


#threading subclass
# loops=(4,2)
# class MyThread(threading.Thread):
#     def __init__(self,func,args,name=''):
#         threading.Thread.__init__(self)
#         self.name=name
#         self.func=func
#         self.args=args
#     def getResult(self):
#         return self.res
#     def run(self):
#         print('starting',self.name,'at',ctime())
#         self.res=self.func(*self.args)
#         print(self.name,'finish at',ctime())
# def loop(nloop,nesc):
#     print('start loop at ',ctime())
#     sleep(nesc)
#     print('loop',nloop,'done at',ctime())
#
# def main():
#     print('starting at:', ctime())
#     threads = []
#     nloops = range(len(loops))
#     for i in nloops:
#         t=MyThread(loop,(i,loops[i]),loop.__name__)
#         threads.append(t)
#     for i in nloops: #start threads
#         threads[i].start()
#     for i in nloops: #wait for all
#         threads[i].join() #threads finish
#     print('all done at ',ctime())
# if __name__=='__main__':
#     main()
#
#compare single and multithreading
class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args
    def getResult(self):
        return self.res
    def run(self):
        print('starting',self.name,'at',ctime())
        self.res=self.func(*self.args)
        print(self.name,'finish at',ctime())

def fib(x):
    sleep(0.005)
    if x<2:return 1
    return (fib(x-2)+fib(x-1))
def fac(x):
    sleep(0.1)
    if x<2:return 1
    return (x*fac(x-1))
def sum(x):
    sleep(0.1)
    if x<2:return 1
    return (x+sum(x-1))

funcs=[fib,fac,sum]
n=12

def main():
    nfunc=range(len(funcs))
    print('---------single thread')
    for i in nfunc:
        print('starting',funcs[i].__name__,'at',ctime())
        print(funcs[i](n),'what fuck')
        print(funcs[i].__name__,'finish at ',ctime())
    print('\n*****multiple threads')
    threads=[]
    for i in nfunc:
        t=MyThread(funcs[i],(n,),funcs[i].__name__)
        threads.append(t)
    for i in nfunc:
        threads[i].start()
    for i in nfunc:
        threads[i].join()
        print(threads[i].getResult())
    print('all done')

if __name__ == '__main__':
    main()