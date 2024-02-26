def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    word_frequency = {}

    for char in word:
        char = str.lower(char)
        if char in word_frequency:
            word_frequency[char] += 1
        else:
            word_frequency[char] = 1

    letter = str.lower(letter)
    if letter in word_frequency:
        return word_frequency[letter]
    else:
        return 0