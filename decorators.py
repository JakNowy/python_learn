# # FUNCTION BASED DECORATORS
# def decorator_function(original_function):
#     def wrapper_function():
#         print('Logic before')
#         result = original_function()
#         print('Logic after')
#         return result
#     return wrapper_function
#
# @decorator_function
# def original_function():
#     print('Original function')
#
#
# original_function()
#
#
#
# f1 = decorator_function(original_function)

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

        # Functools handles naming of wrapped functions (its .__name__ method)
        @functools.wraps(original_function)
        def wrapper(*args, **kwargs):
            # Adds logic before and after original_function
            print('Logic before')
            result = original_function(*args, **kwargs)
            self.counter += 1
            print('Logic after')
            print(f'Decorator_argument = {self.decorator_argument}')
            return result

        return wrapper


# EXECUTING USING @DECORATOR SYNTAX
@DecoratorClass(decorator_argument=5)
def original_function2(a, b):
    print(f'This is original function. It has function arguments a = {a} and b = {b}')


original_function2(1, 2)


# EXECUTING MANUALLY
def original_function1(a, b):
    print(f'This is original function. It has function arguments a = {a} and b = {b}')


# __INIT__
decorator_object = DecoratorClass(decorator_argument=5)
# __CALL__
decorator_closure = decorator_object(original_function1)
# Closure execution
decorator_closure(1, 2)
