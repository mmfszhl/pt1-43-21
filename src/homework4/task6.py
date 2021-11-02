'''
6.Упорядоченный список.
Дан список целых чисел.
Требуется переместить все ненулевые элементы в левую часть списка,
не меняя их порядок, а все нули - в правую часть.
Порядок ненулевых элементов изменять нельзя, дополнительный список использовать нельзя,
задачу нужно выполнить за один проход по списку. Распечатайте полученный список.
'''


def main(input_lst, bad_num):
    print('Input:', input_lst)
    lst_len = len(input_lst)
    for ind in range(lst_len):
        if input_lst[ind] != bad_num:
            continue
        input_lst.insert(lst_len, bad_num)
        input_lst.remove(bad_num)

    print('Result:', input_lst)


main([1, 2, 0, 3, 5, 9, 0, 1, 4, 2], 0)
