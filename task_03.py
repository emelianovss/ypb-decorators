"""
>>> router('sum', 'POST', 1, 2, 3)
Sum is 6
>>> router('inc', 'GET', 5)
Incremented is 6
"""

class Router:
    def __init__(self):
        self._routes = {}
    
    # Change here
    def route(self, path):
        def inner(func):
            self._routes[path] = func
        return inner
    
    def default(self, *args, **kwargs):
        return 'Not found'
    
    # Change here
    def __call__(self, path, *args, **kwargs):
        print(self._routes.get(path, self.default)(*args, **kwargs))


router = Router()

@router.route('sum')
def handler(*args):
    return f'Sum is {sum(args)}'


@router.route('inc')
def increment(arg):
    return f'Incremented is {arg + 1}'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
