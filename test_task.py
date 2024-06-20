import sys

# Чтение элементов массива из файла
with open(sys.argv[1], 'rt') as file:
    nums = [int(line.strip()) for line in file.readlines()]

def stepsCounting(nums):

    steps = 0
    nums.sort()

    # Поиск медианы 
    if len(nums) % 2 == 0:
        median = (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) // 2
    else:
        median = nums[len(nums) // 2]

    # Приведение элементов массива к значению медианы и подсчёт шагов
    for i in range(len(nums)):
        while nums[i] != median:
            if nums[i] < median:
                nums[i] += 1
                steps += 1
            if nums[i] > median:
                nums[i] -= 1
                steps += 1
                
    return steps

print(stepsCounting(nums))