from art import logo
print(logo)
def add(a,b):
  return (a+b)
def sub(a,b):
  return (a-b)
def mult(a,b):
  return (a*b)
def div(a,b):
  return (a/b)
operations = {
  "+":add,
  "-":sub,
  "*":mult,
  "/":div
}

num1=float(input("Enter the first number :"))
print("+\n-\n*\n/")
operator=input("Enter the operation :")
num2=float(input("Enter the secont number :"))  

cal_function = operations[operator]
answer = cal_function(num1,num2)
print(answer)



while 1:
  step=input("press 'no' to exit \n For new calculation press 'n'\n for doing calculation in older answer press 'o' ")
  if step=="no":
    break
  if step == "n":
    num1=int(input("Enter the first number :"))
    print("+\n-\n*\n/")
    operator=input("Enter the operation :")
    num2=int(input("Enter the secont number :"))
    cal_function = operations[operator]
    answer = cal_function(num1,num2)
    print(answer)
  if step =="o":
    print("+\n-\n*\n/")
    operator=input("Enter the operator")
    num2=int(input("Enter the number"))
    
    cal_function = operations[operator]
    answer = cal_function(answer,num2)
    print(answer)


