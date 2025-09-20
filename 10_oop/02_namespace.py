class Chai:
    origin = "India"

print(Chai.origin)  # India

Chai.origin = "China"
print(Chai.origin)  # China

# creating objects from class Chai
masala_tea = Chai()
print(masala_tea.origin)  # China
p