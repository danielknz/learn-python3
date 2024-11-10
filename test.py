try:
  mylist = 1 / 0
  #print(myList[1])
except NameError:
  print("Variable aaa is not defined")
except ZeroDivisionError:
  print("A ZeroDivisionError Occured")
except:
  print("Something else went wrong")