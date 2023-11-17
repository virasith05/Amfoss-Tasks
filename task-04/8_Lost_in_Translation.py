def can_say_hello(s):
    target_word = "hello"
    i = 0  
    for char in s:
        if char == target_word[i]:
            i += 1
            if i == len(target_word):
                return "YES"  
    
    return "NO"

s = input().strip()

result = can_say_hello(s)
print(result)
