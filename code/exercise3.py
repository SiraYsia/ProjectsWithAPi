# WRITE YOUR CODE HERE
def swap(dic):
  swapped_dic = {}

  for key, value in dic.items():
    if not hash(value):
      return "Cannot swap the keys and values for this dictionary"
    swapped_dic[value] = key

  return swapped_dic

# test code below

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : {3 : 4},
    5 : 'five'
  }

  swapped = swap(example_dict)
  print(swapped)