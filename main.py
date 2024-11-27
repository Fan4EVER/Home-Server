import os
import http.server
import socketserver

#class Handler(http.server.SimpleHTTPRequestHandler)
    
def setup(path):

    list = os.listdir(path)
    return(list)
    
setup('/home/clint/Documents/New_Server')
    

