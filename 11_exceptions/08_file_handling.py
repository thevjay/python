# file = open("order.txt","w")
# try:
#     file.write("I want 10 burgers")
# finally:
#     file.close()

with open("order.txt","w") as file:
    file.write("I want 30 burgers")
# with open("order.txt","r") as file:
#     print(file.read())
