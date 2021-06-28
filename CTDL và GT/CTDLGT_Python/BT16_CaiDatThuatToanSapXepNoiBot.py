def bubble_sort(nums):  
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


random_list_of_nums = [25, 2, 45, 1, 34]  
bubble_sort(random_list_of_nums)  
print(random_list_of_nums) 