permitted_names = ["Ghasem", "Gholi", "Ghanbar"]

name = input("namat ra begu: ")

def _decorator_login_required():
    def decorator(view_func):
        print("view functionin decorator: ", view_func)
        def wrapper(name):
            if name not in permitted_names:
                print("khodafez")
            else:
                view_func(name)
        return wrapper
    return decorator

def decorator_login_required(function=None, x=12):
    print("function: ", function)
    result = _decorator_login_required()
    if function:
        return result(function)
    return result


@decorator_login_required(x=12)
def salam(name):
    print(f"salam {name}")

# salam = decorator_check_name(salam)
salam(name)