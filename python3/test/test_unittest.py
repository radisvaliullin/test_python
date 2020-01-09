# Test unittest lib

from unittest.mock import MagicMock, patch


class SomeClass:

    def __init__(self):
        pass

    def method(self, *args, **kwargs):
        self.method2(*args)
        return

    def method2(self, *args):
        pass
        return


def some_function():
    instance = SomeClass()
    return instance.method()


with patch('test_unittest.SomeClass') as mock:
    instance = mock.return_value
    instance.method.return_value = 'the result'
    result = some_function()
    # assert result == 'the result'


if __name__ == '__main__':
    print('test unittest')

    sc = SomeClass()
    sc.method2 = MagicMock()

    sc.method(1, 2, 3)
    print(sc.method2.assert_called_with(1, 2, 3))

    sc.method(1, 2, 3, 4)
    print(sc.method2.assert_called_with(1, 2, 3, 4))

    print('test unittest end')
