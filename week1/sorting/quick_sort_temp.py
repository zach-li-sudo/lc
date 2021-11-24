def quick_sort(a, begin, end):
    if len(a) == 1:
        return
    if begin < end:
        pivot = partition(a, begin, end)
        quick_sort(a, begin, pivot-1)
        quick_sort(a, pivot+1, end)


def partition(a, begin, end):
    pivot = a[end]
    counter = begin-1

    for i in range(begin, end):
        if a[i] <= pivot:
            counter += 1
            a[i], a[counter] = a[counter], a[i]

    a[counter+1], a[end] = a[end], a[counter+1]
    return counter+1



from random import randint

a = [randint(-20, 20) for i in range(10)]
print(a)
quick_sort(a, 0, len(a)-1)
print(a)