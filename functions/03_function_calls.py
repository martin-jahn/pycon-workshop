def compose_string(type_, number):
    print(f'{type_}: {number}')


def main():
    list_10 = list(range(10))
    range_10 = range(10)

    for i in list_10:
        compose_string('list', i)

    for j in range_10:
        compose_string('range', j)


if __name__ == "__main__":
    main()
