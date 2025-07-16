class Solution:
    __privateCounter = 0  # Private variable

    def sum(self):
        self.__privateCounter += 1
        print(self.__privateCounter)

# Creating object
count = Solution()
count.sum()
count.sum()

# Trying to access private member directly (will cause an error)
# print(count.__privateCounter)  

# Accessing private member using class name (correct way)
print(count._Solution__privateCounter)
