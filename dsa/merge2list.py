# Definition for singly-linked list.
# merge tw0 sorted list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1: ListNode, list2: ListNode)-> ListNode:
      
        head = SortedList = ListNode()
        
        while list1 and list2:
            if list1.val <= list2.val:
                SortedList.next = list1
                list1 = list1.next
                SortedList = SortedList.next
            else:
                SortedList = list2
                list2 = list2.next
                SortedList = SortedList.next

            
            
            SortedList.next = list1 or list2
        return head.next