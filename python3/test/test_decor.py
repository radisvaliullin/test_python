
def deco(arg):
    print('deco_arg is', arg)

    def deco2(f):
        def wrapper(*args, **kwargs):
            print('wrapped')
            f(*args, **kwargs)
            print('wrapped end')
        return wrapper

    return deco2


@deco('qwerty')
def one(arg):
    print('arg is', arg)


if __name__ == '__main__':
    print('main begin')

    one('test')
