a, b, c = map(int, input().split())

if a == b == c:
    x = (a*1000)+10000
    print(x)
elif a == b or a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:
    print(max(a, b, c)*100)