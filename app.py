from calculator import addition,subtract
from multiply import do_multipication

def main():
    print("welcome to the calculator")
    print('''
          \n select the function from the given below 
          1.Add
          2.Subtract
          3. Multiply''')
    
    user_input=input("Select the Option")
    a=int(input("Value of A"))
    b=int(input("Value of B"))


    if user_input=="1":
        result=addition(a,b)

    elif user_input=="2":
        result=subtract(a,b)

    elif user_input=="3":
        result=do_multipication(a,b)

    print("result,",result)


if __name__== "__main__" :
    main()