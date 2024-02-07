def page_list(start, end):
    pagelist = []
    for n in range(start, end):
        pagelist.append(n + 1)
    return [max(pagelist), min(pagelist), max(pagelist) - 2, min(pagelist) + 2, max(pagelist) - 4, min(pagelist) + 4,
            max(pagelist) - 6, min(pagelist) + 6], [min(pagelist) + 1, max(pagelist) - 1, min(pagelist) + 3,
                                                    max(pagelist) - 3,
                                                    min(pagelist) + 5, max(pagelist) - 5, min(pagelist) + 7,
                                                    max(pagelist) - 7]


if __name__ == '__main__':
    numbers_of_page = 250
    h = [1, 2, 3, 4, 5, 6, 7, 8, ]
    # print(page_list(0, 16))
    for n in range((int(numbers_of_page / 16)) + 1):
        print(page_list(n * 16, (n * 16) + 16))
