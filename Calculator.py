def add(n1,n2):
  return n1 + n2
  
def subtract(n1,n2):
  return n1 - n2
def multiply(n1,n2):
  return n1 * n2
  
def divide(n1,n2):
  return n1 / n2
  
def floor_division(n1,n2):
  return n1//n2

def modulus(n1,n2):
  return n1 % n2

def square_root(n1):
  return n1**2

def cube(n1):
  return n1**3

operator_names = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "//": floor_division,
    "%": modulus,
    "**": square_root,
    "***": cube
}  
def calculator():
  num1 = float(input("what's the first number?: "))
  for symbol in operator_names:
    print(symbol)
  end = True
  while end:
      operator = input("pick an operation: ")
      if operator == "**":  # Check for square root
          answer = square_root(num1)
      elif operator == "***":  # Check for cube
            answer = cube(num1)
      else:
        num2 = float(input("what's the next number?: "))
        calc = operator_names[operator]
        answer = calc(num1,num2)
        print(f"{num1} {operator} {num2} = {answer}")
  
      if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator.: ") == "y":
        num1 = answer
      else:
        end = False
        calculator()

calculator()  
