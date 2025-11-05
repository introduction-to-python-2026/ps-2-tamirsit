def find_max_number(num1, num2, num3):
   if num1 >= num2 and num1 >= num3:
      return num1
   elif num2 >= num1 and num2 >= num3:
      return num2
   else:
      return num3
    
    def find_max_number(num1, num2, num3):
   if num1 >= num2 and num1 >= num3:
      return num1
   elif num2 >= num1 and num2 >= num3:
      return num2
   else:
      return num3
    
    import math

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    sum_sq_diff = ((num1 - mean)**2 + (num2 - mean)**2 + (num3 - mean)**2)
    std = math.sqrt(sum_sq_diff / 3)
    return mean, std
