cells = input("Enter cells:" )
a = cells[0]
b = cells[1]
c = cells[2]
d = cells[3]
e = cells[4]
f = cells[5]
g = cells[6]
h = cells[7]
i = cells[8]
result = ""
x = [x for x in cells if x == "X"]
o = [o for o in cells if o == "O"]

def win(value):
    global a, b, c, d, e, f, g, h, i
    if a + b + c == value * 3:
        return True
    if d + e + f == value * 3:
        return True
    if g + h + i == value * 3:
        return True
    if a + d + g == value * 3:
        return True
    if b + e + h == value * 3:
        return True
    if c + f + i == value * 3:
        return True
    if a + e + i == value * 3:
        return True
    if c + e + g == value * 3:
        return True
    else:
        return False

if len(x) + 1 < len(o) or len(o) + 1 < len(x):
    result = "Impossible"

elif win("X") and win("O"):
    result = "Impossible"
    
elif win("X"):
    result = "X wins"
    
elif win("O"):
    result = "O wins"
    
else:
    if cells.count("_") > 0:
        result = "Game not finished"
        
    else:
        result = "Draw"

print("""---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------""".format(a, b, c, d, e, f, g, h, i))

print(result)