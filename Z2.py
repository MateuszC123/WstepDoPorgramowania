x = input ("wprowadz litere: ")
if len(x)>1 or len(x)==0:
    print("jest za duzo znakow")
    exit()
if 'a' <= x <= 'z':
    print("litera jest mala")
elif 'A' <= x <= 'Z':
    print("litera jest duza")
else:
    print("to nie jest litera")




