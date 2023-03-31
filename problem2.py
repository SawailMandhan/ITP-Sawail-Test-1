def takeInput():
  a=int(input("enter the first number: "))
  b= int(input("enter the second number: "))
  operator =input("Enter the Arthematic operator: ")
  # operator ="+,-,*,/"
  return (a,b,operator)

(a,b,operator)=takeInput()



def displayoutput(a,b,operator):
  if (operator=="+"):
    print(a+b)
  elif (operator=="-"):
    print(a-b)
  elif (operator=="*"):
    print(a*b)
  elif (operator=="/"):
    print(a/b)
  else:
    print("invalid syntax")

displayoutput(a,b,operator)
   