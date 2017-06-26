a = ' nat server asperaDUP{} protocol udp global 113.105.76.242 3300{} inside 172.16.101.22 3300{} no-reverse'
i = range(1,11)
lis =[]
for x in i:
    s = a.format(x,x,x)
    print(s)
