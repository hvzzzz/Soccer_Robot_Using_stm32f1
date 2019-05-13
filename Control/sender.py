from multiprocessing import Queue
q = Queue()                            # instantiate a Queue object
q.put('hello world')                   # add a string object to the queue
q.put(['this', 'is a', 'list'])        # add a list object to the queue
q.put(3.14)                            # add a number to the queue
print ('Queue size   ==> ', q.qsize())   # report on the size of the queue
print ('1st element  ==> ', q.get())     # pop item off queue and report
print ('2nd element  ==> ', q.get())
print ('3rd element  ==> ', q.get())
print ('Queue size   ==> ', q.qsize())
