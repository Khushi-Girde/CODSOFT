import random, string

def build(length,lower,upper,digits,symbols):
    pools=[]
    if lower: pools.append(string.ascii_lowercase)
    if upper: pools.append(string.ascii_uppercase)
    if digits: pools.append(string.digits)
    if symbols: pools.append("!@#$%^&*()-_+=")
    if not pools: pools=[string.ascii_letters+string.digits]

    allchars="".join(pools)
    pwd=[random.choice(p) for p in pools]
    while len(pwd)<length: pwd.append(random.choice(allchars))
    random.shuffle(pwd)
    return "".join(pwd)

def main():
    print("🔑 Password Generator")
    length=int(input("Length: "))
    count=int(input("How many? "))
    lower=input("Lowercase? y/n: ")=="y"
    upper=input("Uppercase? y/n: ")=="y"
    digits=input("Digits? y/n: ")=="y"
    symbols=input("Symbols? y/n: ")=="y"
    for i in range(count):
        print(f"Password {i+1}:", build(length,lower,upper,digits,symbols))

if __name__=="__main__":
    main()


