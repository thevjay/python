class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]

      
# " Water, Milk, Sugar, Tea Leaves " -> ['Water', 'Milk', 'Sugar', 'Tea Leaves']

# raw = " Water, Milk, Sugar, Tea Leaves "
# cleaned = ChaiUtils.clean_ingredients(raw)
# print(cleaned)
# # ['Water', 'Milk', 'Sugar', 'Tea Leaves']

# add @staticmethod decorator to the method
raw = " Water, Milk, Sugar, Tea Leaves "
cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)