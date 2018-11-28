data = 0
arr = []
def fun(a1):
    global arr
    global data
    if(a1 <= 63):
        data = data + 1
        arr.append(a1)
        fun(2*a1+1)
        fun(2*(a1+1))
fun(0)
str = "bcec8d7dcda25d91ed3e0b720cbb6cf202b09fedbc3e017774273ef5d5581794"
input = [0 for x in range(64)]
for i in range(64):
    input[arr[i]] = str[i]
flag = "".join(input)
print(flag)
