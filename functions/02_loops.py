def main():
    result_dict = {}
    list_10 = list(range(10))
    range_10 = range(10)

    for i in list_10:
        print('list: {}'.format(i))

        result_dict[f'list {i}'] = i**2

    for j in range_10:
        print('range: {}'.format(j))

        result_dict[f'range {j}'] = j ** 2


if __name__ == "__main__":
    main()
