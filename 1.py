s = input()

k = input()

n = int(k.split(" ")[0])

c = k.split(" ")[1]

s = s[:n] + c + s[n+1:]

print(s)