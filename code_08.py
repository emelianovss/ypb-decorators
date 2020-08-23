from code_06 import Router
from task_04 import cache

router = Router()


@router.route('s')
@cache
def my_sum(*args):
    return sum(args) * 2

# my_sum = router.route('s')(cache(my_sum))

router('s', 10, 20)
router('s', 10, 20)
router('s', 10, 20)


@cache
@router.route('d')
def my_diff(a, b):
    return a - b

router('d', 8, 4)
router('d', 8, 4)

# my_diff = cache(router.route('d')(my_diff))
