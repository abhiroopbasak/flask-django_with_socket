import flask
from flask import Flask, render_template, request
import socket

web_site=Flask(__name__)

s.socket.socket()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ip=""
port=8000
s.bind( (ip,port) )
s.listen(8000)
csession,addr=s.accept()

@web_site.route('/')
def index():
  return render_template('index.html')
  
@web_site.route('/user')
def generate_user():
  z=csession.recv(1024)
  ctg1=z.decode()
  z=csession.recv(1024)
  ctg2=z.decode()
  return render_template('videopage.html',category1=ctg1,category2=ctg2)
  
  web_site.run(host='0.0.0.0',port=8080)
  
  if __name__=="__main__":
    web_site.run(debug=True)
