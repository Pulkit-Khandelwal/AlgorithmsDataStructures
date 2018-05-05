class Sort(object):
    def __init__(self, data):
        self.data = data
        pass

    def selection(self):

        for i in range(len(self.data)):
            min_value = self.data[i]
            index = i
            for j in range(len(self.data)-i-1):
                if self.data[j+i+1] < min_value:
                    min_value = self.data[j+i+1]
                    index = j+i+1
            temp = self.data[i]
            self.data[index] = temp
            self.data[i] = min_value
        return self.data

    def insertion(self):

        for i in range(len(self.data)-1):
            curr_index = i+1
            key = self.data[curr_index]
            while i >= 0:
                if key < self.data[i]:
                    self.data[i+1] = self.data[i]
                    i = i-1
                else:
                    break
            self.data[i+1] = key
        return self.data

    def quick(self, start, end):
        """
        Inplace quick sort algorithm
        """

        def partition(array, start, end):
            partition_index = start
            pivot = array[end]

            for i in range(start, end):
                if array[i] <= pivot:
                    array[partition_index], array[i] = array[i], array[partition_index]
                    partition_index += 1

            array[partition_index], array[end] = array[end], array[partition_index]
            return partition_index

        def quicksort(array, start, end):
            if start < end:
                partition_index = partition(array, start, end)
                quicksort(array, start, partition_index-1)
                quicksort(array, partition_index+1, end)

        quicksort(self.data, start, end)
        return self.data

    def merge_sort(self):
        """
        Merge Sort
        """

        def merge(A, L, R):
            nL = len(L)
            nR = len(R)
            i = 0
            j = 0
            k = 0
            while i < nL and j < nR:
                if L[i] <= R[j]:
                    A[k] = L[i]
                    i += 1
                else:
                    A[k] = R[j]
                    j += 1
                k += 1

            while i < nL:
                A[k] = L[i]
                i += 1
                k += 1

            while j < nR:
                A[k] = R[j]
                j += 1
                k += 1

        def mergesort(A):
            nA = len(A)
            if nA < 2:
                return

            mid = int(nA / 2)
            L = A[:mid]
            R = A[mid:]

            mergesort(L)
            mergesort(R)
            merge(A, L, R)

        mergesort(self.data)
        return self.data

    def countingsort(self, data):
        """
        Works for integers between the range 0 and k
        """
        A = data
        B = [0] * len(A)
        k = max(A)
        C = [0] * int(k+1)

        for i in range(len(A)):
            C[A[i]] = C[A[i]] + 1

        for i in range(1, len(C)):
            C[i] = C[i] + C[i-1]

        for i in reversed(range(0, len(A))):
            B[C[A[i]]-1] = A[i]  # This -1 is because of the Python indexing notation
            C[A[i]] = C[A[i]] - 1

        return B

    def radix(self, d):
        """
        d: the highest order digit
        For example if the 456 has order = 3
        Using counting sort
        Alternate: Hashmap and LinkedList
        """

        def countsort(data, arr):
            """
            Works for integers between the range 0 and k.
            Note that this count sort is very slightly modified to accomodate
            Radix Sort
            """
            A = data
            B = [0] * len(A)
            k = max(A)
            C = [0] * int(k + 1)
            arr2 = [0] * len(A)

            for i in range(len(A)):
                C[A[i]] = C[A[i]] + 1

            for i in range(1, len(C)):
                C[i] = C[i] + C[i - 1]

            for i in reversed(range(0, len(A))):
                B[C[A[i]] - 1] = A[i]  # This -1 is because of the Python indexing notation
                arr2[C[A[i]] - 1] = arr[i]
                C[A[i]] = C[A[i]] - 1

            return arr2

        A = self.data
        B = [0] * len(A) # for temporarily storing the integers at significant bits

        mod_value = 10
        div_value = 1

        for i in range(1, d+1):
            B = [a % mod_value for a in A]
            B = [b / div_value for b in B]

            B = countsort(B, A)

            A=B
            mod_value *= 10
            div_value *= 10

        return B

    def BucketSort(self):
        """
        Slightly modified Bucker Sort. This is unlike the algorithm given in CLRS
        """
        pass

if __name__ == '__main__':
    data = [17,44,34,99,23,3333,2198,54,12,93,54,777,34,6] #6,83,7,85,3,393,276,34,142,98
    sort = Sort(data)
    length_data = len(data)
    #sorted_data = sort.selection()
    #sorted_data = sort.insertion()
    #sorted_data = sort.quick(start=0, end=length_data-1)
    #sorted_data = sort.merge_sort()
    #sorted_data = sort.countingsort(data)
    sorted_data = sort.radix(d=4)
    print(sorted_data)
