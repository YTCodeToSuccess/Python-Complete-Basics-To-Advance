'''
This section we will cover everything about iterables in Python.
Like lists, tuples, sets, dictionaries, strings, etc.
and will see most common operations that can be performed on them.
'''


if __name__ == "__main__":

    # empty list
    my_list = []
    # empty list by using list() function
    my_list = list()

    # converting other data structures to list
    str = 'hello'
    my_list = list(str)
    print(my_list)  # ['h', 'e', 'l', 'l', 'o']

    # get elements from the negative index
    my_list = [1, 2, 3, 4, 5]
    print(my_list[-1])  # 5
    print(my_list[-2])  # 4
    print(my_list[-3])  # 3 and so on

    # slicing the list
    my_list = [1, 2, 3, 4, 5]
    print(my_list[1:4])  # [2, 3, 4]
    print(my_list[:4])   # [1, 2, 3, 4]
    print(my_list[1:])   # [2, 3, 4, 5]
    print(my_list[:])    # [1, 2, 3, 4, 5]
    print(my_list[::2])  # [1, 3, 5]
    print(my_list[1::2]) # [2, 4]
    print(my_list[::-1]) # [5, 4, 3, 2, 1] (reversing the list)

    # append elements to the list
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list)  # [1, 2, 3, 4]  # appending single element  
    my_list.append([5, 6])
    print(my_list)  # [1, 2, 3, 4, [5, 6]]  # appending list as single element

    #In order to merge two lists, we can use extend() method or += operator
    my_list = [1, 2, 3]
    my_list.extend([4, 5])
    print(my_list)  # [1, 2, 3, 4, 5]  # extending list by another list
    my_list += [6, 7]
    print(my_list)  # [1, 2, 3, 4, 5, 6, 7]  # extending list by another list
