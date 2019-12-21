# create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.


def filter_list(l):
  print([x for x in l if type(x) == int])


filter_list([1,2,'a','b'])