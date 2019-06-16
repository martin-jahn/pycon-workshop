import requests
from time import sleep


def get_range(length):
    for i in range(length):
        yield i


def generator(length):
    x = 42
    yield from get_range(length)
    print('x is {}'.format(x))


def main():
    ge = generator(5)
    for i in ge:
        print(f'got {i} from iterator')

    r = requests.get('http://localhost:4000/request')
    print('fin')


if __name__ == "__main__":
    main()
