# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)  # nó inicial (facilita)
        atual = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            soma = v1 + v2 + carry
            carry = soma // 10

            atual.next = ListNode(soma % 10)
            atual = atual.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
    
def criar_lista(valores):
        dummy = ListNode(0)
        atual = dummy
        
        for v in valores:
            atual.next = ListNode(v)
            atual = atual.next
        
        return dummy.next
    
def imprimir_lista(node):
        while node:
            print(node.val, end=" -> ")
            node = node.next



l1 = criar_lista([2,4,3])
l2 = criar_lista([5,6,4])

solucao = Solution()
resultado = solucao.addTwoNumbers(l1, l2)
imprimir_lista(resultado)

        