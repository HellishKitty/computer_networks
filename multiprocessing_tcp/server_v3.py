import socket, pickle
from multiprocessing import Process as pr


processes = []
count = 0


def process_task(p_id):
    global processes
    global count
    print("process ", p_id, " started")
    print("active clients ", count)
    print("exiting process ", p_id)


    i = count + 1
    p = pr(target=process_task, args=(i,))
    processes.append(p)
    print(len(processes))
    p.start()