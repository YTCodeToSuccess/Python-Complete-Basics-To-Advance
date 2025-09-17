# Driver function to test the code
import sys

if __name__ == "__main__":
      x =10
      y=10
      print(f"x = {id(x)}, y = {id(y)}")

      #mutable
      a = [1,2,3]
      print(f"a = {id(a)}")
      a.append(4)
      print(f" after modification a = {id(a)}")

      #immutable
      a = 10
      print(f"a int  = {id(a)}")
      a = 20
      print(f" after int modification a = {id(a)}")

      #data types in python
      a = 10 #int
      b = 10.5 #float
      c = 1 + 2j #complex
      d = "Hello" #string
      e = [1,2,3] #list
      f = (1,2,3) #tuple
      g = {1,2,3} #set
      h = {'a':1, 'b':2} #dictionary
      i = True #boolean
      j = None #NoneType
      print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h), type(i), type(j))

      for i in range(len(d)) : 
            print(d[i])

      print(sys.getsizeof(a), sys.getsizeof(b), sys.getsizeof(c), sys.getsizeof(d), sys.getsizeof(e), sys.getsizeof(f), sys.getsizeof(g), sys.getsizeof(h), sys.getsizeof(i), sys.getsizeof(j))

      