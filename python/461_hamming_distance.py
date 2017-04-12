class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        tmp = x ^ y
        return self.count_ones(tmp)
    
    def count_ones(self, num):
        count = 0
        while num > 0:
            count += 1 if num % 2 == 1 else 0
            num = num / 2
        return count

# Optimize
# 上面的遍历每一位的方法并不高效，还可以进一步优化，假如数为num, num & (num - 1)可以快速地移除最右边的bit 1， 一直循环到num为0, 总的循环数就是num中bit 1的个数。
    def hammingDistance(self,x,y):
        num = x ^ y
        count = 0
        while num:
            count += 1
            num = num & (num-1)
        return count