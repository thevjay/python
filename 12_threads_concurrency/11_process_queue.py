from multiprocessing import Process, Queue, Value

# Queue is a thread and process safe data structure that can be used to share data between processes.

def prepare_chai(queue):
    queue.put("Chai is ready")

counter = Value('i', 0)  # Shared integer

if __name__ == "__main__": 
    queue = Queue()

    p = Process(target=prepare_chai, args=(queue,))
    p.start()
    p.join()

    print(queue.get())  # Blocks until data is available