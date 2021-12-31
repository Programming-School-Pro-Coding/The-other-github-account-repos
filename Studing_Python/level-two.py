# Level-2
# even number like 0, 2, 4, 6, 8, ....etc
def remove_even_num(nums):
    for i in [0, 2, 4, 6, 8]:
        if i in nums:
            nums.clear()


# output
test1 = remove_even_num([5, 32, 15, 2, 0, 3])
test2 = remove_even_num([11, 7, 16, 9])
test3 = remove_even_num([1, 18, 60, 15, 42, 4])


print(test1)  # [5, 15, 3] printed
print(test2)  # [11, 7, 16, 9] printed
print(test3)  # [1, 15] printed
