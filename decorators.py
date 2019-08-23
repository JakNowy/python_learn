# FUNCTION BASED DECORATORS
# def decorator_function(function):
#     def wrapper_function():
#         print('Before')
#         return function()
#     return wrapper_function
#
#
# @decorator_function
# def function():
#     print('Original function')
#
#
# # f1 = decorator_function(function)
# # f1()
#
# function()


# CLASS BASED DECORATORS
import functools


class DecoratorClass:
    def __init__(self, decorator_argument):
        """
        Instantiation of decorator_object, like decorator_object = DecoratorClass(arg)
        :param arg: Argument of decorator.
        """
        self.counter = 0
        self.decorator_argument = decorator_argument

    def __call__(self, original_function):
        """
        Called when the decorator_object gets called, like decorator_closure = decorator_object(original_function).

        Returns actual decorator_closure ready to be executed.
        @decorator syntax executes this step automatically.
        """

        @functools.wraps(original_function)
        # Handles naming of wrapped functions (its .__name__ method)
        def wrapper(*args, **kwargs):
            # Adds logic before and after original_function
            print('Additional decorator logic BEFORE')
            result = original_function(*args, **kwargs)
            print('Additional decorator logic AFTER')
            print(f'Decorator_argument = {self.decorator_argument}')
            return result
        return wrapper


print('CLASS BASED DECORATORS RESULTS:')


def original_function1(a, b):
    print(f'This is original function. It has function arguments a = {a} and b = {b}')
    return 'Hello1'


# EXECUTING MANUALLY
print('\nExecuting manually:')
# __INIT__
decorator_object = DecoratorClass(decorator_argument=5)

# __CALL__
decorator_closure = decorator_object(original_function1)

# Closure execution
decorator_closure(1, 2)


# EXECUTING USING @DECORATOR SYNTAX
print('\nUsing @decorator syntax:')
@DecoratorClass(decorator_argument=5)
def original_function2(a, b):
    print(f'This is original function. It has function arguments a = {a} and b = {b}')
    return 'Hello2'


original_function2(1, 2)
