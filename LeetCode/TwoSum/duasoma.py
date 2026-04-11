class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = []
        self.target = target
        numero = {}
        for i, num in enumerate(nums):
            complemento = target - num
            if complemento in numero:
                 return [numero[complemento], i]    
            numero[num] = i


"""Dado um array de inteiros nums e um inteiro target, retorne os índices dos dois números de forma que a soma deles seja igual atarget .

Você pode assumir que cada entrada terá exatamente uma solução e que não poderá usar o mesmo elemento duas vezes.

Você pode retornar a resposta em qualquer ordem.

 

Exemplo 1:

Entrada: nums = [2,7,11,15], alvo = 9
 Saída: [0,1]
 Explicação: Como nums[0] + nums[1] == 9, retornamos [0, 1].
Exemplo 2:

Entrada: nums = [3,2,4], alvo = 6
 Saída: [1,2]
Exemplo 3:

Entrada: nums = [3,3], alvo = 6
 Saída: [0,1]
 

Restrições:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Só existe uma resposta válida.
 

Pergunta complementar:  Você consegue pensar em um algoritmo com complexidade de tempo menor que O(n)?O(n2) """


