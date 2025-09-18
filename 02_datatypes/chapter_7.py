malasa_spices = ("cardamom","cloves","cinnamon")

(spice1,spice2,spice3) = malasa_spices

print(f"Main masala spices are: {spice1}, {spice2}, and {spice3}.")

ginger_ratio, cardamom_ratio= 2,1
print(f"Ratio is G: {ginger_ratio}, C: {cardamom_ratio}")
ginger_ratio, cardamom_ratio= cardamom_ratio, ginger_ratio
print(f"Ratio is G: {ginger_ratio}, C: {cardamom_ratio}")


# membership - in operator 

print(f"Is ginger in masala spices ? {'ginger' in malasa_spices}")
print(f"Is ginger in masala spices ? {'cinnamon' in malasa_spices}")