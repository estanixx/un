m = int(input())
nums = []
def insort(nums, n):
  for i, el in enumerate(nums):
    if n < el:
      nums.insert(i, n)
      return
  nums.append(n)
      
def get_mediana(nums):
  n = len(nums)
  if n % 2 == 0:
    left = nums[n // 2 - 1]
    right = nums[n // 2]
    if (left + right) % 2 == 0:
      return (left + right) // 2
    return f'{left + right}/2'
  else:
    return nums[n // 2]

while (num := int(input())) != 0:
  insort(nums, num)
  if len(nums) % m == 0:
    print(get_mediana(nums))