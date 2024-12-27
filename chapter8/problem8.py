
def rem(li, word):
    n = []
    
    for item in li:
        if not(item == word):
            n.append(item.strip(word))
    return n
        

li = ["Alpesh","Rahul","Satish"]
print(rem(li, "Alpesh"))