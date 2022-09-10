s = input()

k = input()

n = int(k.split(" ")[0]) #position

c = k.split(" ")[1] #character 

s = s[:n] + c + s[n+1:] #inserting character

print(s) #printing output