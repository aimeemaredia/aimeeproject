#_middleware.py_
#import threading 
from threading import current_thread

#define constant request 
_REQUESTS = {}

#class for showing exception messages
class RequestNotFound(Exception):
    def __init__(self, message):
        self.message = message

#function to get request information from any file in the project 
def get_request():
    thread = current_thread()                         #define the caller's thread and of control and store in variable
    if thread not in _REQUESTS:                       # if thread is not found then raise error 
        raise RequestNotFound('global request error') #print error
    else:                                             # if thread is found then assign to constant 
        return _REQUESTS[thread]


#class for middleware functions 
class RequestMiddleware(object):
    def __init__(self, get_response):                 #initiate class with var get_response 
        self.get_response = get_response              #assign var to self 

    def process_request(self, request):               #function to get the current request from the thread 
        _REQUESTS[current_thread()] = request

    def __call__(self, request):                      #functiont to assifn request to response var
        self.process_request(request)
        response = self.get_response(request)

        return response                               #return response 
