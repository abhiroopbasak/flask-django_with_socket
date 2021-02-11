from django.http import HttpResponse
from django.shortcuts import render
import socket


s=socket.socket()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip="13.235.79.157"
port=8000
s.connect( (ip,port) )


def index(request):
  return render(request,'index.html')

def enter(request):
  return render(request,'form.html')


def video(request):
  
  cont=request.GET['category']
  if cont=='cat':
    s.send(b"DXUAyRRkI6k")
    
  elif cont=='dog':
    s.send(b"lyelxGIydeQ")
    
  elif cont=='cooking':
    s.send(b"D0ijxagCEzA")
    
  elif cont=='comedy':
    s.send(b"MsIfrNF25pU")
    
  elif cont=='sports':
    s.send(b"VqLkx5B2pqg")
    
  elif cont=='django':
    s.send(b"OTmQOjsl0eg")
    
  elif cont=='flask':
    s.send(b"Z1RJmh_OqeA")
    
  elif cont=='music':
    s.send(b"2Vv-BfVoq4g")
    
  return render(request,'form.html')
