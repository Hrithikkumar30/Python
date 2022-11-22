# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentNode = head
        
        if head is None:
            return head
        
        while currentNode.next:
            NextNode = currentNode.next
            
            if NextNode :
                if currentNode.val == NextNode.val:
                    currentNode.next = NextNode.next
                else:
                    currentNode = currentNode.next
                    
        return head
                
                
            
        