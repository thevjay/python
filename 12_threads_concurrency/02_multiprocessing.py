from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start of Brewing chai for {name}")
    time.sleep(3)
    print(f"End of Brewing Chai for {name} is ready")

if __name__ == '__main__':
    chai_makers = [
        Process(target=brew_chai, args=(f"Customer-{i+1}",))
        for i in range(3)
    ]

    # start all processes
    for p in chai_makers:
        p.start()

    # wait for all processes to complete
    for p in chai_makers:
        p.join()

    print("All tasks completed.") 


