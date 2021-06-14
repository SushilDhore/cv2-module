#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import socket
import base64
import os
import time
import threading


# In[ ]:


def videoreciver():
    s=socket.socket()
    ip="100.24.20.26"
    port=2026
    s.connect((ip,port))
    i=0
    while True:
        time.sleep(0.8)
        try:
            data =s.recv(100000000)
            #print(data)
            imgdata = base64.b64decode(data)
            filename="{}.jpg".format(i)
            with open(filename, 'wb') as f:
                f.write(imgdata)

            image= "image"+"{}".format(i)
            image=cv2.imread(filename)

            print(image)
            cv2.imshow('sushil Calling...',image)
            os.remove("{}.jpg".format(i))
            i=i+1
            if cv2.waitKey(100) == 13:
                break

        except:
            pass
    cv2.destroyAllWindows()


# In[ ]:


def videosender():
    #sending video
    s=socket.socket()
    ip="100.24.20.26"
    port=2024
    s.connect((ip,port))
    cap=cv2.VideoCapture(0)
    while True:
        time.sleep(0.8)
        ret,photo=cap.read()
        cv2.imwrite("videocall.jpg",photo)
        with open("videocall.jpg", 'rb') as f:
            image_encoded=base64.b64encode(f.read()) #encoding image...
        s.send(image_encoded)


# In[ ]:


t_recv=threading.Thread(target=videoreciver)
t_send=threading.Thread(target=videosender)
t_recv.start()
t_send.start()


# In[ ]:




