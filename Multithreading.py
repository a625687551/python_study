import _thread
import threading
from time import ctime,sleep
def loop0():
    print('start loop0 at ',ctime())
    sleep(4)
    print('loop0 done at ',ctime())
def loop1():
    print('start loop1 at ',ctime())
    sleep(2)
    print('loop0 done at ',ctime())
def main():
    print('starting at ',ctime())
    _thread.start_new_thread(loop0(),())
    _thread.start_new_thread(loop1(),())
    # loop0()
    # loop1()
    sleep(6)
    print('all done at ',ctime())
if __name__=='__main__':
    main()