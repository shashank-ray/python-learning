def is_unique(input_str):
  alphabet = set()
  for i in input_str:
    if i in alphabet:
      return False
    else:
      alphabet.add(i)
  return True