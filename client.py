import requests, json, os, random, string,  threading, time


#url = "http://77.237.53.201:8113/"
#url = "http://localhost:5001/"
url = "http://172.16.0.10/"

def sending_names(name):
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@gmail.com'
    password = ''.join(random.choice(string.ascii_letters) for i in range(8))

    response = requests.put(url, data={
        "name1": username,
        "name2": password
    })

    return(response)

def do_requests():
    names = json.loads(open('names.json').read())
    _filename = "logs/" + str(threading.current_thread().name)
    print(_filename)
    f = open(_filename,"w")
    while True:
        response = sending_names(random.choice(names))
        f.write(str(response.status_code))
        time.sleep(0.01)



threads = []

num_threads = 10

for i in range(num_threads):
    t = threading.Thread(target=do_requests)
    t.daemon = True
    threads.append(t)

for i in range(num_threads):
    threads[i].start()

print("started ...")

for i in range(num_threads):
    threads[i].join()
