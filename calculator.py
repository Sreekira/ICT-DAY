# -*- coding: utf-8 -*-
"""calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MAxm13wS1a9LkJa7vO2NfePftz4iV-tK
"""

class calculator:
   def add(self,x,y):
       return x+y

   def subtract (self,x,y):
       return x-y

   def multiply(self,x,y):
      return x*y

   def divide(self,x,y):
      if y==0:
          return
      else:
          return x/y
          calc =calculator()
          print("Select operation:")
          print("1.Add")
          print("2.Subtract")
          print("3.Multiply")
          print("4. Divide")

          while True:
            choice = input("Enter choice (1/2/3/4):")

          if choice in ('1','2','3','4'):
                num1 = float(input("Enter first number:"))
                num2 = float(input("Enter second number:"))
                if choice== '1':
                  print("Result:",calc.add(num1,num2))
                elif choice == '2':
                  print("Result:",calc.subtract(num1,num2))
                elif choice == '3':
                  print("Result:",calc.mutiply(num1,num2))
                elif choice == '4':
                  print("Result:",calc.divide(num1,num2))
                else:
                  print("invalid input")

class Calculator:
    def calculate(self, expression):
        try:
            result = eval(expression)
            return result
        except Exception as e:
            return f"Error: {str(e)}"

calc = Calculator()

print("Enter a mathematical expression (e.g., 2 + 3 * 4):")

while True:
    expression = input("Expression: ")

    if expression.lower() == "exit":
        break

    result = calc.calculate(expression)
    print("Result:",result)