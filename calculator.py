import math

def add(num1,num2):
    return num1+num2
    
def sub(num1,num2):
    return num1-num2
    
def multiply(num1,num2):
    return num1*num2
    
def divison(num1,num2):
    return num1/num2;

def main():
    while True:
        print("1.Add")
        print("2.Substraction")
        print("3.Multiplication")
        print("4.Divide")
        print("5.Squareroot")
        
        choice = input("Enter your choice:")
        if choice == "1":
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice == "2":
             num1 = float(input("Enter first number:"))
             num2 = float(input("Enter second number:"))
             print(num1,"-",num2,"=",sub(num1,num2))
        elif choice == "3":
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))
            print(num1,"X",num2,"=",multiply(num1,num2))
        elif choice == "4":
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))
            print(num1,"/",num2,"=",divison(num1,num2))
        elif choice == "5":
            x = int(input("Enter the NUmber:"))
            print("Square root of", x, "is:",math.sqrt(x))
        else:
            print("Invalid opperation!")
            
        next_calculation=input("Another Calculation(YES/NO):")
        if next_calculation == "YES":
            bool(1)
        elif next_calculation == "NO":
            break;
            
if __name__ == "__main__":
    main()
