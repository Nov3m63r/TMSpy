# 1_8*

lst = [88, 90, 77, 55, 6, 42, 9, 28, 88, 18, 33, 36, 23, 81, 30, 54.2, 37, 46, 34, 20, 22, 54, 87, 73, 17,
       52, 57, 61, 55, 5, 61, 51, 53, 20, 5, 29, 13, 42, 35, 15, '15.2', 60, 32, 81, 63, 49, 73, 77, 23, 91,
       1, 48, 33, 35, 70, 7, 10, 33, 3, 7, 46, 66, 16, 4, 60, 65, 43, 28, 35, 26, 84, 84, 88, 48, 63, 6, 61,
       15, 70, 57, 64, 77, None, 33, 30, 24, 65, 55, 100, 22, 47, 44, 64, 94, 76, 19, 74, 85, 37, 41, 95, 18]


def count_list(arg):
    a = arg[0]
    counter = [a]
    for i in arg:
        if type(i) == int or type(i) == float:
            if i > a:
                a = i
                counter.append(a)
    return len(counter)


print(count_list(lst))
