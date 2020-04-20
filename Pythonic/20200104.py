"""
第一章 引论
@ 北京宴酒店二楼 2020_01_04
"""


def quicksort(array):
    """快排"""
    less = []
    greater = []
    if len(array) <= 1:
        return array
    pivot = array.pop()
    for each in array:
        if each <= pivot:
            less.append(each)
        else:
            greater.append(each)
    return quicksort(less) + [pivot] + quicksort(greater)  # +号是新建一个对象，而extend是扩展第一个列表


test_array = [3, 4, 1, 5, 4, 9, 0, 5, 7]
print(quicksort(test_array))
print(quicksort(test_array)[2])


# 字符串格式化

print('Hello %s!' % ('Tom',))  # 1)

print('Hello %(name)s!' % {'name': 'Tom'})  # 2)

strs = {'greet': 'Hello world', 'language': 'Python'}
print()
