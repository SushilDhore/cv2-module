#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket 
import time
import threading


# In[2]:


pranay_recv_s=socket.socket()
pranay_recv_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1) #this is done so that we can reuse a port, otherwise everytime we have 
#to kill service because till some time port is remains active


# In[3]:


sushil_recv_s=socket.socket()
sushil_recv_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)


# In[4]:


pranay_send_s=socket.socket()
pranay_send_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)


# In[5]:


sushil_send_s=socket.socket()
sushil_send_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)


# In[8]:


pranay_recv_port=2024 #recive from Aman Dev Verma
sushil_recv_port=2025 #recive from Manasvi Agarwal
pranay_send_port=2026 #send to Aman Dev Verma
sushil_send_port=2027 #send to Manasvi Agarwal
ip=
pranay_recv_s.bind((ip, k_recv_port))
sushil_recv_s.bind((ip, s_recv_port))
pranay_send_s.bind((ip, k_send_port))
sushil_send_s.bind((ip, s_send_port))


# In[9]:


pranay_recv_s.listen()
sushil_recv_s.listen()
pranay_send_s.listen()
sushil_send_s.listen()


# In[10]:


pranay_recv_s.listen()
sushil_recv_s.listen()
pranay_send_s.listen()
sushil_send_s.listen()


# In[ ]:


pranay_recv_session, k_recv_addr = k_recv_s.accept()
sushil_recv_session, s_recv_addr = s_recv_s.accept()
pranay_send_session, k_send_addr = k_send_s.accept()
sushil_send_session, s_send_addr = s_send_s.accept()


# In[ ]:


#above we have created total 4 socket 1) it will recive image in bytes from person2
#2)it will send those bytes recived by person2 to the person1
#3)it will recive image in bytes from person1
#2)it will send those bytes recived by person1 to the person2
def k_recv() #it will recive from digamber and send to Manasvi
    while True
        data=k_recv_session.recv(10000000)
        time.sleep(2)
        s_send_session.send(data)

def s_recv() #it will recive from deepak and send to Aman
    while True
        data=s_recv_session.recv(10000000)
        time.sleep(2)
        k_send_session.send(data)
#used threading so that above both function will run parellely
a1_recv=threading.Thread(target=k_recv)
m1_recv=threading.Thread(target=s_recv)
a1_recv.start()
m1_recv.start()


# In[ ]:




