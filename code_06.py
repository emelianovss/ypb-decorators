class Router:
    def __init__(self):
        self._routes = {}
    
    def route(self, path):
        def inner(func):
            self._routes[path] = func
        return inner
    
    def default(self, *args, **kwargs):
        return 'Not found'
    
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
    router('sum', 1, 2, 3)
    router('inc', 10)
    router('other')