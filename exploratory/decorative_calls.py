"""
After using a class implementing __call__ dunder as a decorator - what else can we do in that vein?

OK, so the structure is:
def decorator_name(decorator_args, decorator_kwargs):
    def decorator(item_to_decorate):
        def wrapper(args, kwargs):
            <computations>

        return wrapper
    return decorator
"""
import functools


def cook(*decorator_args, **decorator_kwargs):
    def decorator(func):
        decorator._kwargs.update(decorator_kwargs)

        @functools.wraps(func)
        def wrapper(key, *args, **kwargs):
            print(f"Cook: {decorator_args[0]} will be cooking {key}")
            if key in decorator._kwargs:
                func(decorator._kwargs[key], *args, **kwargs)
            else:
                func("Rocky Mountain Oysters", *args, **kwargs)

        return wrapper

    decorator._kwargs = {}
    return decorator


def condiments(*decorator_args):
    def decorator(func):
        decorator._args += [item for item in decorator_args]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if 'condiments' in kwargs:
                kwargs['condiments'] += decorator._args
            else:
                kwargs.append({'condiments': decorator._args})
            func(*args, **kwargs)

        return wrapper
    decorator._args = []
    return decorator


# Note: We have a conflict here because double decorator
@condiments('Water vole', {'Kraft parmesan': ['Cellulose', 'Chalk', 'Salt', 'Traces of Parmesan cheese']})
@cook('Joe', fish='Cod', meat='Pork', vegetable='Eggplant')
@condiments('Ketchup')
def cook(what, **kwargs):
    print(f"Cooking {what}")
    print(f"Condiments, spices and stuff: {kwargs.get('condiments')}")


if __name__ == "__main__":
    cook("fish", condiments=['Salt', 'Lemon'])
    cook("meat", condiments=['Salt', 'Marjoram'])
    cook("vegetable", condiments=['Salt', 'Pepper', 'Onions'])
