class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        begin = 0
        end = len(head)-1
        quick_sort(head, 0, end)
        return head
    
    def quick_sort(self, array, begin, end):
        pivot = partition(array, begin, end)
        self.quick_sort(array, begin, pivot-1)
        self.quick_sort(array, pivot+1, end)

    def partition(self, array, begin, end):
        pivot = array[end]
        counter = begin-1

        # i fast pointer
        for i in range(begin, end):
            if array[i] >= pivot:
                counter += 1
                array[i], array[counter] = array[counter], array[i]
        
        array[counter+1], array[end] = array[end], array[counter+1]
        return counter+1
