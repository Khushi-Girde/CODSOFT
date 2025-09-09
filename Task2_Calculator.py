import math

def calculate(a, b, op):
    try:
        if op=="+": return a+b
        if op=="-": return a-b
        if op=="*": return a*b
        if op=="/": return "∞" if b==0 else a/b
        if op=="%": return a%b
        if op=="^": return a**b
    except Exception as e:
        return f"Error: {e}"
    return "❌ Unknown op"

def main():
    print("🧮 Advanced Calculator")
    while True:
        print("\nOperations: + - * / % ^ sqrt exit")
        op=input("Choose: ")
        if op=="exit": break
        if op=="sqrt":
            x=float(input("Enter number: "))
            print("√ =", math.sqrt(x))
            continue
        try:
            x=float(input("First: "))
            y=float(input("Second: "))
        except: print("❌ numbers only"); continue
        print("Result =", calculate(x,y,op))

if __name__=="__main__":
    main()
