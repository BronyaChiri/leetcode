# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
       
        def calculate(t):
            n=1
            while t.next != None:
                n = n * 10 + t.val
                t = t.next
            n = n * 10 + t.val
            return n
        
        def reverse(n):
            s=0
            while n>=1:
                s = s*10 + n%10
                n = (n-n%10)//10
            s = s//10
            # print(f'{s}  ')
            return s
        n1 = reverse(calculate(l1))
        n2 = reverse(calculate(l2))
        n3 = n1 + n2
        
        l3 = ListNode()
        t = l3
        
        while n3>=10 :
            l3.val = n3%10
            l3.next = ListNode()
            l3 = l3.next 
            n3 = (n3-n3%10)//10 
        l3.val = n3%10  
        return t
        
