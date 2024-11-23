def find_sub(string1, sub_str):
    n = len(string1)
    m = len(sub_str)
    c = 0
    for i in range(n-m+1):
        match = True    
        for j in range(m):
            if string1[i+j] != sub_str[j]:
                match = False
                break
        if match:
            c+=1
    return c

str1 = "Hello World"
substr = "l"
print(find_sub(str1,substr))    