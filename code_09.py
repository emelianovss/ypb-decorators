class User:
    def __init__(self, name):
        self.name = name


class Request:
    def __init__(self, path, cookie):
        self.path = path
        self.cookie = cookie
        self.user = None


class Router:
    def __init__(self):
        self._routes = {}
    
    def route(self, path):
        def inner(func):
            self._routes[path] = func
        return inner
    
    def default(self, *args, **kwargs):
        return 'Not found'
    
    def __call__(self, request):
        print(self._routes.get(request.path, self.default)(request))


def auth(users):
    def inner(func):
        def wrapper(request):
            user = users.get(request.cookie)
            if user:
                request.user = user
                return func(request) 
            else:
                raise ValueError('Auth required')
        return wrapper
    return inner


if __name__ == '__main__':
    router = Router()
    users = {
        u.name: u 
        for u in [User('John'), User('Liza')]
    }

    @router.route('me')
    @auth(users)
    def handler(request):
        return f'Request user {request.user.name}'


    @router.route('v')
    def version(request):
        return f'Application version'


    router(Request('me', 'John'))

    print()
    router(Request('v', 'John'))

    print()
    router(Request('me', 'Jack'))