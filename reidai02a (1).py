n = int(input("整数を入力してください> "))

print("------")
#その１：４つの場合ごとにif文で
if n%2 == 0:
    print("2の倍数")

if n%3 == 0:
    print("3の倍数")

if (n%2 == 0) and (n%3 == 0):
    print("2と3の公倍数")

if not((n%2 == 0) or (n%3 == 0)):
    #(n%2 != 0) and (n%3 !=0): と同じ
    print("2または3の倍数ではない")

print("---")
#その２：ifの入れ子で、条件を一つずつ
if n%2 == 0:
    if n%3 == 0:
        print("2と3の公倍数")
    else:
        print("2の倍数　#3の倍数ではない")
else:
    if n%3 == 0:
        print("3の倍数　#2の倍数ではない")
    else:
        print("2または3の倍数ではない")

print("------")
#その３：ifの入れ子を使わない、elifを使う
if (n%2 == 0) and (n%3 == 0):
    print("2と3の公倍数")
elif (n%2 == 0): # and (n%3 != 0)
    print("2の倍数　#3の倍数ではない")
elif (n%3 == 0): # and (n%2 != 0)
    print("3の倍数　#2の倍数ではない")
else: #not((n%2 == 0) or (n%3 == 0))
    print("2または3の倍数ではない")
