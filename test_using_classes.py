def factorial(num):
    return 1 if num <= 1 else num * factorial(num - 1)


class TestUsingClass(object):

    def test_factorial_5(self):
        assert factorial(5) == 120

    def test_factorial_10(self):
        assert factorial(10) != 10
