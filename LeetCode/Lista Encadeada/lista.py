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

"""São dadas duas listas ligadas não vazias representando dois números inteiros não negativos. Os dígitos estão armazenados em ordem inversa e cada um dos nós contém um único dígito. Some os dois números e retorne a soma como uma lista ligada.

Você pode assumir que os dois números não contêm nenhum zero à esquerda, exceto o próprio número 0.

Exemplo 1:


Entrada: l1 = [2,4,3], l2 = [5,6,4]
 Saída: [7,0,8]
 Explicação: 342 + 465 = 807.
Exemplo 2:

Entrada: l1 = [0], l2 = [0]
 Saída: [0]
Exemplo 3:

Entrada: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
 Saída: [8,9,9,9,0,0,0,1]
 

Restrições:

O número de nós em cada lista encadeada está no intervalo [1, 100].
0 <= Node.val <= 9
É garantido que a lista representa um número que não possui zeros à esquerda."""