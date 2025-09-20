def serve_chai():
    yield "Chai served"
    yield "Chai finished"
    yield "Cup cleaned"

stall = serve_chai()

for cup in stall:
    print(cup)

def get_chai_list():
    return ["Chai served", "Chai finished", "Cup cleaned"]

# generator version
def get_chai_generator():
    yield "Chai served"
    yield "Chai finished"
    yield "Cup cleaned"

chai_list = get_chai_list()
for cup in chai_list:
    print(cup)

chai_generator = get_chai_generator()
for cup in chai_generator:
    print(next(cup))