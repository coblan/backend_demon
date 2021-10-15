from waitress import serve
import os
import signal
from wsgi import application

from whitenoise import WhiteNoise
import threading

application = WhiteNoise(application, root=r'D:\work\part3\backend_demon')
application.add_files(r'D:\work\part3\backend_demon\media', prefix='media')
application.add_files(r'D:\work\part3\backend_demon\src\static', prefix='static')


def start():
    print('开始')
    serve(application, port='8077')
    print('退出')
    
if __name__ == '__main__':
    import webview
    webview.create_window('Hello world', 'http://localhost:8077')
     
     
    thread = threading.Thread(target=start)
    thread .start()
    webview.start()  
    os.kill(os.getpid(), signal.SIGINT)
    #glob['serve'].shutdown()