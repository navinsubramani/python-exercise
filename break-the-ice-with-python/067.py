# Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.


def binarysearch(li, element):
    left = 0
    right = len(li)-1

    while True:
        mid = left + int((right-left)/2)
        if right-left < 2:
            mid = -1
            break

        if li[mid] == element:
            break

        elif li[mid] > element:
            right = mid

        elif li[mid] < element:
            left = mid

    return mid


li = [2, 5, 7, 11, 17, 100]
print(binarysearch(li, 7))
print(binarysearch(li, 17))
print(binarysearch(li, 19))
print(binarysearch(li, 3))
print(binarysearch(li, 0))
print(binarysearch(li, 101))

li = [2, 5, 7, 12, 11, 17, 100]
print(binarysearch(li, 7))
print(binarysearch(li, 17))
print(binarysearch(li, 12))
print(binarysearch(li, 3))
print(binarysearch(li, 0))
print(binarysearch(li, 101))
