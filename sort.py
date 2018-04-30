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


if __name__ == '__main__':
    data = [8,3,6,8,3,0,13,-1,4,1]
    sort = Sort(data)
    length_data = len(data)
    #sorted_data = sort.selection()
    #sorted_data = sort.insertion()
    sorted_data = sort.quick(start=0, end=length_data-1)
    print(sorted_data)
