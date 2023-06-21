def move_to_bottom(d, k):
  if k not in d:
    return 'The key is not in the dictionary'
  else:
    value = d.pop(k)
    d[k] = value
    return d