from pytest import fixture


def fib_rec(n):
    if 3 > n > 0:
        return 1
    elif n >= 3:
        return fib_rec(n - 1) + fib_rec(n - 2)
    elif n == 0:
        return 0
    else:
        return "Error"


@fixture
def fun():
    return fib_rec


def test_fib(fun):
    cases = {
        0: 0,
        1: 1,
        2: 1,
        10: 55,
        12: 144,
        15: 610,
        17: 1597,
        -1: "Error",
        -10: "Error",
        20: 6765,
    }
    for key, value in cases.items():
        print(f'{fun.__name__}("{key}") == {fun(key)}')
        assert fun(key) == value
