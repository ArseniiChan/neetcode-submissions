class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Collect all values in an array
        values = []  
        current = head  
        
        while current:
            values.append(current.val)
            current = current.next
        
        # Step 2: Handle empty list
        if not values:
            return None
        
        # Step 3: Reverse the array
        values.reverse()  # or values = values[::-1]
        
        # Step 4: Build new linked list from reversed array
        new_head = ListNode(values[0])
        current = new_head
        
        for i in range(1, len(values)):
            current.next = ListNode(values[i])
            current = current.next
        
        return new_head