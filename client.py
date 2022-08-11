from asyncore import read
from datetime import datetime
from requests.models import Response
import requests, json, os, random, string,  threading, time


#url = "http://77.237.53.201:8113/"
#url = "http://localhost:5001/"
url = "http://172.16.0.10/"

file_write = "logs/write.log"
file_read = "logs/read.log"
lock1 = threading.Lock()
lock2 = threading.Lock()


def sending_names():
    #name_extra = ''.join(random.choice(string.digits))
    #user = name.lower() + name_extra + '@gmail.com'
    user = random.randint(0,3)
    invoice = ''.join(str(random.randint(0,9)) for i in range(7))
    price = random.randint(100,1000)
    try:
        r = requests.session()
        response = r.put(url, data={
            "name1": user,
            "name2": invoice,
            "name3": price
        })
        r.close()
    except:
        fake_response = Response()
        fake_response.status_code = 500
        return(fake_response)
    return(response)

def do_write_requests(_file):
    
    #names = json.loads(open('names.json').read())
    while True:
        t = getTime()
        response = sending_names()
        lock1.acquire()
        f = open(_file,"a")
        f.write(t + str(response.status_code) + " \n")
        f.close()
        lock1.release()
        time.sleep(0.1)
        global stop_threads
        if stop_threads:
            break

def do_read_requests(_file1,):
    while True:
        _url = url + "one"
        t = getTime()
        try:
            r = requests.session()
            response = r.get(_url)
            r.close()
        except:
            response = Response()
            response.status_code = 500
        lock2.acquire()
        f1 = open(_file1,"a")
        f1.write(t + str(response.status_code) + " \n")
        f1.close()
        lock2.release()
        time.sleep(0.1)
        global stop_threads
        if stop_threads:
            break

def getTime():
    now = datetime.now()
    date = now.strftime("%y-%m-%d")
    time = now.strftime("%H:%M:%S:")
    mili = int(now.microsecond / 1000)
    return str(date) +  "," + str(time) + str(mili)+ ","
threads = []

num_threads = 500

stop_threads = False

for i in range(num_threads):
    if i % 10 == 0:
        t = threading.Thread(target=do_write_requests, args=(file_write,))
    else:
        t = threading.Thread(target=do_read_requests, args=(file_read,))
    t.daemon = True
    threads.append(t)

for i in range(num_threads):
    threads[i].start()

print("started ...")

time.sleep(40)

stop_threads = True

for i in range(num_threads):
    threads[i].join()
