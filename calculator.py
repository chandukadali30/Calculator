print("select operations:")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

choice=input("enter choice:")

n1=float(input("enter the first number:"))
n2=float(input("enter the second number:"))

if choice=='1':
   Add=n1+n2
   print("addition of n1 and n2 is:",Add)
         
elif choice=='2':
   sub=n1-n2
   print("subtaction of n1 and n2 is:",sub)
         
elif choice=='3':
   mul=n1*n2
   print("multiplication of n1 and n2 is:",mul)
         
                  
elif choice=='4':
         if n2==0:
            print("error!cannot divide by zero")
         else:
             div=n1/n2
             print("division of n1 and n2 is:",div)
else:
    print("Invalid Input!Please enter a valid input")


