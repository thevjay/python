import threading
import time

chai_stock = 0

def restock():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1
        print(f"Restocked chai. Current stock: {chai_stock}")

threads = [threading.Thread(target=restock) for _ in range(2)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Final chai stock: {chai_stock}")