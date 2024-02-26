def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    term_freq = {}
    for term in lst:
        if term in term_freq:
            term_freq[term] += 1
        else:
            term_freq[term] = 1
    
    if search_term in term_freq:
        return term_freq[term]
    else:
        return 0
