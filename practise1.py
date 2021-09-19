def permutations(letters):
 
    if not letters:
        return []
 
    partial = []
 
    partial.append(letters[0])
 
    for i in range(1, len(letters)):
 
        for j in reversed(range(len(partial))):
 
            curr = partial.pop(j)
    
            for k in range(len(curr) + 1):
                partial.append(curr[:k] + letters[i] + curr[k:])
 
    print(partial)

letters = 'abc'
permutations(letters)