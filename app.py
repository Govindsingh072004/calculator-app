from calc_func import do_addition,do_subtraction
from multiplu import do_multiplication
def main():
    print("Welcome to the calculator app")
    print("""
          \nSelect the Function from the given Options
          1. Add
          2. Subtract
          3. Multiply
          """)
    
    user_input=input("Select the funcation")
    a=int(input("value of A "))
    b =int(input("Value of B"))
    if user_input == "1":
        result = do_addition(a,b)
    elif user_input == "2":
        result=do_subtraction(a,b)
    elif user_input =="3":
        result=do_multiplication(a,b)    
    print("Result",result)        
    
    
if __name__ == "__main__":
        main()
    
    
    

