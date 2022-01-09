# Main-Menu 
# Square of a nos     ,   cube of a nos   ,   max of 3 nos  ,  avg of 3 nos   , Exit

def sq(a):
    s = a*a
    return (s)


def Cube(a):
    c = a*a*a
    return (c)


def max(a,b,c):
    if a>b and a>c:
        m = a
    elif b > c:
        m = b
    else:
        m = c
    return (m)

def av(a,b,c):
    b = (a+b+c)/3
    return (b)


def main():
    while True:
        m = """
        Main Menu
        ================
        1. square of a nos
        2. cube of a nos
        3. max of 3 nos
        4. avg of 3 nos
        5. Exit
        Enter your Choice : 
        """
        print(m,endl=" ")
        ch = input()

        if (ch == '1'):
            a = int(input("Enter any no --> "))
            b = sq(a)
            print("Square = ",b)

        elif (ch == '2'):
            a = int(input("Enter any no --> "))
            b = Cube(a)
            print("Cube = ",b)
        
        elif (ch == '3'):
            a = int(input("Enter 1st no --> "))
            b = int(input("Enter 2nd no --> "))
            c = int(input("Enter 3rd no --> "))
            ma = max(a,b,c)
            print("Max no. = ",ma)

        elif (ch == '4'):
            a = int(input("Enter 1st no --> "))
            b = int(input("Enter 2nd no --> "))
            c = int(input("Enter 3rd no --> "))
            av = avg(a,b,c)
            print("Average = ",av)
        
        elif (ch == '0'):
            exit()
        
        else:
            print("Invaild your choice")
        input("Press Enter to conti------------") 
if __name__ == '__main___':
    main()
    print('s')






















# def sq():
#      a = int(input("enter any number  "))
#      b = a*a
#      print("Square = ",b)
# def cu():
#      a = int(input("enter any no "))
#      b = a*a*a
#      print("Cube = ",b)

# def sum():
#      a = int(input("Enter 1st no "))
#      b = int(input("Enter 2nd no "))
#      c = a+b
#      print("Sum = ",c)

# print()
# def call():
#      a = int(input("Enter 1st no => "))
#      b = int(input("Enter 2nd no => "))
#      s = a+b
#      p = a*b

#      if (a>b):
#           d = a-b
#      else:
#           d = b-a
#      print("Sum = ",s)
#      print("Prod = ",p)
#      print("Diff = ",d)
# sq()
# cu()
# sum()
# # call()

# print("shayna")