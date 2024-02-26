def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_freq = {}
    num2_freq = {}
    num1 = str(num1)
    num2 = str(num2)
    for num in num1:
        if num not in num1_freq:
            num1_freq[num] = 1
        else:
            num1_freq[num] +=1

    for num in num2:
        if num not in num2_freq:
            num2_freq[num] = 1
        else:
            num2_freq[num] +=1

    for key in num1_freq.keys():
        if key not in num2_freq:
            return False
        if num1_freq[key] != num2_freq[key]:
            return False
    
    for key in num2_freq.keys():
        if key not in num1_freq:
            return False
    
    return True