    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

    return (num1 + num2 + num3) / 3

    mean = find_mean(num1, num2, num3)
    std = ((num1 - mean)**2 +(num2 - mean)**2 + (num3 - mean)**2) ** 0.5
    return mean, std
