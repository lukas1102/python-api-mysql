import requests, os, random, string, json, threading


chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

#url = 'http://localhost:5001/'
#url = 'http://77.237.53.201:8113/'
url = 'http://172.16.0.10/'


def sending(name):
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@gmail.com'
    password = ''.join(random.choice(chars) for i in range(8))

    response = requests.put(url, data={
        "name1": username,
        "name2": password
    })

    #print("sending username %s and password %s, %s" % (username,password, response))
    print(response)

def do_requests():
    names = json.loads(open('names.json').read())
    while True:
        sending(random.choice(names))

threads = []

num_threads = 1

for i in range(num_threads):
    t = threading.Thread(target=do_requests)
    t.daemon = True
    threads.append(t)

for i in range(num_threads):
    threads[i].start()

print("started ...")

for i in range(num_threads):
    threads[i].join()


