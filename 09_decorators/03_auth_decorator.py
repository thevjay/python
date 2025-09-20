from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != 'admin':
            print("Access denied. Admins only.")
            return None
        else:
            print("Access granted.")
            return func(user_role)
    return wrapper

@require_admin
def access_tea_inventory(role):
    print("Accessing tea inventory...")

# Test the decorator
access_tea_inventory('guest')  # Should print "Access denied. Admins only."
access_tea_inventory('admin')  # Should print "Access granted." and then "Accessing tea inventory..."