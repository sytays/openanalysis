from openanalysis.sorting import SortAnalyzer, SortingAlgorithm
import numpy as np


class BubbleSort(SortingAlgorithm):
    def __init__(self):
        SortingAlgorithm.__init__(self, "Bubble Sort")

    def sort(self, array, visualization=False):
        SortingAlgorithm.sort(self, array, visualization)
        for i in range(0, len(array)):
            exch = False
            for j in range(0, len(array) - i - 1):
                self.count += 1
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    exch = True
                if visualization:
                    self.hist_array = np.vstack([self.hist_array, array])
            if not exch:
                break
        if visualization:
            self.hist_array = np.vstack([self.hist_array, array])


class InsertionSort(SortingAlgorithm):
    def __init__(self):
        SortingAlgorithm.__init__(self, "Insertion Sort")

    def sort(self, array, visualization=False):
        SortingAlgorithm.sort(self, array, visualization)
        for i in range(1, len(array)):
            ele = array[i]
            ins_pos = i - 1
            while ins_pos >= 0 and ele < array[ins_pos]:
                self.count += 1
                array[ins_pos + 1] = array[ins_pos]
                ins_pos -= 1
                if visualization:
                    self.hist_array = np.vstack([self.hist_array, array])
            array[ins_pos + 1] = ele
        if visualization:
            self.hist_array = np.vstack([self.hist_array, array])


class SelectionSort(SortingAlgorithm):
    def __init__(self):
        SortingAlgorithm.__init__(self, "Selection Sort")

    def sort(self, array, visualization=False):
        SortingAlgorithm.sort(self, array, visualization)
        for i in range(len(array)):
            min_index = i
            for j in range(i + 1, len(array)):
                self.count += 1
                if array[min_index] > array[j]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]
            if visualization:
                self.hist_array = np.vstack([self.hist_array, array])
        if visualization:
            self.hist_array = np.vstack([self.hist_array, array])


class MergeSort(SortingAlgorithm):
    def __init__(self):
        SortingAlgorithm.__init__(self, "Merge Sort")

    def sort(self, array, visualization=False):
        SortingAlgorithm.sort(self, array, visualization)
        unit = 1
        while unit <= len(array):
            for h in range(0, len(array), unit * 2):
                l, r = h, min(len(array), h + 2 * unit)
                mid = h + unit
                # merge xs[h:h + 2 * unit]
                p, q = l, mid
                while p < mid and q < r:
                    self.count += 1
                    if array[p] < array[q]:
                        p += 1
                    else:
                        tmp = array[q]
                        array[p + 1: q + 1] = array[p:q]
                        array[p] = tmp
                        p, mid, q = p + 1, mid + 1, q + 1
                    if visualization:
                        self.hist_array = np.vstack([self.hist_array, array])
            unit *= 2
        if visualization:
            self.hist_array = np.vstack([self.hist_array, array])


class MergeSortRecursive(SortingAlgorithm):
    def __init__(self):
        SortingAlgorithm.__init__(self, "Merge Sort")

    def sort(self, array, visualization=False):
        SortingAlgorithm.sort(self, array, visualization)
        self.visualization = visualization
        self.split(array, 0, len(array) - 1)

    def split(self, array, low, high):
        if low < high:
            mid = (low + high) // 2
            self.split(array, low, mid)
            self.split(array, mid + 1, high)
            self.merge_alternative(array, low, mid, high)

    def merge(self, array, low, mid, high):
        p, q = low, mid + 1
        while p <= mid and q <= high:
            self.count += 1
            if array[p] <= array[q]:
                p += 1
            else:
                tmp = array[q]
                array[p + 1: q + 1] = array[p:q]
                array[p] = tmp
                p, mid, q = p + 1, mid + 1, q + 1
            if self.visualization:
                self.hist_array = np.vstack([self.hist_array, array])

    def merge_alternative(self, array, low, mid, high):
        left = np.copy(array[low: mid + 1])
        right = np.copy(array[mid + 1: high + 1])
        i, j, k = 0, 0, low
        while i < len(left) and j < len(right):
            self.count += 1
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
            if self.visualization:
                self.hist_array = np.vstack((self.hist_array, array))
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


class HeapSort(SortingAlgorithm):
    def __init__(self):
        SortingAlgorithm.__init__(self, "Heapsort")

    def sort(self, array, visualization=False):
        SortingAlgorithm.sort(self, array, visualization)
        # convert aList to heap
        length = len(array) - 1
        leastParent = int(length / 2)
        for i in range(leastParent, -1, -1):
            self.moveDown(array, i, length, visualization)

        # flatten heap into sorted array
        for i in range(length, 0, -1):
            if array[0] > array[i]:
                array[0], array[i] = array[i], array[0]
                self.moveDown(array, 0, i - 1, visualization)
        if visualization:
            self.hist_array = np.vstack([self.hist_array, array])

    def moveDown(self, aList, first: int, last: int, visualization: bool):
        largest = 2 * first + 1
        while largest <= last:
            # right child exists and is larger than left child
            self.count += 1
            if (largest < last) and (aList[largest] < aList[largest + 1]):
                largest += 1

            # right child is larger than parent
            if aList[largest] > aList[first]:
                aList[largest], aList[first] = aList[first], aList[largest]
                # move down to largest child
                first = largest
                largest = 2 * first + 1
                if visualization:
                    self.hist_array = np.vstack([self.hist_array, aList])
            else:
                return  # force exit


class QuickSort(SortingAlgorithm):
    def __init__(self):
        SortingAlgorithm.__init__(self, "Quicksort")

    @staticmethod
    def __median_of_three(array, start: int, end: int, visualization=False):
        # Double underscore before the name of a method makes it private
        histarr = None
        count = 0
        if visualization:
            histarr = np.array(array)
        median = int((end - start) / 2)
        median = median + start
        left = start + 1
        if (array[median] - array[end - 1]) * (array[start] - array[median]) >= 0:
            array[start], array[median] = array[median], array[start]
        elif (array[end - 1] - array[median]) * (array[start] - array[end - 1]) >= 0:
            array[start], array[end - 1] = array[end - 1], array[start]
        pivot = array[start]
        for right in range(start, end + 1):
            count += 1
            if pivot > array[right]:
                array[left], array[right] = array[right], array[left]
                if visualization:
                    histarr = np.vstack([histarr, array])
                left = left + 1
        array[start], array[left - 1] = array[left - 1], array[start]
        return left - 1, histarr, count

    @staticmethod
    def __right_partition(arr, l: int, h: int, visualization=False):
        i = (l - 1)
        x = arr[h]
        hist = None
        if visualization:
            hist = np.array(arr)
        count = 0
        for j in range(l, h):
            if arr[j] <= x:
                count += 1
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                if visualization:
                    hist = np.vstack([hist, arr])
        arr[i + 1], arr[h] = arr[h], arr[i + 1]
        return i + 1, hist, count

    def __quickSortIterative(self, arr, l: int, h: int, partition_alg=__right_partition,
                             visualization=False):
        # Create an auxiliary stack
        size = h - l + 1
        stack = [0] * size

        # initialize top of stack
        top = -1

        # push initial values of l and h to stack
        top = top + 1
        stack[top] = l
        top = top + 1
        stack[top] = h

        # Keep popping from stack while is not empty
        while top >= 0:

            # Pop h and l
            h = stack[top]
            top = top - 1
            l = stack[top]
            top = top - 1

            # Set pivot element at its correct position in
            # sorted array
            p, hist, comps = partition_alg(arr, l, h, visualization)
            self.count += comps
            if visualization:
                self.hist_array = np.vstack([self.hist_array, hist])
            # If there are elements on left side of pivot,
            # then push left side to stack
            if p - 1 > l:
                top = top + 1
                stack[top] = l
                top = top + 1
                stack[top] = p - 1

            # If there are elements on right side of pivot,
            # then push right side to stack
            if p + 1 < h:
                top = top + 1
                stack[top] = p + 1
                top = top + 1
                stack[top] = h
        if visualization:
            self.hist_array = np.vstack([self.hist_array, arr])

    def sort(self, array, visualization=False):
        SortingAlgorithm.sort(self, array, visualization)
        self.__quickSortIterative(array, 0, len(array) - 1, partition_alg=self.__median_of_three,
                                  visualization=visualization)


class QucikSortRecursive(SortingAlgorithm):
    def __init__(self):
        SortingAlgorithm.__init__(self,"Quick Sort Recursive")

    def sort(self, array, visualization = False):
        SortingAlgorithm.sort(self,array,visualization)
        self.visualization = visualization
        n = len(array)
        self.quickSort(array, 0, n - 1)

    def partition(self,arr, low, high):
        i = (low - 1)  # index of smaller element
        pivot = arr[high]  # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                if self.visualization:
                    self.hist_array = np.vstack((self.hist_array,arr))

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickSort(self,arr, low, high):
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)
            if self.visualization:
                self.hist_array = np.vstack((self.hist_array, arr))

if __name__ == "__main__":
    SortAnalyzer(QucikSortRecursive).visualize(num=500)
