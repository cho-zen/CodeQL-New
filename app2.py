A="rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr"
 
def example_function():
    if True:
        print("This is indented with 2 spaces")
        for i in range(3):
            print(f"Nested loop iteration {i}")
    else:
        print("This is the 'else' block")
    print("Function call completed.")

example_function()

def my_function_name(arg1, arg2, arg3):
    print(f"Hello from a function with too many arguments. Arguments: {arg1}, {arg2}, {arg3}")

class my_class_name:
    def __init__(self):
        self.my_instance_var = 42

    def my_method(self, param1, param2):
        print(f"Instance method with invalid name. Params: {param1}, {param2}")

my_instance = my_class_name()


'''<<--To check name convention error-->>'''
MY_CONSTANT = 42

class MyClass:
    def __init__(self):
        self.my_instance_variable = 100

    def myMethod(self):
        pass

class AnotherClass:
    pass

def function_name():
    pass

# Invalid examples
# lowercase is used in class name
class myclass:
    pass

# Digits in class name
class Class1:
    pass

# Starts with a lowercase letter
MyVariable = 100

# Invalid variable name
my_variable = 10


'''<<--TPython code example that contains instances of both no-member and unused-argument issues-->>'''

class MyClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def method1(self):
        return self.arg1

    def method2(self, unused_arg):
        return self.arg2

class AnotherClass:
    def __init__(self):
        self.value = 42

    def method(self):
        print("This method does not use its argument")

def unused_function(unused_parameter):
    print("This function does not use its argument")

obj = MyClass(10, 20)
result1 = obj.method1()
result2 = obj.method2(5)

obj2 = AnotherClass()
obj2.method()

unused_function(123)

# Invalid examples that will trigger linting errors
# These issues are enabled in the configuration
obj.invalid_method()  # no-member issue
obj.method2()  # unused-argument issue

