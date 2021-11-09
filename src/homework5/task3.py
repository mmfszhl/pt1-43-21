'''
3.Даны два списка чисел.
Посчитайте, сколько различных чисел содержится одновременно
как в первом списке, так и во втором.
'''


def main():
    l1 = [1, 2, 3, 5, 7]
    l2 = [2, 9, 3, 1]
    l_res = list(set(l1) & set(l2))

    print('List1:', l1, 'List2:', l2, 'Result:', l_res, 'Len:', len(l_res), sep='\n')


main()