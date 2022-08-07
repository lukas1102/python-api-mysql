from asyncore import read
import requests, json, os, random, string,  threading, time


url = "http://77.237.53.201:8113/"
#url = "http://localhost:5001/"
#url = "http://172.16.0.10/"

file_write = "logs/write.log"
file_read = "logs/read.log"
lock1 = threading.Lock()
lock2 = threading.Lock()


def sending_names(name):
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@gmail.com'
    password = ''.join(random.choice(string.ascii_letters) for i in range(8))

    response = requests.put(url, data={
        "name1": username,
        "name2": password
    })
    return(response)

def do_write_requests(_file):
    
    names = json.loads(open('names.json').read())
    while True:
        response = sending_names(random.choice(names))
        lock1.acquire()
        f = open(_file,"a")
        f.write(str(response.status_code) + " \n")
        f.close()
        lock1.release()
        time.sleep(0.01)

def do_read_requests(_file1):
    _url = url + "one"
    response = requests.get(_url)
    lock2.acquire()
    f1 = open(_file1,"a")
    f1.write(str(response.status_code) + " \n")
    f1.close()
    lock2.release()
    time.sleep(0.001)
        
threads = []

num_threads = 10


for i in range(num_threads):
    if i % 2 == 0:
        t = threading.Thread(target=do_write_requests, args=(file_write,))
    else:
        t = threading.Thread(target=do_read_requests, args=(file_read,))
    t.daemon = True
    threads.append(t)

for i in range(num_threads):
    threads[i].start()

print("started ...")

input()

for i in range(num_threads):
    threads[i].join()
