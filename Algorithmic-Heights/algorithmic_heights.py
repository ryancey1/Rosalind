#! /usr/bin/env python3

import random

def fibonacci_memoized(n, memo = {0:0, 1:1}):
    if n in memo:
        return memo[n]
    else:
        memo[n-1], memo[n-2] = fibonacci_memoized(n-1, memo), fibonacci_memoized(n-2, memo)
        return memo[n-1] + memo[n-2]


def fibonacci_recursive(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

    
def binary_search(value, array, start, end):
    """ Find a value in a sorted array, if it exists. Returns (1-based) index in array wherein value is positioned. Returns -1 if nonexistent. """
    
    assert sorted(array) == array # confirm the array is sorted
    
    l, r = start, end
    m = (l + (r - l) // 2) 
    
    if l <= r:
        if value == array[m]:
            return m + 1
        elif array[m] > value:
            return binary_search(value, array, l, m-1)
        else:
            return binary_search(value, array, m+1, r)
    else:
        return -1

def insertion_sort(arr, n, swaps = 0):
    
    for i in range(1, n):
        k = i
        while k > 0 and arr[k] < arr[k-1]:
            swap(arr, k-1, k)
            swaps += 1
            k -= 1
    return swaps

def majority_element(arr, n):
    elements = {}
    for i in arr:
        elements[i] = elements.get(i, 0) + 1
    if max(elements.values()) > n/2:
        return max(elements, key = elements.get)
    else:
        return str(-1)


def mergesort(A, length):
    if length == 1:
        return A
    left = mergesort(A[:length//2], len(A[:length//2]))
    right = mergesort(A[length//2:], len(A[length//2:]))
    return merge(left, right, len(left), len(right))


def merge(l, r, llen, rlen):
    arr = [0 for _ in range(llen+rlen)]
    i, j, k = 0, 0, 0
    while i < llen and j < rlen:
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
    while i < llen:
        arr[k] = l[i]; k += 1; i += 1
    while j < rlen:
        arr[k] = r[j]; k += 1; j += 1
    return arr


def max_heapify(arr, n, i):
    largest = i
    left_child, right_child = 2*i + 1, 2*i + 2
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child
    if largest != i:
        swap(arr, largest, i)
        max_heapify(arr, n, largest)
    
        
def build_max_heap(arr, n):
    startingIndex = n//2 + 1
    for node in range(startingIndex, -1, -1):
        max_heapify(arr, n, node)
    return arr

def heapsort(arr, n):
    heap = build_max_heap(arr, n)
    ordered = []
    for i in range(n-1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        ordered.insert(0, heap[i])
        max_heapify(heap, i, 0)
    return heap
        
def partition(arr, pivot, end):
    q, fromR, fromL = arr[pivot], pivot+1, end
    while True:
        for i in range(fromR, end+1):
            if arr[i] > q:
                fromR = i; break
        for j in range(fromL, 0, -1):
            if arr[j] <= q:
                fromL = j; break
        if fromR > fromL:
            break
        arr = swap(arr, fromR, fromL)
    arr = swap(arr, pivot, fromL)
    return arr

    
def partition3(arr, pivot, end):
    # 9
    # 4 5 6 4 1 2 5 7 4
    j, k = 0, end
    while j <= k:
        arr_j = arr[j]; arr_p = arr[pivot]
        if arr_j < arr_p:
            # swap pivot with smaller element
            arr[pivot], arr[j] = arr[j], arr[pivot]
            pivot += 1; j += 1
        elif arr_j > arr_p:
            # swap larger element with final compared element
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
        else:
            j += 1
    return arr


def verify_partition(arr, pivot, first = True):
    for i in arr:
        if first and i > pivot:
            return False
        elif first and i == pivot:
            first = False
        if not first and i < pivot:
            return False
    return True
   
        
def swap(arr, item1, item2):
    arr[item1], arr[item2] = arr[item2], arr[item1]
    return arr
    
    
def select(list, left, right, k):
    
    def partition(list, left, right, partitionIndex):
        p = list[partitionIndex]
        list[partitionIndex], list[right] = list[right], list[partitionIndex]
        storeIndex = left
        for i in range(left, right):
            if list[i] < p:
                list[storeIndex], list[i] = list[i], list[storeIndex]
                storeIndex += 1
        list[right], list[storeIndex] = list[storeIndex], list[right]
        return storeIndex
    if len(list) == 1:
        return list[0]
    
    if left == right:
        return list[left]
    
    pivotIndex = partition(list, left, right, random.randint(left+1, right-1))
    
    if k == pivotIndex:
        return list[k]
    elif k < pivotIndex:
        return select(list, left, pivotIndex-1, k)
    else:
        return select(list, pivotIndex+1, right, k)


def __partition(arr, lo, hi):
    pivot, i = arr[hi], lo
    for j in range(lo, hi+1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i


def quicksort(arr, lo, hi):
    if lo < hi:
        p = __partition(arr, lo, hi)
        quicksort(arr, lo, p-1)
        quicksort(arr, p+1, hi)
        return arr


# tester
if __name__ == '__main__':
    l = 7
    arr = [int(x) for x in '5 -2 4 7 8 -10 11'.split()]
    print(*arr)
    print(*quicksort(arr, 0, l-1))
