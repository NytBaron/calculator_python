#calculator

print("This is calculator made in python")
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))

print("The operand you can use are : add(+),sub(-),product,divide,reminder")
operand=input("Enter your operand: ")
add="+";
sub="-";
product="*";
divide="/";
reminder="%";


if operand==add:
    total=num1+num2;
    print(total);
elif operand==sub:
    total=num1-num2;
    print(total);
elif operand==product:
    total=num1*num2;
    print(total);
elif operand==divide:
    total=num1/num2;
    print(total);

elif operand==reminder:
    total=num1%num2;
    print(total);
else :
    print("Wrong expression plear enter the operand again")